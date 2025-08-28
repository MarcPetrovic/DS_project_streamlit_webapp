import streamlit as st
from utils.image_loader import show_github_image
import pandas as pd
import matplotlib.pyplot as plt
from utils.plotting import plot_cat_distribution_vs_success
from spa_config import spa_plot_map
from utils.data_loader import load_csv_data
import io
from utils.modelling_feature_engineering import build_modelling_pipeline
import graphviz
from sklearn import set_config
from sklearn.utils import estimator_html_repr
from utils.summary_stats import summary
from utils.my_colormaps import my_cmap_r
from bs4 import BeautifulSoup
import re
#from feature_engine.creation import CyclicalFeatures
from utils.cyclical_encoder import CyclicalEncoder

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
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
        show_github_image(
        image_filename="images/modelling_spa_fe_dp.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=("Figure 24: Overview of the transition from Success Profile Analysis to concrete feature \n"
                 "transformations and their implementation in modular processing steps within the \n"
                 "modeling phase.")
        )
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

        """, unsafe_allow_html=True)
        show_github_image(
        image_filename="images/feature_construction_tool_spa.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=("Figure 25: Relevant aspects and important stakeholders of the feature construction tool SPA.\n"
                 " "
                )
        )
        st.markdown("""
        
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

        """, unsafe_allow_html=True)
        show_github_image(
        image_filename="images/intro_spa.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption="Figure 26: Introduction to Success Profile Analysis"
        )
        st.markdown("""
        
        This visualization approach plays a central role in translating raw variables into analytically meaningful features. 
        For instance, continuous variables such as the employment index (nr.employed) were segmented into interpretable bins 
        using domain-informed cut points. These segments were then evaluated regarding their respective success rates. 
        Graphical examples (cf. integrated illustrations) highlight how these groupings expose non-linear behaviors and 
        inform the selection of modeling-relevant intervals.

        """, unsafe_allow_html=True)
        show_github_image(
        image_filename="images/dummy_coding_spa.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption="Figure 27: Application of dummy coding based on Success Profile Analysis"
        )
        st.markdown("""
        
        Based on the observed patterns, variables were categorized into transformation strategies. Binary recoding via dummy 
        coding was employed where one specific category (e.g., 'success' in the poutcome variable) exhibited a significantly 
        elevated success rate. In contrast, more complex relationships were captured using effect coding, where multiple 
        categories were grouped into +1/0/−1 schemes to reflect directional impact (e.g., in job, education, or age).

        These transformations were operationalized via custom transformer classes inheriting from BaseEstimator and 
        TransformerMixin. The use of modular transformation classes ensured reproducibility and clear traceability of applied 
        rules. All transformations were ultimately structured within Pipeline objects to ensure compatibility with the broader 
        machine learning workflow.
        
        """, unsafe_allow_html=True)
        show_github_image(
        image_filename="images/effect_coding_spa.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption="Figure 28: Application of effect-coding based on Success Profile Analysis"
        )
        def load_data():
            X_train = pd.read_csv("data/X_train.csv", index_col=0)
            y_train = pd.read_csv("data/y_train.csv", index_col=0).squeeze("columns")
            return X_train, y_train

        X_train, y_train = load_data()

        # Feature-Auswahl
        st.markdown("### Select a feature for Success Profile Analysis")
        feature_name = st.selectbox("Choose a variable", list(spa_plot_map.keys()))

        # Parameter holen
        config = spa_plot_map[feature_name]
        feature = config["feature"]
        bins = config.get("bins")
        title = config.get("title")
        map_bins = config.get("map_bins")

        # Plot anzeigen
        plot_cat_distribution_vs_success(X_train, y_train, feature=feature, bins=bins, title=title, map_bins=map_bins)

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
        st.markdown("""
        Sometimes, users may wish to understand the technical foundation of the preprocessing steps. Tick the checkbox 
        below to dive into the full technical pipeline implementation.
        """)
        show_processing = st.checkbox("Show modelling feature engineering processing steps")
        if show_processing:
          st.subheader("📂 Step 1: Load X_train Data")
      
          df = load_csv_data(
              filename="data/X_train.csv",
              sep=",",
              header=True,
              add_row_id=False
          )
      
          st.success("CSV file X_train loaded successfully.")
          st.write(df.head())
        
          st.subheader("📂 Step 2: Load X_test Data")
          X_test = load_csv_data(
              filename="data/X_test.csv",
              sep=",",
              header=True,
              add_row_id=False
          )       
            
          st.success("CSV file X_test loaded successfully.")
          st.write(X_test.head())
            
          st.subheader("🔄 Step 3: Apply processing Pipeline")
      
          processor = build_modelling_pipeline(df)  # Custom-built scikit-learn pipeline
          set_config(display='diagram')
          html_code2 = estimator_html_repr(processor)
          # BeautifulSoup initialisieren
          soup2 = BeautifulSoup(html_code2, 'html.parser')
          
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
          
          for style_tag in soup2.find_all("style"):
              style_text = style_tag.string
              if style_text:
                  for var_name, new_color in color_variable_mapping.items():
                      style_text = style_text.replace(var_name + ": ", f"{var_name}: {new_color}; /* replaced */ ")
                  style_tag.string.replace_with(style_text)
          
          st.components.v1.html(str(soup2), height=450, width=1200, scrolling=True) 

          processor.set_output(transform='pandas')
          X_train_transformed2nd = processor.fit_transform(df)
          X_test_transformed2nd = processor.transform(X_test)
      
          def make_streamlit_arrow_compatible(df: pd.DataFrame) -> pd.DataFrame:
              df = df.convert_dtypes()
              for col in df.select_dtypes(include='object').columns:
                  df[col] = df[col].apply(lambda x: str(x) if not pd.isna(x) else "")
              return df
      
          X_train_transformed2nd = make_streamlit_arrow_compatible(X_train_transformed2nd)
          X_test_transformed2nd = make_streamlit_arrow_compatible(X_test_transformed2nd)
          st.success("Data transformed successfully.")
      
          st.subheader("📋 Step 4: DataFrame Info After Transformation")
          buffer = io.StringIO()
          X_train_transformed2nd.info(buf=buffer)
          st.text("🧾 X_train_transformed2nd.info():")
          st.text(buffer.getvalue())
            
          buffer2 = io.StringIO()
          X_test_transformed2nd.info(buf=buffer2)
          st.text("🧾 X_test_transformed2nd.info():")
          st.text(buffer2.getvalue())
          
          st.subheader("⚙️ Step 5: CyclicalFeatures Transformation")
          #from feature_engine.creation import CyclicalFeatures
          cyclical_features = CyclicalEncoder(variables=['month_numeric', 'day_of_week_numeric'], 
                                     drop_original=True)
          X_train_transformed2nd = cyclical_features.fit_transform(X_train_transformed2nd)
          X_test_transformed2nd = cyclical_features.transform(X_test_transformed2nd)
          X_train_transformed2nd = make_streamlit_arrow_compatible(X_train_transformed2nd)
          X_test_transformed2nd = make_streamlit_arrow_compatible(X_test_transformed2nd)
          st.success("Model data processing complete.")
          st.write("✅ Dimensions of the training set:", X_train_transformed2nd.shape)
          st.write("✅ Dimensions of the test set:", X_test_transformed2nd.shape)

    
    if task == "Summary of the modelling phase & transition to evaluation phase":
        st.subheader("5. Summary of the modelling phase & transition to evaluation phase")
        st.markdown("""
        The modeling phase served as a pivotal component in translating exploratory data analysis (EDA) into structured, 
        model-ready input features, thereby laying the foundation for robust predictive modeling. In alignment with the 
        CRISP-DM methodology, this phase emphasized both methodological rigor and business interpretability by combining 
        visual diagnostic tools with technically sound feature transformation processes.

        A central element of this phase was the application of the Success Profile Analysis (SPA), which allowed for a 
        targeted examination of feature-target relationships. By leveraging SPA, we identified key variables that exhibited 
        statistically significant deviations from the average success rate. These insights were used to systematically 
        segment the data in a manner that enhanced both predictive accuracy and interpretability.
        
        """, unsafe_allow_html=True)
        show_github_image(
        image_filename="images/2nd_iteration_modelling.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption="Figure 29: Single steps of second iteration modelling phase."
        )
        st.markdown("""
        
        The operationalization of SPA insights into model-ready features was realized through a series of custom-built 
        preprocessing pipelines. These included both dummy encoding (binary flagging of dominant categories) and effect 
        coding (grouping of semantically coherent segments based on their relative outcome performance). Each transformation 
        step was encapsulated within a custom transformer class that adheres to the scikit-learn API, ensuring full 
        compatibility with subsequent model tuning and evaluation workflows. This modular approach not only supported 
        traceability and reuse, but also allowed for seamless integration into grid search, model export, and deployment 
        contexts.

        By the end of this modeling phase, we obtained a fully preprocessed dataset in which structural, semantic, and 
        statistical considerations were coherently embedded. The resulting feature set is both robust and interpretable, 
        striking a balance between machine-learned insight and domain-relevant structure.

        In the following evaluation phase, we transition from data representation to model assessment. Two classification 
        algorithms will be compared: Logistic Regression and XGBoost. These were chosen to reflect the dual objective of the 
        project—balancing interpretability with predictive power. Furthermore, we will explore four different threshold 
        optimization strategies to assess model calibration and business alignment under various decision-making criteria. 

        """, unsafe_allow_html=True)
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
