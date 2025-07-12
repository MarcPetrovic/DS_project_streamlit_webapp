import pandas as pd
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from utils.data_loader import load_csv_data  # Pfad ggf. anpassen
from utils.preprap_feature_engineering import build_pipeline
from utils.data_cleaning import get_cleaning_pipeline
from sklearn.model_selection import train_test_split
from utils.modelling_feature_engineering import build_modelling_pipeline
from feature_engine.creation import CyclicalFeatures
from sklearn import set_config

def load_data():
    """
    Generation of train and test data based on csv-files in data-folder.
    
    Returns:
        X_train, X_test, y_train, y_test: Pandas DataFrames/Series
    """
    # 1. input data (features)
    #X_train = load_csv_data("data/X_train_transformed2nd.csv", ignore_index_column=False)
    #X_test = load_csv_data("data/X_test_transformed2nd.csv", ignore_index_column=False)
    # 2. target feature (labels)
    #y_train = load_csv_data("data/y_train.csv", ignore_index_column=True).squeeze()
    #y_test = load_csv_data("data/y_test.csv", ignore_index_column=True).squeeze()
    # 3. Indices consolidation
    #X_train = X_train.reset_index(drop=True)
    #X_test = X_test.reset_index(drop=True)
    #y_train = y_train.reset_index(drop=True)
    #y_test = y_test.reset_index(drop=True)
    df = load_csv_data(
        filename="data/bank-additional-full.csv",
        sep=";",
        header=True,
        add_row_id=True,
        ignore_index_column=False
    )
      
    # temporäre aggregation view
    df_view = (
        df.groupby(["month", "cons.price.idx"], as_index=False)
        .agg(
            COUNT_TOTAL_PER_MONTH=("month", "count"),
            MAX_RN_month=("ROW_ID", "max")
        )
    )
        
    # year initiation
    df_view["year"] = df_view["MAX_RN_month"].apply(
        lambda x: 2008 if x <= 27690 else (2009 if x <= 39130 else 2010)
    )
        
    # Merge with original df
    df = df.merge(
        df_view[["month", "cons.price.idx", "year"]],
        on=["month", "cons.price.idx"],
        how="left"
    )

    df["date_period"] = pd.to_datetime(
        df["year"].astype(str) + "-" +
        pd.to_datetime(df["month"], format="%b").dt.month.astype(str),
        format="%Y-%m"
    ).dt.to_period("M")
        
    # Integer-type
    df["date_int"] = df["date_period"].dt.strftime('%Y%m').astype(int)
    df["date_period"] = df["date_period"].astype(str)      
      
    preprocessor = build_pipeline(df)  # Custom-built scikit-learn pipeline
    set_config(display='diagram')  
      
    preprocessor.set_output(transform='pandas')
    transformed_df = preprocessor.fit_transform(df)
      
    def make_streamlit_arrow_compatible(df: pd.DataFrame) -> pd.DataFrame:
        df = df.convert_dtypes()
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].apply(lambda x: str(x) if not pd.isna(x) else "")
        return df
      
    transformed_df = make_streamlit_arrow_compatible(transformed_df)
 
    cleaning_pipeline = get_cleaning_pipeline(columns_to_drop='duration')
    newdf = cleaning_pipeline.fit_transform(transformed_df)
 
    y = newdf['target'].copy().astype(int)
    X = newdf.drop(["y", "target",  "year", "date_int", 'date_period'], axis=1).copy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
  
    processor = build_modelling_pipeline(df)  # Custom-built scikit-learn pipeline
    set_config(display='diagram')
 
    processor.set_output(transform='pandas')
    X_train_transformed2nd = processor.fit_transform(X_train)
    X_test_transformed2nd = processor.transform(X_test)
      
    X_train_transformed2nd = make_streamlit_arrow_compatible(X_train_transformed2nd)
    X_test_transformed2nd = make_streamlit_arrow_compatible(X_test_transformed2nd)
 
    cyclical_features = CyclicalFeatures(variables=['month_numeric', 'day_of_week_numeric'], drop_original=True)
    X_train_transformed2nd = cyclical_features.fit_transform(X_train_transformed2nd)
    X_test_transformed2nd = cyclical_features.transform(X_test_transformed2nd)
    
    X_train = make_streamlit_arrow_compatible(X_train_transformed2nd)
    X_test = make_streamlit_arrow_compatible(X_test_transformed2nd)

    return X_train, X_test, y_train, y_test


def train_and_predict(model_type='logistic'):
    """
    Loading data, train data on classification modell and returns probabilities of X_test.

    Args:
        model_type (str): 'logistic' oder 'xgboost'

    Returns:
        model: trained modell
        y_proba: expected probabilities for y_test (only class 1)
        y_test: the empirical values
    """
    # 1. Loading data
    X_train, X_test, y_train, y_test = load_data()

    # 2. Select modell
    if model_type == 'logistic':
        model = LogisticRegression(max_iter=1000, solver='sag')#, random_state=42)
    elif model_type == 'xgboost':
        model = XGBClassifier(
            n_estimators=50, 
            objective='binary:logistic',
            use_label_encoder=False,
            eval_metric='logloss'
            #,
            #random_state=42
        )
    else:
        raise ValueError("Unexpected modell type. Select 'logistic' or 'xgboost'.")

    # 3. Train the modell
    model.fit(X_train, y_train)

    # 4. Calculation of expected probabilities (only class 1)
    y_proba = model.predict_proba(X_test)[:, 1]

    return model, y_proba, y_test

def train_model(model_type='logistic'):
    X_train, X_test, y_train, y_test = load_data()

    if model_type == 'logistic':
        model = LogisticRegression(max_iter=1000, solver='sag', random_state=42)
    elif model_type == 'xgboost':
        model = XGBClassifier(
            n_estimators=50,
            objective='binary:logistic',
            use_label_encoder=False,
            eval_metric='logloss',
            random_state=42
        )
    else:
        raise ValueError("Invalid model type")

    model.fit(X_train, y_train)
    return model, X_train, X_test, y_train, y_test
