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
from utils.plot_gains_chart import *
from utils.display_helpers import display_strategy_results

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

# hier war def render_html_table_metrics(df: pd.DataFrame) -> str:
        
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
        """)
        show_github_image(
            image_filename="images/evaluation_dmp_tts_fia.PNG",
            repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
            caption="Figure 24: Overview of different evaluation levels, reaching from overall discriminative model performance, threshold tuning strategies & feature importance analysis"
        )
        st.markdown("""        
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
        
        #st.subheader("📊 Decile Lift – Logistic Regression")
        #st.dataframe(logreg_deciles)
        
        #st.subheader("📊 Decile Lift – XGBoost")
        #st.dataframe(xgb_deciles)

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
        st.markdown("""
        **Gains Chart vs. ROC Curve: Interpretation**

        The Gains Chart displays the cumulative proportion of positive cases identified by selecting a given proportion of the population sorted 
        by predicted probability. It is especially helpful in real-world applications, such as determining how many true positives can be 
        captured by targeting the top 10%, 20%, or 30% of the model’s predicted rankings. This makes it a highly actionable tool for campaign 
        management, budget allocation, and resource optimization. 

        In contrast, the ROC Curve plots the True Positive Rate (Sensitivity) against the False Positive Rate (1 – Specificity) for all possible 
        thresholds. It provides a threshold-independent measure of model performance, useful for assessing general discriminative ability, 
        especially in imbalanced datasets. However, it does not offer direct insight into business outcomes or operational metrics such as 
        customer reach or return on investment. Thus, while the ROC Curve is valuable for evaluating classification quality, the Gains Chart is 
        more aligned with cost-benefit considerations and decision support in applied settings.
        """)
        st.subheader("📈 Gains Chart")

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_facecolor('lightgrey')
    
        plot_gains_chart(y_test, logreg_probs, 'Logistic Regression', '#097a80')
        plot_gains_chart(y_test, xgb_probs, 'XGBoost', '#191919')
        
        # Random Model
        plt.plot([0, 1], [0, 1], color='#C00000', linestyle='--', label='Random Model')
        
        # Layout
        plt.xlabel('Proportion of Sample')
        plt.ylabel('Cumulative Gain')
        plt.title('Gains Chart')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7, color='grey')
        plt.tight_layout()
        st.pyplot(fig)
        
    elif strategy == "feature_importance":
        st.markdown("## Feature Importance Exploration")
        st.write("""
        In addition to evaluating predictive performance and threshold optimization, understanding which input features drive 
        model behavior is essential for interpretability, transparency, and operational trust in applied machine learning 
        systems. In this section, both the logistic regression and XGBoost models are analyzed with regard to feature importance, 
        focusing on statistical significance, relative influence, and thematic clustering.

        For the logistic regression model, feature importance was assessed via estimated coefficients and transformed Odds Ratios, 
        with standardization to Normalized Odds Ratios (in %). To ensure interpretability and statistical robustness, only features 
        with p-values below 0.05 were retained, excluding the intercept term. To facilitate comparison between positively and 
        negatively associated variables, all Odds Ratios were normalized using the transformation:
        
        - Normalized Odds Ratio = (Odds Ratio−1) × 100

        This yielded a unified scale of effect size and directionality (see Figure 60), where features with higher absolute normalized 
        odds ratios are deemed more influential. Among the top-ranked variables were poutcome_success (412.6%), nr.employed_dummy 
        (129.3%), cons.price.idx (103.7%), and poutcome_nonexistent (80.6%). These variables suggest a particularly strong impact of 
        campaign outcome history and macroeconomic conditions on subscription probability. Several other variables related to contact 
        method, and economic sentiment (e.g., emp.var.rate, euribor3m_effect, cons.conf.idx) also demonstrated statistical relevance, 
        albeit with more moderate effect sizes.

        The XGBoost model's feature importance was extracted using gain-based internal rankings (see Figure 61). Here, nr.employed_dummy 
        dominated with a relative importance of 0.69, followed by emp.var.rate (0.097), cons.conf.idx (0.045), and pdays_cat (0.043). While 
        this ranking differs in scale and methodology from logistic regression, a substantial thematic overlap is observable: both models 
        consistently identify employment indicators, economic sentiment, and past campaign performance as central drivers of model predictions.

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

        st.markdown("""
        A closer comparative analysis of both models reveals a subset of features that are consistently relevant across logistic 
        regression and XGBoost, despite fundamental differences in model architecture. These shared variables can be grouped into 
        three major semantic feature clusters:
        
        1.	Macro-economic environment
            - nr.employed_dummy
            - emp.var.rate
            - cons.conf.idx
            - euribor3m_effect
        """)
        st.markdown("""
            These indicators reflect the general labor market and consumer confidence conditions at the time of contact. 
            Their strong influence in both models underscores the substantial role of the economic climate in shaping 
            customer behavior.

        """, unsafe_allow_html=True)
        st.markdown("""
        
        2.	Previous marketing activities
            - pdays_cat
            - poutcome_success
            - contact_telephone
        """)
        st.markdown("""
            These variables capture past campaign interaction (e.g., whether the customer was previously contacted 
            successfully or at all) and communication channel (telephone = 1 vs. mobile = 0). Their consistent presence 
            suggests that campaign history and contact method critically influence the success probability of subsequent 
            outreach.
        
        """, unsafe_allow_html=True)
        st.markdown("""
        
        3.	Socio-economic items
            - default_cat_unknown|yes
        """)
        st.markdown("""
            This binary variable encodes whether a customer is currently in default or the information is missing, both of 
            which appear to be treated similarly by the models as risk signals. Its retained importance highlights the 
            relevance of a customer’s credit status in response modeling.

        """)
        st.markdown("""
        
        These findings highlight a convergent understanding of feature relevance, despite fundamental differences in model 
        structure and learning mechanism. However, beyond these commonalities, several model-specific differences emerge. 
        The logistic regression model, for instance, assigns high normalized importance to cons.price.idx (consumer price 
        index), a macroeconomic variable that does not appear among the top-ranked XGBoost features. Additionally, the 
        categorical level poutcome_nonexistent—indicating no prior campaign contact—is statistically significant in logistic 
        regression but carries limited gain-based weight in the XGBoost model. Finally, the cosine-transformed contact month 
        (month_numeric_cos) appears relevant only in the tree-based model, suggesting that non-linear seasonal patterns may 
        be better captured through XGBoost’s flexible structure, whereas the sine transformation showed no substantial effect 
        in either model.

        The mentioned findings underline both convergence and divergence in model behavior: while the core decision logic 
        appears to rest on similar economic, behavioral, and financial indicators, the granularity and interaction structure 
        of these features may be modeled differently. Such insights not only inform feature selection and model simplification 
        strategies, but also contribute to a transparent interpretation of why certain models outperform others in predictive 
        accuracy and cost efficiency.

        To promote parsimony and model generalizability, future versions of the pipeline may exclude low-impact variables, 
        particularly those not consistently ranked across models or lacking substantive interpretive value. This may include 
        variables with small coefficients and low gain importance, which contribute minimally to classification strength and 
        may increase overfitting risk in smaller deployment settings.
        """, unsafe_allow_html=True)
        
   
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

        if strategy == "cost":
            display_strategy_results(
                strategy_label=strategy,
                markdown_intro="""
                While default classification thresholds (e.g., 0.500) are often used in practice, they rarely align with the cost structure of real-world 
                business problems. In domains such as direct marketing for banking products, the economic impact of misclassifications is asymmetric: false 
                negatives (i.e., missed contracts) incur high opportunity costs, while false positives (i.e., unnecessary outreach) generate operational 
                costs. Accordingly, threshold selection based on cost minimization represents a more economically rational alternative.
                
                As detailed in Section 3.1.1, this project adopts a cost model in which:
                - False Positives are penalized with €550 (per unnecessary contact/calls),
                - False Negatives incur €3,350 (per missed successful customer/contract).
    
                This 6:1 cost ratio directly informs the threshold optimization process. Instead of maximizing conventional metrics like accuracy or 
                F1 score, thresholds are selected to minimize total expected cost across the classification spectrum. Figure 48 visualizes the cost 
                curves for both models over a range of thresholds. The cost-optimal thresholds are identified as:
                - 0.141 for Logistic Regression
                - 0.161 for XGBoost
                """,
                plot_figure=plot_opex_optimization(y_test, logreg_probs, xgb_probs, language="en"),
                markdown_after_plot="""
                The updated performance metrics under these thresholds are reported in Table 7, revealing significant shifts compared to the default 
                configuration (Table 6). These adjustments reflect the models' improved alignment with the underlying cost asymmetry.
                As shown in table 7, cost-optimized thresholding reduces total cost compared to the default threshold (0.500) by:
                - €1,203,950 for Logistic Regression (from €3,900,300 to €2,696,350)
                - €1,130,950 for XGBoost (from €3,681,600 to €2,550,650)
                
                These correspond to cost savings of approximately 30.9% and 30.7%, respectively.

                To fully evaluate model performance, it is informative to compare these results to two theoretical benchmark strategies: the null model 
                and the total model. In the null model scenario—where no customers are contacted—the institution avoids all operational costs but fails 
                to reach any potential converters. According to the confusion matrix of the logistic regression model (see Figure 49), the test set 
                contains 880 true positives and 544 false negatives, summing to a total of 1,424 actual positives. In the absence of any contact, all 
                1,424 cases become false negatives, resulting in opportunity costs of:
                
                                               1,424 x €3,350 = €4,767,400

                Total cost: €4.77 million, incurred solely through missed business opportunities.
                Conversely, the total model assumes full market coverage—every customer is contacted regardless of likelihood. Based on the confusion 
                matrix from the same model (see Figure 50), the total number of test-set instances is 12,353. As each contact incurs a cost of €550, the 
                operational cost is calculated as:

                                               12,353 × €550 = €6,793,150

                Total cost: €6.79 million, generated entirely through outreach-related expenditure.
                """,
                y_test=y_test,
                logreg_probs=logreg_probs,
                xgb_probs=xgb_probs,
                metrics_logreg=metrics_logreg,
                metrics_xgb=metrics_xgb,
                cmap=cmap_4,
                markdown_metrics_text="### Performance Metrics (with ✅ for better model)",
                markdown_between_confusion_and_metrics="""
                
                These values, derived from the confusion matrices in Figures 49 and 50, serve as upper and lower bounds in the decision space: the null 
                model minimizes operational effort but leads to maximum opportunity loss, whereas the total model guarantees full coverage at the expense 
                of massive contact costs. Compared to these baselines, both machine learning models—particularly XGBoost—offer substantial cost advantages 
                when deployed with cost-optimized thresholds. Specifically, XGBoost yields cost savings of more than €2.2 million relative to both the null 
                model and the total model—demonstrating that selective, model-based targeting clearly outperforms naive all-or-nothing strategies.

                Cost-optimized thresholding illustrates the integration of predictive analytics with business-centric utility functions. By grounding threshold 
                selection in cost asymmetry, rather than arbitrary probability cutoffs, the resulting models deliver not only improved classification performance 
                but also quantifiable economic benefit. Among the evaluated models, XGBoost emerges as the superior choice, offering a favorable balance of 
                precision, recall, and cost efficiency.
                """,
                markdown_after_table="""

                While this thresholding approach is explicitly aligned with business costs, the following section explores an alternative optimization method based 
                on a purely statistical criterion: the Youden Index, which seeks to balance sensitivity and specificity independent of financial considerations. This 
                upcoming strategy provides a useful contrast to cost-based optimization and contributes to a more holistic understanding of threshold selection in 
                applied machine learning.
                """
            )
        
        elif strategy == "youden":
            display_strategy_results(
                strategy_label=strategy,
                markdown_intro="""
                ### Youden Index Optimization  
                This approach maximizes the sum of sensitivity and specificity (Youden’s J statistic) to find a balanced threshold.
                """,
                plot_figure=plot_roc_with_youden(y_test, logreg_probs, xgb_probs),
                markdown_after_plot="The optimal thresholds are where TPR - FPR is maximized on the ROC curve.",
                y_test=y_test,
                logreg_probs=logreg_probs,
                xgb_probs=xgb_probs,
                metrics_logreg=metrics_logreg,
                metrics_xgb=metrics_xgb,
                cmap=cmap_4,
                markdown_metrics_text="### Performance Metrics (Thresholds via Youden Index)"
            )
        
        elif strategy == "f1":
            display_strategy_results(
                strategy_label=strategy,
                markdown_intro="""
                ### F1-Score Maximization  
                This strategy identifies the threshold that maximizes the harmonic mean of precision and recall.
                """,
                plot_figure=plot_precision_recall_with_f1_thresholds(y_test, logreg_probs, xgb_probs),
                markdown_after_plot="Optimal thresholds correspond to the highest F1-score along the PR curve.",
                y_test=y_test,
                logreg_probs=logreg_probs,
                xgb_probs=xgb_probs,
                metrics_logreg=metrics_logreg,
                metrics_xgb=metrics_xgb,
                cmap=cmap_4,
                markdown_metrics_text="### Evaluation Metrics Based on F1-Optimized Thresholds"
            )
        
        elif strategy == "pr_gap":
            display_strategy_results(
                strategy_label=strategy,
                markdown_intro="""
                ### Precision–Recall Gap Minimization  
                This strategy selects thresholds that minimize the absolute difference between precision and recall.
                """,
                plot_figure=plot_precision_recall_gap(y_test, logreg_probs, xgb_probs),
                markdown_after_plot="Thresholds are chosen where the gap between precision and recall is smallest.",
                y_test=y_test,
                logreg_probs=logreg_probs,
                xgb_probs=xgb_probs,
                metrics_logreg=metrics_logreg,
                metrics_xgb=metrics_xgb,
                cmap=cmap_4,
                markdown_metrics_text="### Metrics under PR-Gap-Minimizing Thresholds"
            )
        
        elif strategy == "default":
            display_strategy_results(
                strategy_label=strategy,
                markdown_intro="""
                ### Default Threshold (0.5)  
                This section presents a comparative evaluation of the two classification models – Logistic Regression and XGBoost – under a default probability threshold 
                of 0.500, which is widely used as a baseline in binary classification tasks. While such a configuration may be standard, it is often suboptimal in 
                cost-sensitive, imbalanced domains where the asymmetry between false positives and false negatives carries significant operational and financial implications.

                The evaluation builds on a cost-sensitive performance framework, assigning €550 to each false positive (i.e., unnecessary customer contact) and €3,350 to 
                each false negative (i.e., missed successful contact or lost conversion, for more detailed informa-tion see Section 3.1.1). The corresponding metrics are 
                summarized in Table 6 and visualized in Figures 46 and 47, which include the Confusion Matrix for both models.
                """,
                plot_figure=None,
                y_test=y_test,
                logreg_probs=logreg_probs,
                xgb_probs=xgb_probs,
                metrics_logreg=metrics_logreg,
                metrics_xgb=metrics_xgb,
                cmap=cmap_4,
                markdown_metrics_text="### Performance Metrics for Default Threshold (0.500 | with ✅ for better model)",
                markdown_between_confusion_and_metrics="""        
                From a performance metrics perspective, Logistic Regression exhibits marginally superior values in precision and false positive rate, indicating a more 
                conservative prediction strategy that favors precision over recall. This trait may be desirable in operational settings where minimizing unnecessary outreach 
                is prioritized, such as when agent time is limited or customer contact entails reputational risk.

                However, XGBoost consistently outperforms Logistic Regression across the remaining metrics, most notably in recall (+5.1pp), F1 score (+0.055), accuracy, and 
                Cohen’s kappa, as well as in the Matthews correlation coefficient. These indicators point to a higher discriminative capacity and a better balance between 
                sensitivity and specificity.

                From an economic standpoint, the total cost associated with XGBoost is approximately €218,700 lower than that of Logistic Regression when applying the same 
                threshold. This cost differential is the result of fewer false negatives—and therefore lower opportunity costs—despite a slightly higher false positive burden.
                """
            )
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
