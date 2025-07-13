import streamlit as st
import pandas as pd
import numpy as np

import io
from utils.image_loader import show_github_image
from utils.my_colormaps import my_cmap_r, cmap_4
from utils.model_pipeline import * #train_and_predict
from utils.compare_models import compare_models_by_threshold_strategy
from utils.plot_helpers import plot_confusion_matrices
from utils.plot_era_roc_curve import plot_roc_curves_with_early_area
from utils.plot_precision_recall_f1_threshold import plot_precision_recall_with_f1_thresholds
from utils.plot_precision_recall_gap import plot_precision_recall_gap
from utils.plot_youden import plot_roc_with_youden
from utils.feature_importance_helpers import (
    get_preprocessed_training_data,
    get_fitted_xgboost_model,
    plot_logistic_feature_importance,
    plot_xgboost_feature_importance
)
from utils.plot_opex_optimization import plot_opex_optimization

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    # Mapping for strategy within selectbox
    strategy_options = {
        "Introduction into CRISP-DM Evaluation Phase": None,
        "Threshold Tuning with Standard Configuration": "default",
        "Cost-Optimized Thresholding": "cost",
        "Trade-Off Optimization using Youden Index": "youden",
        "Threshold Optimization via F1-Score Maximization": "f1",
        "Minimization of the Precision–Recall Gap": "pr_gap",
        "Feature Importance Exploration": "feature_importance",  # 
        "Summary of Evaluation Phase": "summary"
    }

    # Auswahlbox
    strategy_label = st.selectbox("Choose evaluation strategy:", list(strategy_options.keys()))
    strategy = strategy_options[strategy_label]
    # Daten & Modelle laden (einmal, mit Caching)
    @st.cache_resource
    def get_predictions():
        _, logreg_probs, y_test = train_and_predict(model_type="logistic")
        _, xgb_probs, _ = train_and_predict(model_type="xgboost")
        return logreg_probs, xgb_probs, y_test

    @st.cache_resource
    def get_model_fit():
        logreg_model, X_train, X_test, y_train, y_test = train_model(model_type="logistic")
        xgb_model, _, _, _, _ = train_model(model_type="xgboost")
        return logreg_model, xgb_model, X_train, y_train

    def render_html_table_metrics(df: pd.DataFrame) -> str:
        html = """
        <style>
            .scrollable-table-container {
                height: 400px;
                overflow-y: auto;
                border: 1px solid #ccc;
                padding: 10px;
            }
    
            table {
                width: 100% !important;
                border-collapse: collapse !important;
                table-layout: fixed !important;
                border: 2px solid black !important;
            }
            th {
                position: sticky;
                top: 0;
                background-color: #097a80 !important;
                color: white !important;
                border: 1px solid lightgray !important;
                text-align: left !important;
                padding: 8px !important;
                word-break: break-word !important;
                max-width: 250px !important;
                font-size: 14px !important;
            }
            td {
                background-color: white !important;
                color: black !important;
                border: 1px solid black !important;
                text-align: left !important;
                padding: 8px !important;
                word-break: break-word !important;
                max-width: 250px !important;
                font-size: 14px !important;
            }
        </style>
        <div class="scrollable-table-container">
        <table>
            <thead>
                <tr>
        """
    
        for col in df.columns:
            html += f"<th>{col}</th>"
        html += "</tr></thead><tbody>"
    
        for _, row in df.iterrows():
            html += "<tr>"
            for col in df.columns:
                cell = row[col]
                html += f"<td>{str(cell)}</td>"
            html += "</tr>"
    
        html += "</tbody></table></div>"
        return html
        
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
        # ROC-Curve Plot
        st.markdown("---")
        st.subheader("Model Comparison using ROC-Curves with Early Retrieval Area")
        logreg_probs, xgb_probs, y_test = get_predictions()
        fig_intro_roc = plot_roc_curves_with_early_area(y_test, logreg_probs, xgb_probs)        
        st.pyplot(fig_intro_roc)

        
    elif strategy == "feature_importance":
        st.markdown("## Feature Importance Exploration")
        st.write("""
        This view compares the most significant features between **Logistic Regression** and **XGBoost**.

        **Logistic Regression**
        - Odds Ratios from `statsmodels`
        - Statistically significant features only (p < 0.05)

        **XGBoost**
        - Gain-based feature importances
        """)

        # Daten & Modelle laden
        logreg_model, xgb_model, X_train, y_train = get_model_fit()
        #X_train, y_train = get_preprocessed_training_data()
        #xgb_model = get_fitted_xgboost_model()
        st.write(X_train.dtypes)
        st.write("X_train types:", X_train.dtypes)
        st.write("y_train unique values:", y_train.unique())
        # Logistic Regression: Feature Importance
        st.markdown("### Logistic Regression Feature Importance")
        try:
            fig_logreg = plot_logistic_feature_importance(logreg_model, X_train, y_train ,9)
            st.pyplot(fig_logreg)
        except Exception as e:
            st.error(f"Error plotting logistic regression importance: {e}")

        # XGBoost: Feature Importance
        st.markdown("### XGBoost Feature Importance")
        try:
            fig_xgb = plot_xgboost_feature_importance(xgb_model, X_train,9)
            st.pyplot(fig_xgb)
        except Exception as e:
            st.error(f"Error plotting XGBoost importance: {e}")
        
   
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
        logreg_probs, xgb_probs, y_test = get_predictions()
    
        # Threshold-optimierte Evaluation
        metrics_logreg, metrics_xgb = compare_models_by_threshold_strategy(
            y_test, logreg_probs, xgb_probs, strategy=strategy
        )
        # Nur für F1-Strategie: Precision–Recall-Kurve mit Threshold-Markierung anzeigen
        if strategy == "f1":
            st.markdown("---")
            st.subheader("Precision–Recall Curve with F1-Optimized Thresholds")
            fig_f1 = plot_precision_recall_with_f1_thresholds(y_test, logreg_probs, xgb_probs)
            st.pyplot(fig_f1)
        # Nur bei Precision–Recall-Gap-Minimierung: Visualisierung des Schwellenwertverlaufs
        if strategy == "pr_gap":
            st.markdown("---")
            st.subheader("Threshold Optimization via Precision–Recall Gap Minimization")
            fig_pr_gap = plot_precision_recall_gap(y_test, logreg_probs, xgb_probs)
            st.pyplot(fig_pr_gap)    
        if strategy == "youden":
            st.markdown("---")
            st.subheader("ROC Curve with Youden’s J Optimization")
            fig_youden = plot_roc_with_youden(y_test, logreg_probs, xgb_probs)
            st.pyplot(fig_youden)
        if strategy == "cost":
            st.markdown("---")
            st.subheader("Threshold Optimization via OPEX Optimization")
            fig_opex_opti = plot_opex_optimization(y_test, logreg_probs, xgb_probs, language="en")
            st.pyplot(fig_opex_opti)
        # Ergebnisse als Tabelle anzeigen
        st.subheader(f"Performance Metrics ({strategy_label})")
        df_results = pd.DataFrame([metrics_logreg, metrics_xgb],
                                  index=["Logistic Regression", "XGBoost"]).T
    
        # ✅-Spalte zur Markierung des besseren Werts
        #def mark_better(row):
        #    try:
        #        if isinstance(row.iloc[0], (float, int)) and isinstance(row.iloc[1], (float, int)):
        #            if "Rate" in row.name or "Cost" in row.name:
        #                return "✅" if row.iloc[1] < row.iloc[0] else ""
        #            else:
        #                return "✅" if row.iloc[1] > row.iloc[0] else ""
        #        return ""
        #    except:
        #        return ""
        def mark_best(df):
            df_marked = df.copy()
            for idx in df.index:
                val1 = df.loc[idx, "Logistic Regression"]
                val2 = df.loc[idx, "XGBoost"]
                if isinstance(val1, (float, int)) and isinstance(val2, (float, int)):
                    # Wenn kleiner besser (Cost, Error Rate etc.)
                    if "Rate" in idx or "Cost" in idx:
                        if val1 < val2:
                            df_marked.loc[idx, "Logistic Regression"] = f"{val1:.3f} ✅"
                            df_marked.loc[idx, "XGBoost"] = f"{val2:.3f}"
                        else:
                            df_marked.loc[idx, "Logistic Regression"] = f"{val1:.3f}"
                            df_marked.loc[idx, "XGBoost"] = f"{val2:.3f} ✅"
                    else:  # Wenn größer besser (Accuracy, F1 etc.)
                        if val1 > val2:
                            df_marked.loc[idx, "Logistic Regression"] = f"{val1:.3f} ✅"
                            df_marked.loc[idx, "XGBoost"] = f"{val2:.3f}"
                        else:
                            df_marked.loc[idx, "Logistic Regression"] = f"{val1:.3f}"
                            df_marked.loc[idx, "XGBoost"] = f"{val2:.3f} ✅"
                else:
                    # Falls kein numerischer Vergleich möglich
                    df_marked.loc[idx, "Logistic Regression"] = str(val1)
                    df_marked.loc[idx, "XGBoost"] = str(val2)
            return df_marked
            
        df_results_marked = mark_best(df_results)    
        #df_results["✓"] = df_results.apply(mark_better, axis=1)    
        #st.dataframe(df_results.style.format(precision=3))

        
        # 3. Index (Metriken) als Spalte übernehmen
        df_results_marked.reset_index(inplace=True)
        df_results_marked.rename(columns={"index": "Metric"}, inplace=True)
        
        # 4. Optional: Formatierung
        #df_results = df_results.round(3)
        
        # 5. HTML-Rendering der neuen Tabelle
        html_table_metrics = render_html_table_metrics(df_results_marked)
        
        # 6. Anzeige in Streamlit
        st.subheader("Performance Metrics (with ✅ for better model)")
        st.markdown(html_table_metrics, unsafe_allow_html=True)

       # Konfusionsmatrizen visualisieren
        st.markdown("---")
        st.subheader("Confusion Matrices")

        # Vorhersagen anhand des gewählten Thresholds
        logreg_pred = (logreg_probs >= metrics_logreg['Threshold']).astype(int)
        xgb_pred = (xgb_probs >= metrics_xgb['Threshold']).astype(int)

        # Logistic Regression – Confusion Matrix
        st.markdown("### Logistic Regression")
        fig_logreg = plot_confusion_matrices(
            y_test, logreg_pred,
            model_name="Logistic Regression",
            strategy=strategy_label,
            cmap=cmap_4
        )
        st.pyplot(fig_logreg)

        # XGBoost – Confusion Matrix
        st.markdown("### XGBoost")
        fig_xgb = plot_confusion_matrices(
            y_test, xgb_pred,
            model_name="XGBoost",
            strategy=strategy_label,
            cmap=cmap_4
        )
        st.pyplot(fig_xgb)
    st.markdown("""
        <!-- Font Awesome einbinden -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

        <style>
        #scroll-top-link {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 100;
    
            width: 60px;
            height: 60px;
            border: none;
            border-radius: 50%;
            cursor: pointer;
    
            display: flex;
            align-items: center;
            justify-content: center;
    
            background-color: black;
            color: white;
            text-decoration: none;
            font-size: 24px;
            transition: background-color 0.3s ease, opacity 0.2s ease;
        }
    
        @media (prefers-color-scheme: dark) {
            #scroll-top-link {
                background-color: #222;
                color: white;
            }
        }
    
        @media (prefers-color-scheme: light) {
            #scroll-top-link {
                background-color: #e0e0e0;
                color: black;
            }
        }
    
        /* Optional: Hover-Effekt */
        #scroll-top-link:hover {
            opacity: 0.85;
        }
        </style>
    
        <!-- Button mit Icon -->
        <a href="#top" id="scroll-top-link" title="Top">
            <i class="fas fa-arrow-up"></i>
        </a>
    """, unsafe_allow_html=True)
