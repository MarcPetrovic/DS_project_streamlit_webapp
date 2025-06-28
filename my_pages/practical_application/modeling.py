import streamlit as st
from utils.image_loader import show_github_image

def show():
#    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    task = st.selectbox("Select a subchapter of CRISP-DM-phase Modelling:", [
        "Introduction to the modelling phase",
        "Theoretical relevance of Success Profile Analysis",
        "Practical Application of Success Profile Analysis",
        "Data Processing & Feature Engineering based on SPA",
        "Summary of the modelling phase & transition to evaluation phase"
    ])

    if task == "Introduction to the modelling phase":
        st.subheader("1. Introduction to the modelling phase")
        st.markdown("""
        In the context of the present data science project, the modeling chapter aims to bridge the insights derived 
        from exploratory data analysis with robust, interpretable, and business-aligned predictive modelling. Structurally, 
        it is divided into four inter¬linked subchapters: 
        
        Section 3.4.1 presents the theoretical relevance and practical application of Success Profile Analysis (SPA) within 
        financial services, emphasizing its function as both a diagnostic tool and a regulatory interface. Section 3.4.2 
        illustrates the concrete application of SPA to the present dataset, establishing segment-level insights and 
        identifying success-driving behavioural patterns. These empirical findings then inform the data processing and 
        feature engineering strategies detailed in Section 3.4.3, where the transformation logic is technically implemented 
        using object-oriented classes, pipelines, and column transformers. The modeling phase concludes in Section 3.4.4 
        with a synthesis of key findings and a conceptual transition into the evaluation phase, in which two classification 
        algorithms and four threshold tuning strategies are systematically compared.
        """, unsafe_allow_html=True)

    if task == "Theoretical relevance of Success Profile Analysis":
        st.subheader("2. Theoretical & practical relevance of Success Profile Analysis")
        st.markdown("""
        Success Profile Analysis (SPA), also referred to as characteristic profiling, is an established methodology within 
        the financial services and risk analytics domain. It focuses on analyzing the relationship between individual 
        feature levels (e.g., age brackets, education, or employment status) and a binary target outcome, such as credit 
        default or product subscription.

        From a theoretical perspective, SPA represents a bivariate diagnostic tool capable of detecting nonlinear effects 
        and group-specific deviations in success rates that might not be revealed by traditional multivariate models. 
        Particularly in the context of risk scoring and subscription modeling, SPA enables early identification of 
        discriminative patterns in feature distributions. In this way, it uncovers domain-relevant group structures and 
        serves as a hypothesis-generating mechanism for downstream feature engineering.

        The practical value of SPA lies in its strong interpretability and alignment with regulatory expectations. In an 
        increasingly transparency-driven modeling environment—especially in credit decisioning—SPA provides an effective 
        framework for involving both business stakeholders and supervisory bodies in the model development process. Within 
        regulated industries such as banking or insurance, SPA enhances model transparency by establishing traceable success 
        patterns prior to model training, thereby meeting essential compliance requirements.

        Moreover, the method facilitates the early detection of business-critical customer segments, such as high-risk profiles 
        or clusters with elevated conversion potential. This supports more effective resource allocation and campaign targeting. 
        By visually highlighting significant deviations from average success probabilities, SPA fosters not only transparency 
        but also domain-specific interpretability—an essential objective of modern data science practices in regulated 
        environments.

        """, unsafe_allow_html=True)

    if task == "Practical Application of Success Profile Analysis":
        st.subheader("3. Practical Application of Success Profile Analysis (SPA)")
        st.markdown("""
        In the context of the present use case, SPA was applied to identify relevant segmentations of predictor variables. 
        The methodological basis is provided by the function plot_cat_distribution_vs_success(), which combines bar plots of 
        group-wise distributions with line plots of corresponding success rates and confidence intervals. This dual-plot 
        structure visually emphasizes both the statistical reliability of observed outcomes and their deviation from the 
        population average. Observed success rates are accompanied by binomial confidence intervals (typically at the 95% 
        level), and statistically significant deviations are marked to increase interpretability.

        This visualization approach plays a central role in translating raw variables into analytically meaningful features. 
        For instance, continuous variables such as the employment index (nr.employed) were segmented into interpretable bins 
        using domain-informed cut points. These segments were then evaluated regarding their respective success rates. 
        Graphical examples (cf. integrated illustrations) highlight how these groupings expose non-linear behaviors and 
        inform the selection of modeling-relevant intervals.

        Based on the observed patterns, variables were categorized into transformation strategies. Binary recoding via dummy 
        coding was employed where one specific category (e.g., 'success' in the poutcome variable) exhibited a significantly 
        elevated success rate. In contrast, more complex relationships were captured using effect coding, where multiple 
        categories were grouped into +1/0/−1 schemes to reflect directional impact (e.g., in job, education, or age).

        These transformations were operationalized via custom transformer classes inheriting from BaseEstimator and 
        TransformerMixin. The use of modular transformation classes ensured reproducibility and clear traceability of applied 
        rules. All transformations were ultimately structured within Pipeline objects to ensure compatibility with the broader 
        machine learning workflow.
        
        """, unsafe_allow_html=True)
    if task == "Data Processing & Feature Engineering based on SPA":
        st.subheader("4. Data Processing & Feature Engineering based on SPA")
        st.markdown("""
        The empirical patterns discovered through SPA directly guided the construction of the feature engineering pipeline. 
        Each selected variable was assigned a dedicated transformation path, often combining SPA-based grouping logic with 
        technical encoding. To ensure consistency and maintainability, each transformation was encapsulated as a custom 
        Python class. For example, CustTransDummyPoutcome handled binary recoding based on SPA insights, while 
        CustTransEffectJob implement¬ted effect coding logic for more nuanced feature representations. Each class outputs 
        modified features that reflect the success profile analysis, while simultaneously dropping the original column via 
        a ColumnDrop() transformer.

        The transformed features were then orchestrated within a make_column_trans-former() object. This transformer bundled 
        all transformation steps and combines further standard preprocessing steps like standardization and one-hot encoding 
        for residual variables into a unified preprocessing block. This block is furthermore compatible with downstream 
        modeling tools (e.g., GridSearchCV, model export, and deployment). The pipeline followed a layered structure, 
        combining:
         - SPA-based semantic transformations (dummy/effect coding)
         - Temporal feature transformations (e.g., weekday and month handling)
          - Standardization of numerical and categorical residual variables
          - Passthrough handling for pre-cleaned variables

        This approach ensured not only technical robustness and modularity but also interpretability of each transformation 
        step. The pipeline design is visualized within the project (cf. embedded diagrams) and executed using scikit-learn's 
        pipeline framework.

        For instance, the variable euribor3m was segmented based on SPA outcomes, then processed in a pipeline consisting of 
        an effect transformation followed by column dropping. Similar pipelines were constructed for nr.employed, month, 
        day_of_week, and sociodemographic attributes such as job, age, and education.

        In sum, the transition from SPA to technically robust feature engineering represents a methodologically sound 
        integration of business logic into the model design process. Furthermore, it involved both analytical reasoning and 
        reproducible implementation logic. By translating group-level success insights into structured transformations, the 
        project ensured that predictive modeling would rest on a well-founded, interpretable, and business-aligned feature 
        set. The use of visual SPA outputs, paired with class-based transformation pipelines, serves as a best-practice 
        blueprint for integrating expert knowledge into data-driven environments.
        
        """, unsafe_allow_html=True)
