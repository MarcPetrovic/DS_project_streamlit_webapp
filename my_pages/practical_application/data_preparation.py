import streamlit as st
from utils.image_loader import show_github_image
from utils.data_loader import load_csv_data
import pandas as pd
import numpy as np

def show():
  #  st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    task = st.selectbox("Select a subchapter of CRISP-DM-phase Data Preparation:", [
        "Introductory Remarks",
        "Technical & Practical Realization",
        "Strategic & Methodical Aspects of Train-Test-Split",
        "Model Comparison within the first Iteration",
        "Conclusions of the Data Preparation Phase"
    ])

    if task == "Introductory Remarks":
        st.subheader("1. Introductory Remarks Data Preparation Phase")
        st.markdown("""
        The third phase of the CRISP-DM process—Data Preparation—serves as a critical bridge between data understanding 
        and modeling. Building upon the insights gained during the previous phase, this step focuses on systematically 
        addressing the identified issues within the raw dataset and transforming the data into a clean, structured, and 
        model-ready format.

        The main objective of this phase is to create a consistent and analytically robust data foundation that meets 
        both the methodological requirements of the modeling process and the contextual demands of the business domain. 
        This includes, among other things, the removal of duplicate records, appropriate handling of missing or incomplete 
        values, encoding of categorical attributes, and transformation of numerical variables to ensure comparability and 
        support algorithmic performance.

        Particular emphasis is placed on adhering to empirically and domain-informed recommendations—such as the exclusion 
        of the duration variable to prevent data leakage—as well as on the practical implementation of preprocessing 
        strategies derived from the data audit. Each transformation step is carried out in a transparent and reproducible 
        manner, thereby safeguarding the relevance, integrity, and modeling suitability of the prepared dataset.

        The following sections provide a structured overview of the data preparation process. This includes a description 
        of the technical and practical realization of preprocessing tasks, the rationale and implementation of the train-
        test split, a preliminary model comparison, and a summary of key results from Phase 3.
        """, unsafe_allow_html=True)

    if task == "Technical & Practical Realization":
        st.subheader("2. Technical & Practical Realization of Data (Pre-)Processing")
        st.markdown("""
        To operationalize the insights derived from the data understanding phase and to comply with CRISP-DM’s standards 
        for structured, reproducible workflows, the data preparation process was implemented in Python within a Jupyter 
        Notebook environ-ment, deployed via the Anaconda Cloud framework. This setup ensures a controlled development 
        environment that prevents dependency conflicts and enhances reproducibility.

        In line with industry-oriented modular design principles, a custom transformer archi¬tecture was developed, based 
        on the scikit-learn interface (BaseEstimator, Transfor¬merMixin). These reusable components were embedded into a 
        larger pipeline framework, enabling full integration with Pipeline and ColumnTransformer. This design supports 
        the principle of end-to-end pipeline completeness, ensuring all transformations—starting from raw ingestion 
        through to modeling-ready format—are encap¬sulated in a transparent and auditable structure.

        To systematically manage the heterogeneity of feature types, a composite pipeline architecture was implemented. 
        Using the ColumnTransformer, separate prepro-cessing paths were assigned to numerical and categorical variables. 
        This approach allows component-wise, column-specific preprocessing—such as imputation, scaling, and encoding—while 
        maintaining clarity and modularity. In industrial data science projects following CRISP-DM, this level of structure 
        ensures reproducibility and pro¬cess integrity in the data workflows.

        We will now explore the individual data preprocessing steps in more detail, focusing on both procedural and 
        methodological considerations.

        a). Pipeline I: Initial Cleaning and Recoding
         - Target Variable Transformation: The binary target variable y ("yes"/"no") was converted into a dummy variable 
           (1 for "yes", 0 for "no"), making it compatible with classification algorithms.
         - Handling Missing Values ("unknown"): Placeholder values like "unknown" were replaced with NaN and subsequently 
           imputed using SimpleImputer(strate-gy="most_frequent"), a technique particularly suitable for categorical 
           variables.
         - Feature Harmonization – default: The default feature was binarized into a unified "unknown|yes" group. This 
           consolidation reflects domain knowledge from the financial sector, where both values indicate increased credit 
           risk and low quality of information.
         - Semantic Reformatting – pdays: The value 999, used to indicate lack of prior contact, was recoded into 0 
           ( = not contacted), improving semantic clarity.
        <br>

        b) Pipeline II: Structural Adjustments 
        This step focused on structural refinement and ethical model integrity:
         - Duplicate Removal: Redundant records were eliminated to avoid data leakage and maintain statistical independence 
           across observations.
         - Feature Exclusion – duration: Despite its predictive strength, duration was excluded from modeling due to its 
           post-outcome nature—it is only known after the marketing contact and would therefore introduce severe data 
           leakage if used during training.
        <br>            
        c) Strategic Train-Test Split
        Prior to applying final transformations, a stratified 70/30 train-test split was performed. This sequencing is 
        essential for preserving the independence of the test set and preventing information leakage from transformation 
        steps such as scaling and encoding (for more detailed information on this step see paragraph 3.3.2).
        <br>
        The used stratification ensured consistent distribution of the target class—11.15% positive in the training set 
        and 11.53% in the test set—thus preserving representative¬ness and supporting reliable model evaluation. This 
        separation also enabled fitting transformations on the training data (fit_transform) and applying them to the 
        test data (transform) without introducing target leakage.
        <br>
        d) Pipeline III: Feature Transformation
        This final preprocessing stage ensured that the data conformed to the input require¬ments of machine learning 
        models, both in terms of scale and format.
         - Z-Standardization for numeric features was applied using StandardScaler() function. Each continuous feature 
           was centered (mean = 0) and scaled (std = 1), which improves performance of Distance-based algorithms (e.g. KNN) 
           and regularized linear models (e.g. Logistic Regression with L2 penalty). This ensures numeric comparability 
           across features, accelerates model convergence and is required for many ML algorithms. Unfortunately, this 
           method is **not robust to outliers** (can skew the mean and standard deviation) and the **transformed values lose 
           intuitive interpretability.**
         - One-Hot Encoding was applied to categorical variables. These features were transformed via OneHotEncoder(drop=
           'first', handle_unknown='ignore', sparse_out-put=False), producing binary indicator columns for all but not for 
           the first category (to avoid multicollinearity). This method retains full category information, is widely 
           supported by most algorithms and very safety for non-linear models. Unfortunately, this can on the one hand 
           create very large sparse matrices for high-cardinality features. On the other hand, it increases model 
           complexity and memory consumption.
        """, unsafe_allow_html=True)
          # Bild von der URL laden und anzeigen 
        show_github_image(
          image_filename="images/attribute_cluster.PNG",
          repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
          caption=( "Figure 9: Overview of the four data type clusters within the used database")
          )
    elif task == "Strategic & Methodical Aspects of Train-Test-Split":
        st.subheader("3. Strategic & Methodical Aspects of Train-Test-Split")
        st.markdown("""
        The authors provide the following key recommendations and insights, which are directly relevant to the current project:
         - Missing Values: Several categorical attributes contain missing values, represented by the label "unknown". According to 
           the authors, these should be handled explicitly, either by treating them as a valid class category or by applying 
           deletion or imputation techniques, depending on the intended analysis and model type.
         - Feature Importance and Predictive Use: Particular caution is advised when interpreting and using the variable duration 
           (last contact duration in seconds). While highly predictive, this attribute is only known after the outcome of the 
           contact and thus cannot be used in a real-time predictive setting. Moro et al. recommend that this feature be excluded 
           from models aiming to simulate realistic predictive scenarios and used only for benchmark comparison purposes.
         - Attribute Documentation: Detailed descriptions of all 20 input attributes and the binary target variable y are provided 
           in the accompanying metadata file.
        """, unsafe_allow_html=True)
