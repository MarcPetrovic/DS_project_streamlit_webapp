import streamlit as st
from utils.image_loader import show_github_image
from utils.data_loader import load_csv_data
import pandas as pd
import numpy as np
from utils.preprap_feature_engineering import build_pipeline
import graphviz
from sklearn import set_config

def show():
    st.header("evaluation with flexible CSV-Loading")

    # Beispiel: Bank-Daten laden
    df = load_csv_data(
        filename="data/bank-additional-full.csv",
        sep=";",
        header=True,
        add_row_id=True
    )

    st.success("Datei erfolgreich geladen.")
    st.dataframe(df.head())
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
#    preprocessor.set_output(transform='pandas')
    transformed_df = preprocessor.fit_transform(df)

    st.subheader("Daten nach Transformation:")
    st.dataframe(transformed_df.head())
