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
    
 # Deine Farbvorgaben
    line_color = "#C00000"      # für Success Ratio
    bar_color = "#097a80"       # für Kontaktanzahl
    bg_color = "white"
    plot_area_color = "lightgrey"
    label_color = "black"
    
    # 🎯 Sicherstellen, dass Success Ratio in Prozent ist
    df_plot_view["Success_Ratio"] = df_plot_view["Success_Ratio"] * 100
    
   # 📊 Plot erzeugen
    fig, ax1 = plt.subplots(figsize=(14, 5))
    ax1.set_facecolor(area_color)
    fig.patch.set_facecolor(bg_color)

    # 🟦 Säulen auf linker Y-Achse
    bars = ax1.bar(
        df_plot_view["date_period"],
        df_plot_view["Basis"],
        color=bar_color,
        label="Total Contacts",
        alpha=0.85,
        zorder=1
    )
    ax1.set_ylabel("Total Contacts", color=label_color)
    ax1.tick_params(axis='y', labelcolor=label_color)
    ax1.set_xlabel("Date (Month)", color=label_color)
    ax1.tick_params(axis='x', rotation=45, labelcolor=label_color)

    # 🔴 Linie auf rechter Y-Achse
    ax2 = ax1.twinx()
    line = ax2.plot(
        df_plot_view["date_period"],
        df_plot_view["Success_Ratio"],
        color=line_color,
        marker='o',
        linestyle='--',
        linewidth=2.2,
        label="Success Ratio (%)",
        zorder=2  # Linie vor die Säulen
    )
    ax2.set_ylabel("Success Ratio (%)", color=label_color)
    ax2.tick_params(axis='y', labelcolor=label_color)
    ax2.set_ylim([0, 100])

    # 🗂️ Legende manuell zusammenführen
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc="center right")

    # 🧾 Titel & Layout
    plt.title("Success Ratio and Contact Volume Over Time", fontsize=14, fontweight='bold', color=label_color)
    ax1.grid(True, linestyle='--', color='grey', alpha=0.6)
    plt.tight_layout()    
    # 📌 Streamlit-Ausgabe
    st.pyplot(fig)
    
    # ℹ️ Interpretation
    st.markdown("""
    🧠 **Interpretation**  
    The red line illustrates the success rate of term deposit subscriptions, while the blue bars represent total campaign contacts.  
    The mid-right legend and overlaid line ensure readability while tracking both scale and performance over time.
    """)
