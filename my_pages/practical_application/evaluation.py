import streamlit as st
import io
from utils.image_loader import show_github_image
import pandas as pd
import numpy as np
from utils.my_colormaps import my_cmap_r
from utils.model_pipeline import train_and_predict
from utils.compare_models import compare_models_by_threshold_strategy


def show():
    st.header("evaluation with flexible CSV-Loading")

    # Mapping der Strategien für die Selectbox
    strategy_options = {
        "Introduction into CRISP-DM Evaluation Phase": None,
        "Threshold Tuning with Standard Configuration": "default",
        "Cost-Optimized Thresholding": "cost",
        "Trade-Off Optimization using Youden Index": "youden",
        "Threshold Optimization via F1-Score Maximization": "f1",
        "Minimization of the Precision–Recall Gap": "pr_gap",
        "Summary of Evaluation Phase": "summary"
    }

    # Auswahlbox
    strategy_label = st.selectbox("Choose evaluation strategy:", list(strategy_options.keys()))
    strategy = strategy_options[strategy_label]
    
    # 1. Einführung
    if strategy is None:
        st.markdown("""
        ## Introduction
    
        The evaluation phase in the CRISP-DM process helps identify the most effective model by comparing performance metrics 
        across different strategies for threshold optimization.
    
        Strategies include:
        - **Default Threshold (0.5)**
        - **Cost Minimization**
        - **Youden Index (Trade-off TPR/FPR)**
        - **F1 Score Maximization**
        - **Precision–Recall Gap Minimization**
    
        This step ensures that the selected model is aligned with business goals like minimizing false positives or operational cost.
        """)
    
    # 2. Summary View (optional)
    elif strategy == "summary":
        st.markdown("""
        ## Summary of Evaluation Phase
    
        This summary aggregates all threshold optimization strategies, allowing model stakeholders to:
        - Visually compare metric-based trade-offs
        - Justify model decisions with interpretable thresholds
        - Select the most robust strategy for deployment
        """)
        st.info("Implement this section by aggregating all strategies into a combined view if needed.")
        
    # 3. Strategien mit Threshold-Anpassung
    else:
        # Daten & Modelle laden (einmal, mit Caching)
        #@st.cache_resource
        def get_predictions():
            _, logreg_probs, y_test = train_and_predict(model_type="logistic")
            _, xgb_probs, _ = train_and_predict(model_type="xgboost")
            return logreg_probs, xgb_probs, y_test
    
        logreg_probs, xgb_probs, y_test = get_predictions()
    
        # Threshold-optimierte Evaluation
        metrics_logreg, metrics_xgb = compare_models_by_threshold_strategy(
            y_test, logreg_probs, xgb_probs, strategy=strategy
        )
    
        # Ergebnisse als Tabelle anzeigen
        st.subheader(f"Performance Metrics ({strategy_label})")
        df_results = pd.DataFrame([metrics_logreg, metrics_xgb],
                                  index=["Logistic Regression", "XGBoost"]).T
    
        # ✅-Spalte zur Markierung des besseren Werts
        def mark_better(row):
            try:
                if isinstance(row.iloc[0], (float, int)) and isinstance(row.iloc[1], (float, int)):
                    if "Rate" in row.name or "Cost" in row.name:
                        return "✅" if row.iloc[1] < row.iloc[0] else ""
                    else:
                        return "✅" if row.iloc[1] > row.iloc[0] else ""
                return ""
            except:
                return ""
    
        df_results["✅"] = df_results.apply(mark_better, axis=1)
        st.dataframe(df_results.style.format(precision=3))
