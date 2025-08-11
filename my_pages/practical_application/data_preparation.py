import streamlit as st
from utils.image_loader import show_github_image
from utils.data_loader import load_csv_data
import pandas as pd
import numpy as np
import io
from utils.preprap_feature_engineering import build_pipeline
import graphviz
from sklearn import set_config
from sklearn.utils import estimator_html_repr
from utils.summary_stats import summary
from utils.my_colormaps import my_cmap_r
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
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
        on the scikit-learn interface (BaseEstimator, TransformerMixin). These reusable components were embedded into a 
        larger pipeline framework, enabling full integration with Pipeline and ColumnTransformer. This design supports 
        the principle of end-to-end pipeline completeness, ensuring all transformations—starting from raw ingestion 
        through to modeling-ready format—are encap¬sulated in a transparent and auditable structure.

        To systematically manage the heterogeneity of feature types, a composite pipeline architecture was implemented. 
        Using the ColumnTransformer, separate preprocessing paths were assigned to numerical and categorical variables. 
        This approach allows component-wise, column-specific preprocessing—such as imputation, scaling, and encoding—while 
        maintaining clarity and modularity. In industrial data science projects following CRISP-DM, this level of structure 
        ensures reproducibility and process integrity in the data workflows.

        """)
        show_github_image(
          image_filename="images/data_preparation_steps.PNG",
          repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
          caption=( "Figure 15: Overview of single steps within data preparation phase")
          )
        st.markdown("""

        We will now explore the individual data preprocessing steps in more detail, focusing on both procedural and 
        methodological considerations.

        **a) Pipeline I: Initial Cleaning and Recoding**
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
        """, unsafe_allow_html=True)
        st.markdown("""
        **b) Pipeline II: Structural Adjustments**
        <br>
        This step focused on structural refinement and ethical model integrity:
         - Duplicate Removal: Redundant records were eliminated to avoid data leakage and maintain statistical independence 
           across observations.
         - Feature Exclusion – duration: Despite its predictive strength, duration was excluded from modeling due to its 
           post-outcome nature—it is only known after the marketing contact and would therefore introduce severe data 
           leakage if used during training.
        <br>
        """, unsafe_allow_html=True)
        st.markdown("""
        **c) Strategic Train-Test Split**
        <br>
        Prior to applying final transformations, a stratified 70/30 train-test split was performed. This sequencing is 
        essential for preserving the independence of the test set and preventing information leakage from transformation 
        steps such as scaling and encoding (for more detailed information on this step see paragraph 3.3.2).
        
        The used stratification ensured consistent distribution of the target class—11.15% positive in the training set 
        and 11.53% in the test set—thus preserving representative¬ness and supporting reliable model evaluation. This 
        separation also enabled fitting transformations on the training data (fit_transform) and applying them to the 
        test data (transform) without introducing target leakage.
        <br><br>
        """, unsafe_allow_html=True)
        st.markdown("""
        **d) Pipeline III: Feature Transformation**
        <br>
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
        show_github_image(
          image_filename="images/preprocessing_pipelines.PNG",
          repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
          caption=( "Figure 16: Pipeline overview within data preparation phase")
          )
    elif task == "Strategic & Methodical Aspects of Train-Test-Split":
        st.subheader("3. Strategic & Methodical Aspects of Train-Test-Split")
        st.markdown("""
        A key consideration in model validation is the prevention of data leakage. Therefore, the train-test split was 
        performed before applying transformations such as scaling and encoding. This ensures that the StandardScaler and 
        OneHotEncoder were fitted exclusively on the training set (fit_transform), and only applied to the test set via 
        transform. This strategy aligns with best practices in machine learning, providing a realistic evaluation of 
        generalization performance.

        So, after all structural transformations were complete and irrelevant features removed, the dataset was split 
        into training (70%) and test (30%) subsets (stratified sampling). The decision to split the dataset into training 
        and test sets before standardization and encoding was crucial for preserving the integrity of the modeling pipeline.

         - Training Set (70%) was used to fit_transform() the StandardScaler() and OneHotEncoder(), ensuring that the 
           transformation logic (e.g. mean, variance, dummy mapping) was based only on known data.
         - Test Set (30%) was only exposed to these transformations via .transform(), ensuring no data leakage. All 
           transformations in pipeline III (standardization and encoding) involve parameter fitting. These parameters 
           (mean, variance, encoding logic) must be learned only from the training data using fit_transform and then 
           applied to the test data via transform

        This methodology ensures that:
         - Test performance remains unbiased and reflects true generalization. Fitting the scaler or encoder on the full 
           dataset before splitting would contaminate the test set and artificially boost performance metrics.
         - Feature distributions in the test set are not influencing model fitting or transformation logic.

        Train-Test Split and class distribution validation
        <br>
        The 70/30 train-test split was executed using stratified sampling to preserve class distribution. The target 
        variable, with approximately 11% positive responses in both the training and test sets, reflects the real-world 
        class imbalance inherent in the original dataset. This setup is crucial for:
         - Maintaining the representativeness of model evaluation.
         - Ensuring that model calibration and threshold tuning are based on realistic conditions.
         - Avoiding optimistic bias, which could result from an unbalanced or unstratified test sample.
        """, unsafe_allow_html=True)
        show_github_image(
          image_filename="images/train_test_split.PNG",
          repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
          caption=( "Figure 17: Train-test-split and class distribution validation")
          )

    elif task == "Model Comparison within the first Iteration":
        st.subheader("4. Model Comparison within the first Iteration")
        st.markdown("""
        Seven different classification algorithms were benchmarked using a uniform modeling framework, with preprocessing 
        steps applied via pipelines. The evaluation was conducted using both Train Accuracy and Repeated Stratified K-Fold 
        cross-Validation to ensure robust performance estimates.
         - Logistic Regression
         - KNeighborsClassifier
         - Gradient Boosting Classifier
         - Decision Tree
         - Random Forest
         - Naïve Bayes
         - XGBoost
         <br>
         Evaluation Logic:
         <br>
         - A broad spectrum of models was selected: from simple linear models (Logistic Regression) to complex non-linear 
           classifiers (XGBoost, Gradient Boosting, Random Forest).
         - Comparison of training and cross-validation scores revealed overfitting patterns (e.g., Decision Tree) and 
           robust generalization (e.g., Logistic Regression, Gradient Boosting).
         - Overfitting Detection:  Decision Tree with 99.5% train vs. 84.0% cross-validation accuracy as a good “negative 
           example”.
              
        """, unsafe_allow_html=True)
        show_github_image(
          image_filename="images/1st_iteration_modelling.PNG",
          repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
          caption=( "Figure 18: Overview of single steps within data preparation phase")
          )
        st.markdown("""
        <br>
        Model Focus for Second Iteration (Threshold Tuning)
        <br>
        Based on validation stability, interpretability, and predictive performance, two models were selected for further 
        optimization:
        <br>
        
        """, unsafe_allow_html=True)
        st.markdown("""
        **Logistic Regression**
                 
        - Stable and nearly identical scores in training and validation (90.1 % vs. 90.0 %).
        - Fully interpretable: ideal for explainability, compliance, and internal communication, internal audit and 
          regulatory transparency
        - Reliable benchmark for business applications
        <br><br>        
        """, unsafe_allow_html=True)
        st.markdown("""
        **XGBoost**
        
        - Best training performance (92.2 %) with solid validation (89.9 %).
        - Captures complex non-linear interactions without manual feature engineering
        - Industry standard for credit scoring, marketing classification and churn prediction
        <br><br>

        """, unsafe_allow_html=True)
        st.markdown("""
        **Didactic Rationale**
         
        - Selection of one linear and one non-linear model provides a clear trade-off comparison
            - Interpretability vs. Predictive Power
            - Transparency vs. Complexity

        """, unsafe_allow_html=True)
        st.markdown("""
        - Reflects best practices in model governance and machine learning application in business contexts.
        - Combination of linear and non-linear modeling paradigms allows
            - Clear analysis of performance vs. interpretability
            - Better justification of complexity from a business value standpoint
            - Robust foundation for threshold tuning using probability scores

        """, unsafe_allow_html=True)
    elif task == "Conclusions of the Data Preparation Phase":
        st.subheader("5. Conclusions of the Data Preparation Phase")
        st.markdown("""
        The data preparation phase established a clean, well-structured dataset ready for predictive modeling. The 
        deliberate separation of training and test sets before transformation, combined with reproducible pipelines and 
        robust cross-validation, ensures that the modeling phase is both technically sound and business-relevant. The 
        selected models—Logistic Regression and XGBoost—cover both transparency and performance, offering a strong basis 
        for final optimization and deployment in the next project phase.
        
         - Preprocessing logic was encapsulated into modular, testable units via custom transformer classes
         - A layered pipeline architecture separates semantic, structural, and statistical preparation steps
         - By splitting the data before feature transformation, the integrity of evaluation metrics was preserved
         - Clean use of ColumnTransformer ensures full pipeline compatibility with GridSearchCV

        This approach sets the stage for reliable, scalable, and interpretable modeling in subsequent phases                
        """, unsafe_allow_html=True)
        st.markdown("""
        Sometimes, users may wish to understand the technical foundation of the preprocessing steps. Tick the checkbox 
        below to dive into the full technical pipeline implementation.
        """)
        show_preprocessing = st.checkbox("Show technical preprocessing steps")
        if show_preprocessing:
          st.subheader("📂 Step 1: Load Data")
      
          df = load_csv_data(
              filename="data/bank-additional-full.csv",
              sep=";",
              header=True,
              add_row_id=True,
              ignore_index_column=False
          )
      
          st.success("CSV file loaded successfully.")
          st.write(df.head())
      
          st.subheader("🛠 Step 2: Feature Engineering – Add Year & Date Fields")
          
          # temporäre aggregation view
          df_view = (
              df.groupby(["month", "cons.price.idx"], as_index=False)
              .agg(
                  COUNT_TOTAL_PER_MONTH=("month", "count"),
                  MAX_RN_month=("ROW_ID", "max")
              )
          )
        
          # year initiation
          df_view["year"] = df_view["MAX_RN_month"].apply(
              lambda x: 2008 if x <= 27690 else (2009 if x <= 39130 else 2010)
          )
        
          # Merge with original df
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
        
          # Integer-type
          df["date_int"] = df["date_period"].dt.strftime('%Y%m').astype(int)
          df["date_period"] = df["date_period"].astype(str)      
      
          st.success("Date enriched successfully.")
          st.dataframe(df.head())
      
          st.subheader("🔄 Step 3: Apply Preprocessing Pipeline")
      
          preprocessor = build_pipeline(df)  # Custom-built scikit-learn pipeline
          set_config(display='diagram')
          html_code = estimator_html_repr(preprocessor)
          # BeautifulSoup initialisieren
          soup = BeautifulSoup(html_code, 'html.parser')
          
          color_variable_mapping = {
              "--sklearn-color-unfitted-level-0": "#0097A7",     # vorher: #fff5e6 → jetzt: Türkisblau
              "--sklearn-color-unfitted-level-1": "#f3f3f3",     # vorher: #f6e4d2
              "--sklearn-color-unfitted-level-2": "#d9d9d9",     # vorher: #ffe0b3
              "--sklearn-color-unfitted-level-3": "#C00000",     # vorher: chocolate
              "--sklearn-color-fitted-level-0": "#0097A7",       # vorher: #f0f8ff
              "--sklearn-color-fitted-level-1": "#097a80",       # vorher: #d4ebff
              "--sklearn-color-fitted-level-2": "#00575b",       # vorher: #b3dbfd
              "--sklearn-color-fitted-level-3": "#191919",       # vorher: cornflowerblue
              "--sklearn-color-icon": "#607d8b",                 # vorher: #696969
              "--sklearn-color-icon": "#00575b",                   # Einheitliches Icon-Petrol
              "--sklearn-color-text-on-default-background": "#191919",
              "--sklearn-color-background": "#f3f3f3",
              "--sklearn-color-border-box": "#191919",
          }
          
          for style_tag in soup.find_all("style"):
              style_text = style_tag.string
              if style_text:
                  for var_name, new_color in color_variable_mapping.items():
                      style_text = style_text.replace(var_name + ": ", f"{var_name}: {new_color}; /* replaced */ ")
                  style_tag.string.replace_with(style_text)

          
          html_wrapped = f"""
          <div style="
              width: 100%;
              overflow-x: auto;
              background-color: #f3f3f3;
              padding: 10px;
          ">
          <div style="
              max-width: 100%;   /* passt sich der Bildschirmbreite an */
              display: inline-block;
          ">
          {str(soup)}
          </div>
          </div>
          """

          st.components.v1.html(html_wrapped, height=600, scrolling=True)

          #st.components.v1.html(str(soup), height=450, scrolling=True) 
      
          preprocessor.set_output(transform='pandas')
          transformed_df = preprocessor.fit_transform(df)
      
          def make_streamlit_arrow_compatible(df: pd.DataFrame) -> pd.DataFrame:
              df = df.convert_dtypes()
              for col in df.select_dtypes(include='object').columns:
                  df[col] = df[col].apply(lambda x: str(x) if not pd.isna(x) else "")
              return df
      
          transformed_df = make_streamlit_arrow_compatible(transformed_df)
          st.success("Data transformed successfully.")
      
          st.subheader("📋 Step 4: DataFrame Info After Transformation")
          buffer = io.StringIO()
          transformed_df.info(buf=buffer)
          st.text("🧾 transformed_df.info():")
          st.text(buffer.getvalue())
          
          st.subheader("🧹 Step 5: Post-Processing – Drop Duplicates & Drop 'duration'")
          from utils.data_cleaning import get_cleaning_pipeline
          cleaning_pipeline = get_cleaning_pipeline(columns_to_drop='duration')
          newdf = cleaning_pipeline.fit_transform(transformed_df)

          st.success("Data cleaned successfully.")
          st.subheader("🔧 Pipeline: Drop Duplicates + Drop Column")

          html_code_cleaning = estimator_html_repr(cleaning_pipeline)
          soup_cleaning = BeautifulSoup(html_code_cleaning, 'html.parser')

          # Reuse color mapping
          for style_tag in soup_cleaning.find_all("style"):
              style_text = style_tag.string
              if style_text:
                  for var_name, new_color in color_variable_mapping.items():
                      style_text = style_text.replace(var_name + ": ", f"{var_name}: {new_color}; /* replaced */ ")
                  style_tag.string.replace_with(style_text)


          st.components.v1.html(str(soup_cleaning), height=500, scrolling=True)

          st.subheader("📊 Feature Summary After Cleaning")
          summary_df = summary(newdf)
          st.dataframe(summary_df)

          st.subheader("🎯 Step 6: Train/Test Split + Target Balance")

          y = newdf['target'].copy().astype(int)
          X = newdf.drop(["y", "target",  "year", "date_int", 'date_period'], axis=1).copy()

          from sklearn.model_selection import train_test_split
          X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
          st.success("Data splitted successfully between train & test.")
          y_train_dis = y_train.value_counts()
          y_test_dis = y_test.value_counts()

          fig, axs = plt.subplots(1, 2, figsize=(10, 5))

          axs[0].pie(
              y_train_dis, 
              explode=[0.2, 0.2],
              colors=['#d9d9d9', '#097a80'],
              autopct='%1.2f%%',
              shadow=True,
              labels=['No', 'Yes']
          )
          axs[0].set_title('Target distribution train data sample')
          axs[0].legend()

          axs[1].pie(
              y_test_dis,
              explode=[0.2, 0.2],
              colors=['#d9d9d9', '#097a80'],
              autopct='%1.2f%%',
              shadow=True,
              labels=['No', 'Yes']
          )
          axs[1].set_title('Target distribution test data sample')
          axs[1].legend()

          st.pyplot(fig)

          st.subheader("⚙️ Step 7: Final Preprocessing – Scaling & Encoding for Modeling")

          from sklearn.preprocessing import StandardScaler, OneHotEncoder
          from sklearn.pipeline import Pipeline
          from sklearn.compose import make_column_transformer

          # Transformer definieren
          scaler = StandardScaler()
          cat_ohe = OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False)
          cat_ohe.set_output(transform='pandas')
          scaler.set_output(transform='pandas')

          # Feature-Typen korrekt bestimmen (Streamlit-kompatibel)
          numerical_cols_PipX = [col for col in X.columns if pd.api.types.is_numeric_dtype(X[col])]
          categorical_cols_PipX = [col for col in X.columns if pd.api.types.is_string_dtype(X[col])]

          st.write("📐 Numerische Features:", numerical_cols_PipX)
          st.write("🧾 Kategorische Features:", categorical_cols_PipX)

          # Pipelines definieren
          NumericalPipeline_X = Pipeline(steps=[('standardization', scaler)])
          CategorialPipeline_X = Pipeline(steps=[('encoder', cat_ohe)])

          preprocessor_X = make_column_transformer(
              (NumericalPipeline_X, numerical_cols_PipX),
              (CategorialPipeline_X, categorical_cols_PipX),
              verbose_feature_names_out=False,
              remainder='passthrough'
          )
          preprocessor_X.set_output(transform='pandas')

          st.subheader("🧪 Pipeline: Scale + Encode")
          st.success("Data scaled & encoded successfully.")
          html_code_X = estimator_html_repr(preprocessor_X)
          soup_X = BeautifulSoup(html_code_X, 'html.parser')

          for style_tag in soup_X.find_all("style"):
              style_text = style_tag.string
              if style_text:
                  for var_name, new_color in color_variable_mapping.items():
                      style_text = style_text.replace(var_name + ": ", f"{var_name}: {new_color}; /* replaced */ ")
                  style_tag.string.replace_with(style_text)

          st.components.v1.html(str(soup_X), height=400, scrolling=True)

          X_train_transformed = preprocessor_X.fit_transform(X_train)
          X_test_transformed = preprocessor_X.transform(X_test)
          X_train_transformed = make_streamlit_arrow_compatible(X_train_transformed)
          X_test_transformed = make_streamlit_arrow_compatible(X_test_transformed)

          st.success("Final preprocessing complete.")
          st.write("✅ Dimensions of the training set:", X_train_transformed.shape)
          st.write("✅ Dimensions of the test set:", X_test_transformed.shape)

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
