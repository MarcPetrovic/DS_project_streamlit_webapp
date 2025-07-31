import streamlit as st
from utils.plot_helpers import plot_confusion_matrices
from utils.table_helpers import render_html_table_metrics, mark_best
import matplotlib.pyplot as plt

def display_strategy_results(
    strategy_label: str,
    markdown_intro: str,
    plot_figure,
    markdown_after_plot: str,
    y_test,
    logreg_probs,
    xgb_probs,
    metrics_logreg,
    metrics_xgb,
    cmap,
    markdown_metrics_text: str,
    markdown_between_confusion_and_metrics: str = "",
    markdown_after_table: str = ""
):
    # 1. Markdown-Intro
    st.markdown(markdown_intro)

    # 2. Strategietypische Visualisierung (falls vorhanden)
    if plot_figure is not None:
        st.pyplot(plot_figure)

    # 3. Nachfolgender Text zur Interpretation der Visualisierung
    if markdown_after_plot:
        st.markdown(markdown_after_plot)

    # 4. Confusion Matrices
    st.markdown("---")
    st.subheader("Confusion Matrices")

    # Threshold-Anwendung
    logreg_pred = (logreg_probs >= metrics_logreg["Threshold"]).astype(int)
    xgb_pred = (xgb_probs >= metrics_xgb["Threshold"]).astype(int)

    st.markdown("### Logistic Regression")
    fig_logreg = plot_confusion_matrices(y_test, logreg_pred, model_name="Logistic Regression", strategy=strategy_label, cmap=cmap)
    st.pyplot(fig_logreg)

    st.markdown("### XGBoost")
    fig_xgb = plot_confusion_matrices(y_test, xgb_pred, model_name="XGBoost", strategy=strategy_label, cmap=cmap)
    st.pyplot(fig_xgb)

    # 4.1 Optionaler Text zwischen Confusion Matrices und Performance Metrics
    if markdown_between_confusion_and_metrics:
        st.markdown(markdown_between_confusion_and_metrics)

    # 5. Überleitung zu den Metriken
    st.markdown("---")
    st.markdown(markdown_metrics_text)

    # 6. Vergleichstabelle rendern
    df_results = {
        "Logistic Regression": metrics_logreg,
        "XGBoost": metrics_xgb
    }
    import pandas as pd
    df_results = pd.DataFrame(df_results)
    df_results_marked = mark_best(df_results)
    df_results_marked.reset_index(inplace=True)
    df_results_marked.rename(columns={"index": "Metric"}, inplace=True)

    html_table = render_html_table_metrics(df_results_marked)
    st.markdown(html_table, unsafe_allow_html=True)
    st.markdown("   ")

    # 7. Optionaler Text nach der Tabelle
    if markdown_after_table:
        st.markdown(markdown_after_table)
