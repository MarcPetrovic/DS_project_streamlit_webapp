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
from utils.plot_ks_curve import plot_ks_curve
import matplotlib.pyplot as plt
from utils.plot_lift_curve import plot_lift_curve_with_ci
from utils.decile_analysis import *

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    # Mapping for strategy within selectbox
    strategy_options = {
        "Introduction into CRISP-DM Evaluation Phase": None,
        "Overall Model Evaluation": "overall",
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
        ## Introduction into CRISP-DM Evaluation Phase
    
        In the context of this data mining project, the evaluation phase within the CRISP-DM framework represents the final step toward 
        achieving the central goal of the practical use case: the development of a robust and high-performing response model for cost-optimized 
        segmentation of an existing customer portfolio. Based on a statistically validated prediction model, future phone-based marketing 
        campaigns should target only those customer segments whose likelihood of signing a fixed-term deposit contract at least offsets the 
        associated campaign costs.
    
        The two previously selected classification algorithms—Logistic Regression and XGBoost—are now compared objectively based on both 
        statistical metrics and business-related performance indicators. The initial focus lies on evaluating overall model quality, especially 
        the ability of each model to differentiate effectively between positive and negative cases. In line with common challenges in the 
        financial sector, the dataset used in this project is highly imbalanced, with only 11.4% of the test cases belonging to the positive 
        class. Therefore, particular emphasis is placed on the Early Retrieval Area as an evaluation criterion, specifically by analyzing model 
        performance at a False Positive Rate (FPR) ≤ 20%. This business-relevant threshold helps determine whether a model can capture a 
        significant portion of high-value targets early—ideally achieving a True Positive Rate (TPR) ≥ 70%, while maintaining cost efficiency. 
        Additionally, AUC-ROC is used as a standard metric to evaluate the overall discriminative power of the models across all thresholds.

        Beyond AUC, several advanced metrics are applied to obtain a more nuanced assessment of model performance under class imbalance. These 
        include the Gini coefficient, which provides a normalized measure of class separation; the Brier Score, which quantifies the accuracy 
        of predicted probabilities; and the Kolmogorov–Smirnov (KS) statistic, which identifies the maximum separation between cumulative 
        distributions of positives and negatives. The Precision–Recall AUC (PR-AUC) offers an alternative view on classification performance, 
        especially relevant in imbalanced contexts. Furthermore, a Lift Curve analysis illustrates how well each model improves targeting over 
        random selection, while a Decile Analysis breaks down predictive power across score segments to assess model calibration and ranking 
        quality. Together, these metrics and visual tools provide a comprehensive view of each model’s discriminative strength and practical 
        utility in a cost-sensitive business environment.

        Each model is evaluated under different threshold-tuning strategies, using the following performance metrics:
        - False Positive Rate (FPR) – Minimizing operational costs
        - False Negative Rate (FNR) – Minimizing lost revenue opportunities
        - Precision – Maximizing the accuracy of positive predictions (focus on false positives)
        - Recall (True Positive Rate) – Maximizing potential revenue gains
        - Specificity (True Negative Rate) – Reducing unnecessary customer contacts (cost control)
        - F1-Score – Harmonic mean of Precision and Recall
        - Accuracy – Overall classification performance (used with caution in imbalanced datasets)        
        - Cohen’s Kappa – Agreement between predicted and actual classes adjusted for chance (≥ 0.35 indicates acceptable to moderate agreement)
        - Matthews Correlation Coefficient (MCC) – Measures correlation between predicted and observed classifications (≥ 0.35 considered meaningful)
        - Total Cost (€) – Minimizing total cost by considering both operational expenditures and opportunity losses

        The threshold-tuning strategies applied include:
        - Default Threshold (0.5)
        - Cost Minimization
        - Youden Index (balancing TPR and FPR)
        - F1-Score Maximization
        - Precision–Recall Gap Minimization

        In the following subsections, the models will be compared under each threshold-tuning approach using tables that present the respective 
        performance metrics side by side. This serves to facilitate a clear and structured interpretation and improve readability. Visual aids 
        such as color-coded confusion matrices with both absolute and relative values, and—depending on the tuning strategy—graphical 
        representations of threshold curves, will be provided. This presentation is intended to help the reader follow and understand the 
        evaluation results in a transparent and practice-oriented manner.

        To enhance the interpretability of the models and provide actionable insights, a feature importance analysis is also conducted for both 
        classification algorithms. For Logistic Regression, only the most statistically significant features are considered, based on odds 
        ratios derived from the statsmodels package. Specifically, only variables with a p-value below 0.05 are included to ensure statistical 
        relevance. For XGBoost, gain-based feature importances are utilized, which measure each feature’s relative contribution to reducing loss 
        across all boosting iterations. In each case, the top nine predictors with the greatest influence on the target variable are visualized. 
        This comparative perspective offers valuable information about the differ-rent ways the two models interpret and prioritize customer 
        characteristics, thereby supporting domain experts in understanding the driving factors behind positive responses and enabling more 
        targeted campaign strategies

        """)
        
    elif strategy == "overall":
        st.markdown("""
        ## Overall Evaluation of discriminative Performance under class imbalance

        In the evaluation phase, model performance was assessed using both global discrimination metrics and business-critical indicators. The 
        Area Under the ROC Curve (AUC) values of 0.790 for Logistic Regression and 0.799 for XGBoost reflect good overall separability between 
        the two target classes, even in the presence of class imbalance (11.5% positive class). More importantly, the Early Retrieval Area—focusing 
        on cases with a False Positive Rate (FPR) of 20% or lower—yielded True Positive Rates (TPR) of 0.674 and 0.685, respectively. This confirms 
        the models’ ability to identify a large proportion of valuable customers while keeping outreach costs under control.
        
        """)

        # ROC-Curve Plot
        st.markdown("---")
        st.subheader("Model Comparison using ROC-Curves with Early Retrieval Area")
        logreg_probs, xgb_probs, y_test = get_predictions()
        fig_intro_roc = plot_roc_curves_with_early_area(y_test, logreg_probs, xgb_probs)        
        st.pyplot(fig_intro_roc)
        st.markdown("---")
        st.markdown("""

        In addition to the previously presented performance metrics, several statistical measures were employed to provide a more comprehensive 
        assessment of model quality.

        The Gini coefficient is closely related to the area under the ROC curve (AUC) and is calculated as:
        """)
        st.latex(r"\text{Gini} = 2 \times \text{AUC} - 1")
        st.markdown("""
        It quantifies a model’s discriminatory power; a value of 0 corresponds to random performance, while 1 indicates perfect separation. 
        """)
        st.markdown(
            "The Brier score measures the mean squared difference between predicted probabilities "
            r"$\hat{p}_i$ and actual outcomes $\gamma_i$ (0/false or 1/true):"
        )
        st.latex(r"""
        \text{Brier Score} = \frac{1}{N} \sum_{i=1}^{N} (\hat{p}_i - \gamma_i)^2
        """)
        st.markdown("""
        Lower values indicate better calibration and accuracy of probability predictions.

        The Kolmogorov-Smirnov (KS) statistic quantifies the maximum distance between the empirical cumulative distribution functions (ECDFs) 
        of the predicted scores for the positive and negative classes: 
        """)
        st.latex(r"""
        \text{Kolmogorov–Smirnov} = \max_x \left| F_1(x) - F_0(x) \right|
        """)
        st.markdown("**Where:**")
        st.markdown("- $F_1(x)$ is the cumulative distribution function (CDF) of scores for the **positive class**")
        st.markdown("- $F_0(x)$ is the CDF of scores for the **negative class**")
        st.markdown("- $\\max_x$ denotes the maximum over all thresholds $x \\in \\mathbb{R}$")
        st.markdown("""
        The KS value ranges from 0 to 1, with higher values indicating better class separation between the distributions. The threshold that 
        maximizes the KS statistic can be interpreted as an optimal classification cutoff, meaning that at this value the difference between 
        positive and negative score distributions is maximized, facilitating effective classification.

        The Precision-Recall AUC (PR-AUC) is the area under the Precision-Recall curve. It focuses on balancing precision and recall, which is 
        particularly important in highly imbalanced datasets, as it better reflects the model’s ability to detect rare positive events compared 
        to ROC-AUC. 
        """)

        st.latex(r"""
        \text{Precision} = \frac{TP}{TP + FP} \quad ; \quad
        \text{Recall} = \frac{TP}{TP + FN}
        """)

        st.markdown("**Where:**")
        st.markdown("- **TP**: True Positive")
        st.markdown("- **FP**: False Positive")
        st.markdown("- **FN**: False Negative")
        

        st.markdown("**The PR-AUC is then computed as:**")
        st.latex(r"""
        \text{PR-AUC} = \int_0^1 \text{Precision}(r) \, dr
        """)
        st.markdown("""
        Interpretation of these metrics in the context of imbalanced data:
        - Gini coefficient: Values > 0.5 indicate good discriminatory power; values between 0.3 and 0.5 are moderate, and below 0.3 are weak.
        - Brier score: Values below 0.1 are considered good; the score reflects both calibration and accuracy.
        - KS statistic: Values above 0.4 indicate strong class separation, values between 0.2 and 0.4 are moderate.
        - PR-AUC: Particularly important in imbalanced settings; a PR-AUC > 0.4 signals reliable positive class detection.
        
        """)
        st.subheader("Kolmogorov–Smirnov (KS) Curve – Logistic Regression")
        fig_ks_logreg = plot_ks_curve(y_test, logreg_probs, model_name="Logistic Regression", color='#097a80')
        st.pyplot(fig_ks_logreg)
        
        st.subheader("Kolmogorov–Smirnov (KS) Curve – XGBoost")
        fig_ks_xgb = plot_ks_curve(y_test, xgb_probs, model_name="XGBoost", color='#C00000')
        st.pyplot(fig_ks_xgb)

        st.markdown("""
        For the logistic regression model, the Gini coefficient of 0.5790 indicates solid discriminatory power. The Brier score of 0.0809 confirms 
        good calibration of predicted probabilities. The KS statistic of 0.4804, with an optimal threshold at 0.1128, supports that this cutoff 
        maximizes the separation between classes, enabling effective classification. The PR-AUC of 0.4489 further confirms the model’s ability to 
        reliably identify positive cases despite class imbalance.

        For the XGBoost model, the Gini coefficient of 0.5977 and Brier score of 0.0791 also demonstrate good to very good model quality. The KS 
        statistic of 0.4944 indicates strong class separation, while the PR-AUC of 0.4641 substantiates solid detection of positive cases in the 
        presence of imbalance.

        **Lift-Curve Analysis**

        The Lift Curve illustrates the improvement a model provides over random selection in identifying positive cases within different proportions 
        of the population. For both models, the lift starts high and gradually decreases as more of the population is included, indicating that the 
        models are successful in ranking customers by their likelihood of being positive.

        """)
        st.latex(r"""
        \text{Lift}(\rho) = 
        \frac{\text{Precision at } \rho}{\text{Baseline Positive Rate}} = 
        \frac{TP_{\rho} / n_{\rho}}{P / N}
        """)
        st.markdown("**Where:**")
        st.markdown("- $\\rho$: Proportion of the population considered (e.g., the top 10% based on predicted scores)")
        st.markdown("- $TP_{\\rho}$: Number of true positive cases within the top $\\rho$% of the population")
        st.markdown("- $n_{\\rho}$: Total number of observations within the top $\\rho$ segment")
        st.markdown("- $P$: Total number of positive cases in the entire population")
        st.markdown("- $N$: Total number of observations in the population")
        st.markdown("- $P/N$: Baseline positive rate (i.e., the expected positive rate under random selection)")

        st.subheader("Lift Curve with Confidence Intervals")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_facecolor('lightgrey')        
        plot_lift_curve_with_ci(y_test, logreg_probs, 'Logistic Regression', '#097a80', ax=ax)
        plot_lift_curve_with_ci(y_test, xgb_probs, 'XGBoost', '#191919', ax=ax)
        ax.plot([0, 1], [1, 1], color='#C00000', linestyle='--', label='Random Model')
        
        # Style
        ax.set_xlabel('Proportion of Sample')
        ax.set_ylabel('Lift')
        ax.set_title('Lift Curve with 95% Confidence Intervals')
        ax.grid(True, linestyle='--', alpha=0.6, color='grey')
        ax.legend()
        plt.tight_layout()
        st.pyplot(fig)

   
        st.markdown("""
        For Logistic Regression, the lift reaches a value of 8 at the very top of the ranked sample (i.e., top predicted scores), drops to 4 at 
        the top 10%, and continues declining to 3 at 20%, ~2 at 40%, and 1.5 at 60% of the sample.

        The XGBoost model shows a similar shape but maintains slightly higher lift values in the top deciles. The curve confirms that both models 
        significantly outperform random guessing (lift = 1) in the upper-ranked segments, with diminishing marginal gains as larger segments of 
        the population are included.

        This behavior supports the effectiveness of both models for ranking and prioritization, especially when only a limited portion of the 
        population can be targeted (e.g., marketing campaigns or risk management). The curve's early steep rise also implies strong model 
        discrimination.

        **Decile Analysis**

        Decile analysis divides the scored population into ten equally sized groups (deciles) based on predicted probabilities, ranking them 
        from the highest to the lowest likelihood of a positive outcome. This analysis assesses the model’s ability to separate positive and 
        negative cases across these segments. A well-performing model will concentrate a disproportionate number of true positives in the top 
        deciles, indicating effective ranking capability.

        Higher lift values in top deciles reflect the model’s ability to identify high-probability cases more effectively than random selection. 
        As the decile rank decreases (i.e., moving toward lower-score groups), both the number of positives and the lift typically decline, 
        indicating reduced model performance in those segments.

        """)     
        st.latex(r"""
        \text{Lift}_d = \frac{\frac{TP_d}{n_d}}{\frac{P}{N}}
        """)
        
        st.markdown("""
        **Where:**
        - $\\text{Lift}_d$: Lift in decile *d*
        - $TP_d$: Number of True Positives in decile *d*
        - $n_d$: Total number of observations in decile *d*
        - $P$: Total number of Positive cases in the full population
        - $N$: Total number of observations in the full population
        - $P/N$: Baseline positive rate across the full population
        """)
        
        st.markdown("""
        The decile analysis for both models highlights a clear concentration of positive cases in the top deciles, affirming the models' ability 
        to effectively rank customers according to their likelihood of exhibiting the target behavior.
        
        In the **Logistic Regression** model, the top decile (Decile 9) includes 1,236 observations and achieves a **lift of approximately 4.27**, 
        indicating that this segment contains over four times the average rate of positive cases. With **609 positive cases** in this group, it is 
        ideal for prioritized interventions. As the decile rank decreases, both the number of positives and the lift decline consistently, which 
        reflects a natural drop in model performance in lower-risk segments.
        
        The **XGBoost** model shows a similar trend, with an even higher **lift of 4.56 in Decile 9**, where **650 positive cases** are concentrated. 
        The steady decrease in lift across the lower deciles is consistent with expectations, and the slightly stronger performance in the top segment 
        suggests XGBoost may offer more precise segmentation. The similarity in the mid and lower deciles between both models confirms their reliability 
        in identifying less likely targets with reduced effectiveness.
        
        **Overall**, the decile figures demonstrate the practical value of both models for operational decision-making, enabling **data-driven 
        prioritization** that aligns with business objectives.
        """)
        logreg_deciles = decile_analysis(y_test, logreg_probs)
        xgb_deciles = decile_analysis(y_test, xgb_probs)
        
        # Optional: zeige Tabellen
        st.subheader("📊 Decile Lift – Logistic Regression")
        st.dataframe(logreg_deciles)
        
        st.subheader("📊 Decile Lift – XGBoost")
        st.dataframe(xgb_deciles)
        
        # Diagramm
        fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
        fig.suptitle('Decile-wise Lift Comparison')
        
        # Plot: Logistic Regression
        axes[0].bar(logreg_deciles.index.astype(str), logreg_deciles['lift'], color='#097a80')
        axes[0].set_title('Logistic Regression')
        axes[0].set_xlabel('Decile (9 = highest predicted scores)')
        axes[0].set_ylabel('Lift')
        axes[0].grid(axis='y', linestyle='--', alpha=0.6, color='grey')
        
        # Plot: XGBoost
        axes[1].bar(xgb_deciles.index.astype(str), xgb_deciles['lift'], color='#191919')
        axes[1].set_title('XGBoost')
        axes[1].set_xlabel('Decile (9 = highest predicted scores)')
        axes[1].grid(axis='y', linestyle='--', alpha=0.6, color='grey')
        
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        st.pyplot(fig)

        
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
        #st.write(X_train.dtypes)
        #st.write("X_train types:", X_train.dtypes)
        #st.write("y_train unique values:", y_train.unique())
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

        def mark_best(df):
            df_marked = df.copy()
            for idx in df.index:
                idx_str = str(idx) 
                val1 = df.loc[idx, "Logistic Regression"]
                val2 = df.loc[idx, "XGBoost"]

                is_cost = "Cost" in idx_str or "€" in idx_str

                # Optional: Werte umrechnen, wenn es sich um Kosten handelt
                if is_cost:
                    val1 = val1 / 1000
                    val2 = val2 / 1000
                    if not idx_str.endswith("(k €)"):
                        df_marked.rename(index={idx: f"{idx_str} (k €)"}, inplace=True)
                        idx = f"{idx_str} (k €)"  # Update Referenz für loc unten
                
                if isinstance(val1, (float, int)) and isinstance(val2, (float, int)):
                    # Wenn kleiner besser (Cost, Error Rate etc.)
                    if "Rate" in idx_str or is_cost: #"Cost" in idx:
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
