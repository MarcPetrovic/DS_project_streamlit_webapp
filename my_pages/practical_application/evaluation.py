import streamlit as st
from utils.image_loader import show_github_image
from utils.data_loader import load_csv_data

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
