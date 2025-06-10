import streamlit as st
import io
from utils.image_loader import show_github_image
from utils.data_loader import load_csv_data
import pandas as pd
import numpy as np
from utils.preprap_feature_engineering import build_pipeline
import graphviz
from sklearn import set_config
from utils.summary_stats import summary
from utils.my_colormaps import my_cmap_r

def show():
    st.header("evaluation with flexible CSV-Loading")

    st.markdown("""
    ### Data preprocessing according to the key results of data understanding phases
    
    During this phase of the CRISP-DM process, the initial data preprocessing is carried out based on the one hand on 
    instructions from the primary researchers. On the other hand, results from the data audit will be taken into account.
    The goal is to clean and transform the data into a suitable format for later modeling.
    
    ### Initial Situation
    The dataset used originates from a secondary source and includes special codings that need to be standardized. For 
    example the target variable (y = Term deposit subscription) is binary, so the values (yes/no) must be transformed to (1/0).
    
    The following data transformations were implemented:
    - **Replace 'unknown' with 'NaN' in all categorical features**  
      *Rationale:* The value 'unknown' indicates missing information and is therefore encoded as 'NaN' to allow for proper handling (e.g., imputation or removal).
    
    - **Combine `unknown` and `yes` values in the `default` feature into a single category `unknown|yes`**  
      *Rationale:* Both values suggest potential credit risk and should be treated as one category.
    
    - **Transform the target variable `y`:**  
      Original values: `'no'`, `'yes'`  
      New encoding: `0` (no subscription), `1` (subscription)  
      *Rationale:* Required for binary classification in a supervised learning context.
      
    - **Transform the `pdays` variable (days since last contact):**  
      Value `999` → `0`  
      *Rationale:* A value of 999 indicates no previous contact and is re-coded to 0 for meaningful numeric interpretation.

    Below you find top 5 recordsets of the initial dataframe.
    """, unsafe_allow_html=True)

    # Beispiel: Bank-Daten laden
    df = load_csv_data(
        filename="data/bank-additional-full.csv",
        sep=";",
        header=True,
        add_row_id=True
    )

#    st.success("Datei erfolgreich geladen.")
    st.dataframe(df.head())    
    st.markdown("""
    ### Additional Preprocessing Pipeline: Duplicate Removal and Column Exclusion (CRISP-DM: Data Preparation)
    
    In the data preparation phase, further steps were taken to ensure model reliability and adherence to methodological 
    guidelines from the primary researchers.
       
    This additional preprocessing pipeline includes two critical actions:    
    1. **Remove duplicate rows**
       - *Rationale:* Ensures data quality by eliminating redundant observations that may bias the model or inflate its 
       performance.
        <br> <br>
    
    2. **Drop the feature `duration`**
       - *Rationale:* Based on explicit instructions from the primary researchers, the variable `duration` must be excluded because it is not available before the marketing campaign takes place.
       - Including it would introduce *data leakage*, as `duration` is only known **after** a call ends and is strongly correlated with the target variable.
    
    ---
    
    ### Summary of the Additional Preprocessing Steps
    
    | Step | Feature       | Transformation              | Rationale                                                        |
    |------|---------------|-----------------------------|------------------------------------------------------------------|
    | 1    | Entire dataset| Removal of duplicates       | Avoids bias and inflated performance due to redundant entries    |
    | 2    | `duration`    | Dropped from the dataset    | Prevents data leakage, not known at time of prediction           |
    
    ---
    
    > *Note:* These steps are applied before model training and are considered essential to ensure the model generalizes well to unseen data.
    """, unsafe_allow_html=True)
    
    # SQL-artige Gruppierung ersetzen durch pandas
    grouped = df.groupby(["month", "cons.price.idx"]).agg(
        COUNT_TOTAL_PER_MONTH=('month', 'count'),
        MAX_RN_month=('ROW_ID', 'max')
    ).reset_index()

    def assign_year(row):
        if row['MAX_RN_month'] <= 27690:
            return 2008
        elif row['MAX_RN_month'] <= 39130:
            return 2009
        else:
            return 2010

    grouped['year'] = grouped.apply(assign_year, axis=1)
    df = pd.merge(df, grouped[['month', 'cons.price.idx', 'year']], on=['month', 'cons.price.idx'], how='left')
    df['date_period'] = pd.to_datetime(df['year'].astype(str) + "-" + pd.to_datetime(df['month'], format='%b').dt.month.astype(str)).dt.to_period('M')
    df['date_int'] = df['date_period'].dt.strftime('%Y%m').astype(int)
    df['date_period'] = df['date_period'].astype(str)

    st.success("Datei erfolgreich angereichert.")
    st.dataframe(df.head())

    preprocessor = build_pipeline(df)
    preprocessor.set_output(transform='pandas')
    transformed_df = preprocessor.fit_transform(df)

    sum_df = summary(transformed_df)
    
    styled_summary = sum_df.style.background_gradient(
        cmap=my_cmap_r,
        subset=['rate_missing_values']
    )

    st.subheader("Daten nach Transformation:")
    st.subheader("Datenzusammenfassung")
    st.dataframe(styled_summary)
    #st.dataframe(summary(df).reset_index().rename(columns={"index": "Spalte"}))
