import streamlit as st
from utils.plot_helpers import plot_confusion_matrices
from utils.table_helpers import render_html_table_metrics, mark_best
import matplotlib.pyplot as plt

def display_strategy_results(
    strategy_label: str,
    markdown_intro: str,
    plot_figure,
    y_test,
    logreg_probs,
    xgb_probs,
    metrics_logreg,
    metrics_xgb,
    cmap,
    markdown_metrics_text: str = None
):
    # 1. Einleitung
    st.markdown(markdown_intro)

    # 2. Visualisierung
    st.subheader(f"Threshold Optimization via {strategy_label}")
    st.pyplot(plot_figure)

    # 3. Confusion Matrices
    st.subheader("Confusion Matrices")
    logreg_pred = (logreg_probs >= metrics_logreg['Threshold']).astype(int)
    xgb_pred = (xgb_probs >= metrics_xgb['Threshold']).astype(int)

    st.markdown("### Logistic Regression")
    fig_logreg = plot_confusion_matrices(y_test, logreg_pred, model_name="Logistic Regression", strategy=strategy_label, cmap=cmap)
    st.pyplot(fig_logreg)

    st.markdown("### XGBoost")
    fig_xgb = plot_confusion_matrices(y_test, xgb_pred, model_name="XGBoost", strategy=strategy_label, cmap=cmap)
    st.pyplot(fig_xgb)

    # 4. Optionaler Markdown zur Tabelle
    if markdown_metrics_text:
        st.markdown(markdown_metrics_text)

    # 5. Performance-Tabelle
    st.subheader("Performance Metrics (with ✅ for better model)")

    df_results = pd.DataFrame([metrics_logreg, metrics_xgb], index=["Logistic Regression", "XGBoost"]).T
    df_results_marked = mark_best(df_results)
    df_results_marked.reset_index(inplace=True)
    df_results_marked.rename(columns={"index": "Metric"}, inplace=True)
    html_table = render_html_table_metrics(df_results_marked)
    st.markdown(html_table, unsafe_allow_html=True)
