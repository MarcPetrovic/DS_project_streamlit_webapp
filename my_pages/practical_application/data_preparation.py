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
          caption=( "Figure 10: Overview of single steps within data preparation phase")
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
          caption=( "Figure 11: Pipeline overview within data preparation phase")
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
    elif task == "Conclusions of the Data Preparation Phase":
        st.subheader("4. Conclusions of the Data Preparation Phase")
        st.markdown("""
        The data preparation phase established a clean, well-structured dataset ready for predictive modeling. The 
        deliberate separation of training and test sets before transformation, combined with reproducible pipelines and 
        robust cross-validation, ensures that the modeling phase is both technically sound and business-relevant. The 
        selected models—Logistic Regression and XGBoost—cover both transparency and performance, offering a strong basis 
        for final optimization and deployment in the next project phase.
        
        The authors provide the following key recommendations and insights, which are directly relevant to the current project:
         - Preprocessing logic was encapsulated into modular, testable units via custom transformer classes
         - A layered pipeline architecture separates semantic, structural, and statistical preparation steps
         - By splitting the data before feature transformation, the integrity of evaluation metrics was preserved
         - Clean use of ColumnTransformer ensures full pipeline compatibility with GridSearchCV, model export, and deployment

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
              add_row_id=True
          )
      
          st.success("CSV file loaded successfully.")
          st.write(df.head())
      
          st.subheader("🛠 Step 2: Feature Engineering – Add Year & Date Fields")
      
          grouped = df.groupby(["month", "cons.price.idx"]).agg(
              COUNT_TOTAL_PER_MONTH=('month', 'count'),
              MAX_RN_month=('ROW_ID', 'max')
          ).reset_index()
      
          def assign_year(row):
              if row['MAX_RN_month'] <= 27690:
                  return 2008
              elif row['MAX_RN_month'] <= 39130:
                  return 2009
              else:
                  return 2010
      
          grouped['year'] = grouped.apply(assign_year, axis=1)
          df = pd.merge(df, grouped[['month', 'cons.price.idx', 'year']], on=['month', 'cons.price.idx'], how='left')
          df['date_period'] = pd.to_datetime(df['year'].astype(str) + "-" + pd.to_datetime(df['month'], format='%b').dt.month.astype(str)).dt.to_period('M')
          df['date_int'] = df['date_period'].dt.strftime('%Y%m').astype(int)
          df['date_period'] = df['date_period'].astype(str)
      
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
          
          st.components.v1.html(str(soup), height=700, scrolling=True) 
      
          preprocessor.set_output(transform='pandas')
          transformed_df = preprocessor.fit_transform(df)
      
          def make_streamlit_arrow_compatible(df: pd.DataFrame) -> pd.DataFrame:
              df = df.convert_dtypes()
              for col in df.select_dtypes(include='object').columns:
                  df[col] = df[col].apply(lambda x: str(x) if not pd.isna(x) else "")
              return df
      
          transformed_df = make_streamlit_arrow_compatible(transformed_df)
      
          st.subheader("📋 Step 4: DataFrame Info After Transformation")
          buffer = io.StringIO()
          transformed_df.info(buf=buffer)
          st.text("🧾 transformed_df.info():")
          st.text(buffer.getvalue())
          
          st.subheader("🧹 Step 5: Post-Processing – Drop Duplicates & Drop 'duration'")

          # Reinigungspipeline laden und anwenden
          from pipeline_utils import get_cleaning_pipeline
          cleaning_pipeline = get_cleaning_pipeline(columns_to_drop='duration')
          newdf = cleaning_pipeline.fit_transform(transformed_df)

          # Zeige Ergebnisübersicht
          buffer2 = io.StringIO()
          newdf.info(buf=buffer2)
          st.text("🧾 newdf.info():")
          st.text(buffer2.getvalue())

          # Optional: tabellarische Übersicht
          st.subheader("📊 Feature Summary After Cleaning")
          summary_df = summary(newdf)
          st.dataframe(summary_df)

          # Visualisierung der Cleaning-Pipeline
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

          # Daten aufteilen für Modellierung
          st.subheader("🎯 Step 6: Train/Test Split + Target Balance")

          y = newdf['target'].copy().astype(int)
          X = newdf.drop(["y", "target",  "year", "date_int", 'date_period'], axis=1).copy()

          from sklearn.model_selection import train_test_split
          X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

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
