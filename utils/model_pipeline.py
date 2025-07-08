import pandas as pd
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from utils.data_loader import load_csv_data  # Pfad ggf. anpassen

def load_data():
    """
    Loading train and test data based on csv-files in data-folder.
    
    Returns:
        X_train, X_test, y_train, y_test: Pandas DataFrames/Series
    """
    # 1. input data (features)
    X_train = load_csv_data("data/X_train_transformed2nd.csv", ignore_index_column=False)
    X_test = load_csv_data("data/X_test_transformed2nd.csv", ignore_index_column=False)
    # 2. target feature (labels)
    y_train = load_csv_data("data/y_train.csv", ignore_index_column=True).squeeze()
    y_test = load_csv_data("data/y_test.csv", ignore_index_column=True).squeeze()
    # 3. Indices consolidation
    X_train = X_train.reset_index(drop=True)
    X_test = X_test.reset_index(drop=True)
    y_train = y_train.reset_index(drop=True)
    y_test = y_test.reset_index(drop=True)
    
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
