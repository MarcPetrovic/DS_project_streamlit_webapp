import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data_loader import load_csv_data
from utils.my_colormaps import my_cmap_r, cmap_4, my_cmap

def show():
    st.header("Conclusion & Discussion")
    #st.write("Hier formulierst du deine Schlussfolgerungen und Diskussion.")
    st.markdown("""
    Im Rahmen dieses Projektes wurde die Klassifikation für den Abschluss eines Festgeldvertrages optimiert.  
    Ein Aspekt, der **nicht Bestandteil** war, ist die Kalibrierung der Score-Bänder basierend auf den Trefferwahrscheinlichkeiten der Modelle.
    """)
    df = load_csv_data(
        filename="data/bank-additional-full.csv",
        sep=";",
        header=True,
        add_row_id=True,
        ignore_index_column=False
    )
    
    # Jahr zuordnen anhand von ROW_ID
    df_view = (
        df.groupby(["month", "cons.price.idx"], as_index=False)
        .agg(COUNT_TOTAL_PER_MONTH=("month", "count"), MAX_RN_month=("ROW_ID", "max"))
    )
    df_view["year"] = df_view["MAX_RN_month"].apply(
        lambda x: 2008 if x <= 27690 else (2009 if x <= 39130 else 2010)
    )
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
    df["date_int"] = df["date_period"].dt.strftime('%Y%m').astype(int)
    df["date_period"] = df["date_period"].astype(str)

    # 👉 AGGREGATION FÜR ZEITREIHENPLOT
    df["target"] = df["y"].apply(lambda x: 0 if x == "no" else 1)
    df["BASIS"] = 1

    df_plot_view = (
        df.groupby("date_period")
          .agg(Target=("target", "sum"), Basis=("BASIS", "sum"))
          .reset_index()
    )
    df_plot_view["Success_Ratio"] = df_plot_view["Target"] / df_plot_view["Basis"]
    df_plot_view.sort_values("date_period", inplace=True)

    # Titel und Beschreibung
    st.subheader("Subscription Success Rate Over Time")
    st.markdown("This time series shows the monthly success rate of term deposit subscriptions based on the bank’s marketing campaigns.")
    
    # Prozentuale Darstellung
    df_plot_view["Success_Ratio"] = df_plot_view["Success_Ratio"] * 100
    
    # Plot erzeugen
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(data=df_plot_view, x="date_period", y="Success_Ratio", color="tab:red", marker="o", ax=ax)
    
    ax.set_title("Monthly Success Rate of Fixed-Term Deposit Campaigns", fontsize=14)
    ax.set_xlabel("Date (Month)")
    ax.set_ylabel("Success Rate (%)")
    ax.grid(True, linestyle="--", alpha=0.6, color="gray")
    ax.set_facecolor("lightgrey")
    plt.xticks(rotation=45)
    
    st.pyplot(fig)
    
    # Interpretation als Text (optional)
    st.markdown("""
    🧠 **Interpretation**  
    This plot reveals how the subscription success rate evolved over time.  
    Strong fluctuations may indicate behavioral drift or external market influences—suggesting the need for out-of-time validation before model deployment.
    """)
