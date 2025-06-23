import streamlit as st
from utils.image_loader import show_github_image
from utils.data_loader import load_csv_data
import pandas as pd
import numpy as np

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
  # Dropdown für die Phasen
    task = st.selectbox("Select a subchapter of CRISP-DM-phase Data Understanding:", [
        "General Procedere & EDA",
        "Instructions Primary Researcher",
        "Data Audit - Client Socio-Economic Attributes",
        "Data Audit - Economic Environment",
        "Data Audit - Current Marketing Activities",
        "Data Audit - Previous Marketing Activities",
        "Data Audit - Target Feature",
        "Key Findings of the 2nd Phase"
    ])

    # Inhalte je nach Auswahl
    if task == "General Procedere & EDA":
        st.subheader("1. General Procedere & Exploratory Data Analysis")
        st.markdown("""
        As already mentioned in the first section of the third chapter of this research project paper, data was not 
        collected independently, but secondary data was used in the empirical part of the study. The dataset used, 
        entitled *“Bank Marketing (with social/economic context)”*, is freely available to secondary researchers in 
        the machine learning repository of the University of California, Irvine (UCI), at the following link: <a href="http://archive.ics.uci.edu/ml/datasets/Bank+Marketing" target="_blank">http://archive.ics.uci.edu/ml/datasets/Bank+Marketing</a>.
        The data basis of the project was collected from a Portuguese bank that used its own contact-center to do 
        directed marketing campaigns. The telephone, with a human agent as the interlocutor, was the dominant marketing 
        channel. The dataset collected is related to 17 campaigns that occurred between May 2008 and November 2010, 
        corresponding to a total of 41,188 contacts. During these phone campaigns, an attractive long-term deposit 
        application, with good interest rates, was offered to the bank customers (hot flow). For each contact, a large 
        number of attributes were stored (see in detail Tables 2-5) and if there was a subscription to term deposit 
        (the target/response variable). For the whole database considered, there were 4,640 successes (11.3% success rate). 
        The data set was supplemented by five nationwide socio-economic indicators, which are published by Banco de 
        Portugal and are publicly available (see link: <a href="https://bpstat.bportugal.pt/" target="_blank">https://bpstat.bportugal.pt/</a>).
        """, unsafe_allow_html=True)
          # Bild von der URL laden und anzeigen 
        show_github_image(
        image_filename="images/da_general_procedere_data_basis.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 8: Overview of the data basis of the AI project")
        )
        st.markdown("""
        Within the second phase of CRISP-DM, the primary objective is to understand the data, especially its structure 
        and quality. Before initiating the data audit—a critical sub-step within this phase—this study takes into account 
        the advices and documentation provided by the primary researchers who collected and curated the dataset. These 
        recommendations provide essential context for understanding variable meanings, data encoding, and known data 
        quality issues, and are therefore instrumental in designing a meaningful audit process.

        The data audit structures the available data sample based on various properties. For example, a distinction is 
        made between dependent and independent variables. The data type of each attribute is identified, and the relevant 
        value ranges (feature domains) are listed. A central concern of the audit is to detect missing values and, 
        depending on the data type and contextual relevance, to apply representative and statistically sound procedures 
        for their treatment.

        """)
          # Bild von der URL laden und anzeigen 
        show_github_image(
          image_filename="images/attribute_cluster.PNG",
          repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
          caption=( "Figure 9: Overview of the four data type clusters within the used database")
          )
        st.markdown("""
        Figure 9 shows that the available dataset can be broadly categorized into four feature clusters. These clusters 
        are examined in detail in the following subsections. First, a general definition and categorization of each 
        cluster’s features is presented. Subsequently, an exploratory, descriptive data analysis is conducted, focusing 
        on data distributions, patterns, and completeness. This enables the identification of missing values and informs 
        the selection of suitable imputation or transformation methods in alignment with the industrial CRISP-DM methodology.

        The chapter concludes with a comprehensive summary of key results and derived recommendations for subsequent phases 
        of data (pre-)processing. These insights serve as a foundational basis for the Data Preparation phase that follows.
        """)
    elif task == "Instructions Primary Researcher":
        st.subheader("2. Consideration of primary researchers' advices")
        st.markdown("""
        Before conducting a structured data audit within the second phase of CRISP-DM, it is essential to consider the contextual 
        information and methodological recommendations provided by the primary researchers who originally compiled and analyzed 
        the dataset. The dataset used in this project—bank-additional-full.csv—is a refined version of the original Bank Marketing 
        dataset, extended by five nationwide socio-economic indicators. It was developed by Sérgio Moro (ISCTE-IUL), Paulo Cortez 
        (University of Minho), and Paulo Rita (ISCTE-IUL), and has been publicly released via the UCI Machine Learning Repository.

        The primary source for contextual and methodological guidance is the publication by Moro et al. (2014), titled “A Data-Driven 
        Approach to Predict the Success of Bank Telemarketing”, published in Decision Support Systems (Moro et al., 2014). The researchers 
        emphasize that the dataset includes 41,188 instances collected between May 2008 and November 2010, each representing a client 
        contact within a telemarketing campaign aimed at promoting a long-term deposit product.
        <br>
        """, unsafe_allow_html=True)
          # Bild von der URL laden und anzeigen 
        show_github_image(
        image_filename="images/instructions_primary_researcher.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 10: Main advices of the primary researchers")
        )
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
        st.markdown("""
        These insights and methodological advices form an essential foundation for the subsequent steps in the Data Understanding 
        phase. They ensure that decisions made during the audit and preprocessing stages are both informed by domain knowledge and 
        aligned with best practices established in prior peer-reviewed research.
        <br>
        """, unsafe_allow_html=True)
        st.write("""
        Taking into account the advices of the primary researchers in general, and in particular by adjusting the 
        categorical variables by converting the expression “unknown” into NaN (missing value), the data set used is 
        presented and analyzed in the following subsections for the respective data clusters (data audit). 
        The report used in the exploratory data analysis was automatically generated with 
        [YData Profiling](https://github.com/ydataai/ydata-profiling) and provides a comprehensive overview of the data 
        quality, distributions and correlations.
        """)
        st.markdown("""
        <a href="https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html" target="_blank">
            📊 Open Profiling Report 
        </a>
        """, unsafe_allow_html=True)

    elif task == "Data Audit - Client Socio-Economic Attributes":
        st.subheader("3. Data Audit - Client Socio-Economic Attributes")
        st.markdown("""
        The first cluster of variables includes, on the one hand, socio-economic characteristics of the bank customers, such as 
        information on any loan agreements, real estate financing and whether the customer has a non-performing loan. On the other 
        hand, the first cluster of variables contains socio-demographic characteristics of the bank customers, including age, job, 
        marital status and level of education at the time of the telephone interview. Table 2 provides a good overview of certain 
        characteristics of the features of the first cluster. It shows the name of the characteristic in the dataset (e.g. age), 
        the data type (continuous or categorical), a brief description of the bank customer characteristics (e.g. for age: “age at 
        time of contact”), the value range of the characteristics (e.g. for age between 17 and 98 years) and the model type 
        (independent variable or target).
        """)
        df2 = load_csv_data(
          filename="data/bank-additional-full.csv",
          sep=";",
          header=True,
          add_row_id=True
        )
        st.write("✅ DEBUG: CSV loaded – Shape:", df2.shape)
        #st.dataframe(df2.head())  

        attribute_metadata = [
          {
            "ATTRIBUTE NAME": "age",
            "ATTRIBUTE DATA TYPE": "Continuous",
            "ATTRIBUTE DESCRIPTION": "Age at the contact date",
            "ATTRIBUTE DOMAIN VALUE": "[17, 98]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Client socio-economic attributes"
          },
          {
            "ATTRIBUTE NAME": "job",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "Clients type of job",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df2["job"].dropna().unique())),
           # "ATTRIBUTE DOMAIN VALUE": "<ul>" + "".join(
           #   f"<li>{val}</li>" for val in sorted(df2["job"].dropna().unique())
           # ) + "</ul>",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Client socio-economic attributes"
          },
          {
            "ATTRIBUTE NAME": "marital",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "Clients Marital Status at time of call",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df2["marital"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Client socio-economic attributes"
          },
          {
            "ATTRIBUTE NAME": "education",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "Clients educational background at time of call",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df2["education"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Client socio-economic attributes"
          },
          {
            "ATTRIBUTE NAME": "default",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "If the client has a credit in default",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df2["default"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Client socio-economic attributes"
          },
          {
            "ATTRIBUTE NAME": "housing",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "If the client has a house loan contract",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df2["housing"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Client socio-economic attributes"
          },
          {
            "ATTRIBUTE NAME": "loan",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "If the client has a house loan contract",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df2["loan"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Client socio-economic attributes"
          }
        ]
        metadata_df = pd.DataFrame(attribute_metadata)

        def render_html_table(df: pd.DataFrame) -> str:
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
                td ul {
                    padding-left: 20px !important;
                    margin: 0 !important;
                }
                td li {
                    margin-bottom: 3px !important;
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
                    if isinstance(cell, str) and cell.strip().startswith("<ul>"):
                        html += f"<td>{cell}</td>"  # HTML anzeigen
                    else:
                        html += f"<td>{str(cell)}</td>"  # Normaler Text
                html += "</tr>"
        
            html += "</tbody></table>"
            return html
        html_table = render_html_table(metadata_df)

        st.subheader("Table 2: Overview Client Socio-Economic Attributes")
        #scrollable_html = f"""<div style='height: 400px; overflow-y: auto; border: 1px solid #ccc; padding: 10px'>{html_table}</div>"""
        #st.markdown(scrollable_html, unsafe_allow_html=True)
        st.markdown(html_table, unsafe_allow_html=True)

        st.markdown("""
        <br><br>
        The “Age” characteristic is a metric (continuous) variable that records the customer’s age at the time of 
        the telephone contact. The variable contains no missing values and shows a broad age distribution ranging 
        from 17 to 98 years. The median age is 38, while the mean is slightly higher at 40.0 years, indicating a 
        slight right skew (skewness = 0.78). The standard deviation is 10.42, and the interquartile range (IQR) is 
        15 years, reflecting moderate variability within the customer base. The 95th percentile is at 58 years, 
        suggesting that most customers fall within a working-age range, with relatively few very young or elderly 
        individuals.

        From a marketing and modeling perspective, age is expected to correlate with financial behavior and risk 
        preferences. Middle-aged and older customers may be more likely to subscribe to term deposits, due to a 
        greater focus on financial security and long-term savings. Younger customers, by contrast, may show less 
        interest in such products, either due to lower income levels or a higher preference for liquidity. Given 
        its wide distribution and complete data coverage, the age variable offers strong potential as a predictor 
        in modeling customer decisions regarding fixed-term deposit subscriptions.

        The “Job” characteristic describes the professional status of the bank customers contacted by telephone. 
        Overall, it can be seen that a large proportion of the sample consists of people with administrative jobs: 
        with 10,422 cases, admin occupations make up the largest proportion (25.3 %). This is followed by blue-collar 
        occupations (manual/industrial) with 9,254 cases (22.5 %) and technicians with 6,743 cases (16.4 %). Other 
        frequently represented groups are services (9.6 %) and management (7.1 %). Pensioners (retired, 4.2 %) and 
        people with self-employed or entrepreneurial activities (entrepreneur, self-employed, 3.5 % each) are 
        comparatively underrepresented. The categories housemaid (2.6 %) and unemployed (2.5 %) have the lowest number 
        of cases. Overall, there is a broad occupational spread with a focus on administrative and non-academic 
        professions.

        It should also be mentioned that 330 cases (around 0.8 %) have missing values in the “Job” characteristic. 
        In industrial data mining projects, missing values are often dealt with pragmatically, especially if the 
        proportion is relatively low. It is therefore planned to replace these missing values with the mode, i.e. 
        the most frequent category (admin), in the subsequent data preparation phase (phase 3 of the CRISP-DM model). 
        This procedure enables complete use of the data sets without any significant distortion of the distribution. 
        From a modeling perspective, it is expected that job type may influence financial behavior, with certain 
        groups—such as management, technicians, or pensioners—potentially showing a higher likelihood of subscribing 
        to a term deposit due to more stable income sources, risk aversion, or stronger financial planning habits.

        The “Marital” characteristic records the marital status of the bank customers contacted. The distribution 
        shows that the majority of the sample is classified as married - with 24,928 cases, this corresponds to 60.5% 
        of the total sample. In second place are single (single) with 11,568 cases (28.1%), followed by divorced 
        (divorced) with 4,612 cases (11.2%). This distribution suggests a majority of stable customers, which could 
        be relevant for certain marketing measures (e.g. in relation to savings or investment products).

        In addition, 80 missing values (0.2 %) were identified in the “Marital” characteristic. In line with established 
        practice in industrial data mining projects, a pragmatic approach to missing values is also taken here. Due to 
        the very low proportion, it is planned to replace the missing values in the third CRISP-DM phase (Data Preparation) 
        with the mode - i.e. the most frequent characteristic (married). This ensures data completeness without significant 
        distortion of the distribution.

        The “Education” characteristic describes the highest level of education completed by each bank customer, based on 
        the structure of the Portuguese education system. The distribution is relatively broad, with the largest group 
        holding a university degree (12,168 cases, 29.5 %), followed by high school graduates (9,515 cases, 23.1 %). A 
        significant share of the sample completed only basic education: 14.7 % with 9 years of schooling (basic.9y), 
        10.1 % with 4 years (basic.4y), and 5.6 % with 6 years (basic.6y). These categories reflect the three cycles of 
        Portugal’s basic education system. Additional groups include vocational training graduates (professional.course, 
        12.7 %) and a very small number of illiterate individuals (<0.1 %). The observed distribution suggests a diverse 
        customer base in terms of educational background, which may influence financial decision-making and product 
        preferences.

        From a marketing and predictive modeling perspective, a positive correlation is expected between higher education 
        levels and the likelihood of subscribing to a term deposit. Customers with university or professional education 
        may exhibit greater financial literacy, long-term planning behavior, and awareness of investment products. 
        Therefore, education could serve as a relevant predictor for identifying customer segments more inclined toward 
        fixed-term savings products. The variable also includes 1,731 missing values (4.2 %), which will be imputed with 
        the mode (university.degree) during the Data Preparation phase, in line with common data mining practices.
        <br>
        """, unsafe_allow_html=True)
        anchor_map = {
          "age": "pp_var_5630436754821285116",
          "job": "pp_var_-2855576533511057154",
          "marital": "pp_var_-2655159898856749981",
          "education": "pp_var_3871473053277162198"
        }

        selected_var = st.selectbox("🔍 Select a socio-demographic feature to replicate above mentioned analysis", list(anchor_map.keys()))

        url = f"https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing_scaled.html#{anchor_map[selected_var]}"

        st.components.v1.iframe(src=url, height=600, width=800, scrolling=True)

        st.markdown("""
        The “Default” characteristic is a dichotomous variable indicating whether the bank customer had a credit in 
        default at the time of the telephone contact. The vast majority of customers (32,588 cases, 79.1 %) were not 
        in default, while only 3 cases (<0.1 %) were explicitly marked as being in default. A relatively large proportion 
        of entries (8,597 cases, 20.9 %) are missing. This high proportion of missing values must be addressed during 
        data preparation.

        Due to the extreme class imbalance and the very low number of observed “True” cases, it is recommended to 
        merge the missing values with the “True” category. From a conservative risk assessment perspective, the 
        absence of information in this context may suggest higher credit risk or lower transparency—both of which 
        are relevant indicators in financial modeling. This recoding approach is commonly used in industrial data 
        mining when a variable may reflect underlying risk through both observed and unobserved (missing) states, 
        and ensures the variable remains useful in predictive modeling without distorting its binary structure.

        The “Housing” characteristic is a dichotomous variable indicating whether the customer has an active housing 
        loan at the time of contact. In the sample, the majority of customers (21,576 cases, 52.4 %) reported having 
        a housing loan, while 18,622 cases (45.2 %) indicated they do not have such a loan. A small proportion of 990 
        cases (2.4 %) are missing and will require imputation during data preparation.

        From a financial behavior perspective, having a housing loan typically reflects a significant long-term 
        financial commitment. Customers with a housing loan might exhibit different risk profiles and saving habits 
        compared to those without, which could influence their propensity to subscribe to fixed-term deposit products. 
        For instance, customers with housing loans may prioritize debt servicing, while those without might have more 
        disposable income available for savings or investments. Given the relatively low number of missing values, it 
        is planned to impute these with the mode category (“True”) to maintain data completeness without distorting 
        the overall distribution.

        The “Loan” characteristic is a dichotomous variable indicating whether the client has an individual credit 
        contract at the time of contact. The majority of customers (33,950 cases, 82.4 %) do not have such a credit 
        contract, while 6,248 cases (15.2 %) are marked as “True,” indicating they currently hold an individual loan. 
        There are 990 missing values (2.4 %) that will need to be addressed during data preparation.

        From a financial behavior and risk perspective, having an individual loan signals an existing financial 
        obligation that may influence the customer’s saving and investment decisions. Customers with loans might show 
        a different propensity to subscribe to term deposits compared to those without, potentially due to differences 
        in disposable income or financial priorities. Given the relatively small share of missing data, these values 
        are planned to be imputed using the mode (“False”) to ensure data completeness while preserving the distribution 
        for subsequent analysis.

        in the following second section of the data audit, the macroeconomic variables (economic & social environment) 
        are discussed in more detail.
        """)
        
        anchor_map2 = {
          "default": "pp_var_3783804538312100998",
          "housing": "pp_var_-7580748235938891539",
          "loan": "pp_var_6909794517524857854"
        }

        selected_var2 = st.selectbox("🔍 Select a socio-economic feature to replicate above mentioned analysis", list(anchor_map2.keys()))

        url2 = f"https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html#{anchor_map2[selected_var2]}"

        #st.components.v1.iframe(src=url2, height=600, width=700, scrolling=True)
        st.markdown(f"""
            <style>
                /* Webkit (Chrome, Safari, Edge) Scrollbar */
                div.custom-scroll::-webkit-scrollbar {{
                    width: 16px;
                }}
                div.custom-scroll::-webkit-scrollbar-track {{
                    background: #f1f1f1;
                }}
                div.custom-scroll::-webkit-scrollbar-thumb {{
                    background: #888;
                    border-radius: 8px;
                }}
                div.custom-scroll::-webkit-scrollbar-thumb:hover {{
                    background: #555;
                }}
        
                /* Optional: Firefox */
                div.custom-scroll {{
                    scrollbar-width: thin;
                    scrollbar-color: #888 #f1f1f1;
                }}
            </style>
            <div class="custom-scroll" style="transform: scale(0.8); transform-origin: top left; width: 875px; height: 750px; overflow: auto;">
                <iframe src="{url2}" width="1093" height="938" style="border:none"; scrolling="yes"></iframe>
            </div>
        """, unsafe_allow_html=True)

    elif task == "Data Audit - Economic Environment":
        st.subheader("4. Data Audit - Economic Environment")
        st.markdown("""
        The second cluster of variables captures the broader economic and social environment at the time of customer 
        contact. Unlike the first cluster, which focuses on individual customer characteristics, this set of variables 
        reflects the macroeconomic conditions in Portugal, such as labor market dynamics, consumer sentiment, and 
        interest rate levels. These continuous variables were recorded at different temporal frequencies (monthly, 
        quarterly, or daily) and serve as contextual background for interpreting customer behavior. They are external 
        to the customer but may influence financial decision-making—particularly with regard to long-term financial 
        products such as term deposits. Table 3 provides an overview of the features in this cluster, including 
        variable names, descriptions, and domain values.
        """)
        attribute_metadata_macro = [
          {
            "ATTRIBUTE NAME": "emp.var.rate",
            "ATTRIBUTE DATA TYPE": "Continuous",
            "ATTRIBUTE DESCRIPTION": "Employment variation rate, with a quarterly frequency",
            "ATTRIBUTE DOMAIN VALUE": "[-3.40, 1.40]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Economic & social environment"
          },
          {
            "ATTRIBUTE NAME": "cons.price.idx",
            "ATTRIBUTE DATA TYPE": "Continuous",
            "ATTRIBUTE DESCRIPTION": "Monthly average consumer price index",
            "ATTRIBUTE DOMAIN VALUE": "[92.2010, 94.7670]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Economic & social environment"
          },
          {
            "ATTRIBUTE NAME": "cons.conf.idx",
            "ATTRIBUTE DATA TYPE": "Continuous",
            "ATTRIBUTE DESCRIPTION": "Monthly average consumer confidence index",
            "ATTRIBUTE DOMAIN VALUE": "[-50.80, -26.90]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Economic & social environment"
          },
          {
            "ATTRIBUTE NAME": "euribor3m",
            "ATTRIBUTE DATA TYPE": "Continuous",
            "ATTRIBUTE DESCRIPTION": "Daily three month Euribor rate",
            "ATTRIBUTE DOMAIN VALUE": "[0.6340, 5.0450]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Economic & social environment"
          },
          {
            "ATTRIBUTE NAME": "nr.employed",
            "ATTRIBUTE DATA TYPE": "Continuous",
            "ATTRIBUTE DESCRIPTION": "Quarterly average of the total number of employed citizens",
            "ATTRIBUTE DOMAIN VALUE": "[4963.60, 5228.10]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Economic & social environment"
          }
        ]
        metadata_macro_df = pd.DataFrame(attribute_metadata_macro)
        
        def render_html_table2(df: pd.DataFrame) -> str:
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
                td ul {
                    padding-left: 20px !important;
                    margin: 0 !important;
                }
                td li {
                    margin-bottom: 3px !important;
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
                    if isinstance(cell, str) and cell.strip().startswith("<ul>"):
                        html += f"<td>{cell}</td>"  # HTML anzeigen
                    else:
                        html += f"<td>{str(cell)}</td>"  # Normaler Text
                html += "</tr>"
        
            html += "</tbody></table>"
            return html
        
        html_table_macro = render_html_table2(metadata_macro_df)

        st.subheader("Table 3: Overview of feature-cluster socio-economic-environment")
        st.markdown(html_table_macro, unsafe_allow_html=True)

        st.markdown("""
        <br>
        The variable emp.var.rate reflects the quarterly change in the employment rate in Portugal at the time of 
        the bank’s telephone contact with the customer. It is a continuous variable that serves as a proxy for the 
        health of the labor market. The distribution shows several dominant values, as the variable appears to have 
        been discretized into a limited number of economically relevant states.

        The most frequent value is 1.4 (16,234 cases, 39.4 %), followed by 1.1 (7,763 cases, 18.8 %), and -1.8 
        (9,184 cases, 22.3 %). These values suggest that a substantial portion of the dataset was collected during 
        periods of slight to moderate employment growth, but also during a noticeable downturn (−1.8). Smaller groups 
        fall into strongly negative labor market phases such as −2.9, −3.0, and −3.4, together accounting for about 
        7 % of the data. Positive employment variation values tend to signal economic recovery or expansion, while 
        negative values correspond to downturns or recessions.

        From a modeling perspective, it is expected that the employment variation rate influences customers’ financial 
        behavior by shaping their perception of economic security. Interestingly, this relationship may be negative in 
        the context of fixed-term deposits: during periods of positive employment development (e.g. rising emp.var.rate), 
        customers may feel more confident about their financial future and therefore be less inclined to lock in capital 
        in conservative products like term deposits. Instead, they might prefer more flexible or higher-yielding 
        investment options. Conversely, in times of rising unemployment or economic downturns, fixed-term deposits may 
        be perceived as a safer choice, increasing their appeal. The variable thus captures an important aspect of the 
        macroeconomic environment that may indirectly influence product demand.

        The variable cons.price.idx represents the monthly average of the consumer price index (CPI) at the time of 
        customer contact. It is a continuous variable, measured on a metric scale, and serves as an indicator of 
        inflationary dynamics in the economy. In total, the variable contains 26 distinct values, with no missing or 
        infinite entries, and thus offers full data coverage. The CPI values in the dataset range from 92.201 to 94.767, 
        with a mean of 93.58 and a standard deviation of 0.58. The interquartile range (IQR) is relatively narrow at 
        0.919, indicating that most observations lie close to the central tendency. The distribution shows slight 
        left-skewness (−0.23) and mild platykurtic characteristics (kurtosis = −0.83), meaning that values are more 
        evenly spread across the range with less concentration around the mean.

        Although the variable is metric, the distribution is multimodal, as a limited number of CPI values occur with 
        particularly high frequency—reflecting the temporal aggregation of macroeconomic conditions. For example, values 
        such as 93.994 (18.8 %), 93.918 (16.2 %), and 92.893 (14.1 %) are clearly overrepresented, likely corresponding 
        to periods of data collection with stable or repeat economic conditions.

        From an economic perspective, the CPI reflects changes in the general price level and is closely linked to 
        inflation expectations and household purchasing power. Notably, all values in the dataset lie below the normalized 
        base index of 100, indicating a generally low inflationary environment during the observation period. In this 
        context, a moderate increase in the CPI may be perceived as a sign of emerging inflation or economic uncertainty, 
        which in turn can strengthen the appeal of safe and predictable investments such as fixed-term deposits. Customers 
        may seek to protect the value of their assets against future price increases, especially when variable-yield 
        alternatives are viewed as riskier. Therefore, in contrast to typical high-inflation scenarios, a positive 
        correlation between CPI and the likelihood of term deposit subscription is plausible in this specific low-index 
        context. The cons.price.idx variable thus provides valuable insight into how macroeconomic price expectations 
        shape customer preferences for secure investment products.
        """, unsafe_allow_html=True)
        anchor_map_macro = {
          "emp.var.rate": "pp_var_1742109992004542320",
          "cons.price.idx": "pp_var_3908269255914349566"
        }

        selected_var_macro = st.selectbox("🔍 Select a macro-economic feature to replicate above mentioned analysis", list(anchor_map_macro.keys()))

        url_macro = f"https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html#{anchor_map_macro[selected_var_macro]}"

        #st.components.v1.iframe(src=url_macro, height=600, width=700, scrolling=True)
        st.markdown(f"""
            <div style="transform: scale(0.8); transform-origin: top left; width: 875px; height: 750px; overflow: auto;">
                <iframe src="{url_macro}" width="1093" height="938" style="border:none"; scrolling="yes"></iframe>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        The variable cons.conf.idx represents the monthly average of the consumer confidence index, a metric indicator that 
        reflects the sentiment of consumers regarding the overall economic outlook and their personal financial expectations. 
        It is a continuous variable with 26 distinct values, no missing or infinite entries, and is exclusively negative in 
        this dataset. The values range from −50.8 to −26.9, with a mean of −40.50 and a median of −41.8. The standard deviation 
        is 4.63, and the interquartile range (IQR) is 6.3, which indicates moderate dispersion.

        Although the histogram suggests a left-skewed distribution visually, the calculated skewness of +0.30 reveals a slight 
        right-skew on a technical level, meaning there is a tail toward less negative (i.e. relatively more optimistic) values. 
        The overall shape of the distribution is mildly platykurtic (kurtosis = −0.36), suggesting flatter peaks and a wider 
        spread of values. The variable is not monotonic and shows several distinct modes. For instance, values such as −36.4 
        (18.8 %), −42.7 (16.2 %), and −46.2 (14.1 %) are highly frequent, reflecting repeated data collection during periods 
        of relatively low consumer confidence.

        From a behavioral and economic perspective, the consumer confidence index plays a significant role in influencing 
        household saving and investment decisions. In this dataset, all observed values are negative, indicating a period of 
        generally low consumer sentiment. However, rising values within the negative range can be interpreted as a signal of 
        gradual recovery in confidence. In such transitional phases, consumers may feel more secure in their personal financial 
        situation—but often not secure enough to shift toward riskier investments. Instead, fixed-term deposits are perceived 
        as a safe yet predictable investment option, offering capital protection and financial stability. Therefore, a positive 
        correlation between moderately rising CCI values and the likelihood of term deposit subscription is plausible. The 
        cons.conf.idx variable thus provides valuable insights into how subtle shifts in macroeconomic sentiment influence 
        customer behavior, particularly in times of uncertainty.

        The variable euribor3m captures the daily value of the three-month Euribor (Euro Interbank Offered Rate) at the time 
        of customer contact. It is a continuous metric variable and an important macro-financial indicator reflecting short-term 
        interest rates within the Eurozone. The dataset includes 316 distinct values, covering a range from 0.634 to 5.045 with 
        no missing or negative values. The mean is 3.62, while the median is considerably higher at 4.86, indicating a left-skewed 
        distribution (skewness = −0.71). This skewness reflects the relatively longer time spent in low-interest environments, 
        followed by a sharper increase toward the end of the observation period.

        The interquartile range (IQR) is relatively large at 3.62, and the standard deviation is 1.73, both pointing to substantial 
        variability in interest rates over time. While the distribution includes a broad range of values, it is concentrated around 
        certain high-frequency points such as 4.857 (7.0 %), 4.962 (6.3 %), and 4.963 (6.0 %), reflecting recurring rate levels 
        during specific periods of customer contact. The data is not monotonic, which aligns with the typical volatility of daily 
        market rates.

        From an economic perspective, the Euribor rate is a key benchmark for short-term interest rates in the Eurozone and 
        directly influences both the general interest level and consumer behavior regarding savings products. At first glance, 
        one might assume a positive correlation between rising Euribor values and the likelihood of subscribing to fixed-term 
        deposits, since higher interest levels increase the nominal return on such products, thereby enhancing their 
        appeal—especially to yield-sensitive investors.

        However, in the specific context of this dataset—covering the years 2008 to 2010, during and after the global financial 
        crisis—a different dynamic may be at play. In this period, sharp drops in the Euribor rate were often associated with 
        economic stress, monetary interventions by the European Central Bank, and a general sense of uncertainty. Even though 
        interest rates fell to historic lows, the demand for secure and predictable financial products like fixed-term deposits 
        often increased, driven by a heightened need for capital preservation and stability. From this perspective, a negative 
        correlation between the Euribor and term deposit subscriptions is also plausible: as the Euribor falls in response to 
        crisis conditions, customers may turn to low-risk investment forms despite unattractive returns. This dual perspective 
        highlights the importance of interpreting macro-financial indicators not in isolation, but in the context of prevailing 
        economic sentiment and behavioral responses.

        The characteristic “number employed” represents the quarterly average of the total number of employed citizens within 
        the relevant economic context. This continuous variable exhibits a relatively narrow range between 4,963.6 and 5,228.1 
        employed individuals, with 11 distinct observed values across the dataset. The majority of cases (39.4%) correspond to 
        the highest value of 5,228.1 employed citizens, followed by other values distributed across the range, such as 5,191 
        (18.8%) and 5,099.1 (20.7%). The low coefficient of variation (1.4%) indicates minimal relative variability, while the 
        moderate negative skewness (-1.04) suggests a slight concentration towards the higher employment figures.

        From an economic standpoint, a higher number of employed persons typically reflects improved labor market conditions 
        and economic health, which can influence consumer confidence and financial behaviors. A rising employment level may 
        reduce the perceived need for highly secure savings instruments like fixed-term deposits, as consumers feel more 
        confident in their income stability and are more willing to pursue riskier or higher-yield investment options. 
        Conversely, declining employment figures could trigger more conservative saving behavior, thus potentially increasing 
        demand for fixed-term deposits as a safe investment.

        Given the observed limited variation in this variable within the period considered (2008–2010), its direct influence 
        on the likelihood of concluding a fixed-term deposit contract may be subtle. However, it remains an important 
        macroeconomic indicator reflecting the broader socio-economic environment impacting bank customers’ financial decisions.

        After thoroughly examining the macroeconomic features that provide valuable context on the broader economic environment 
        influencing bank customers’ financial behavior, the analysis now shifts focus to the cluster of bank marketing activities.
        These features capture the direct interaction between the bank and its customers, both through previous and current 
        marketing campaigns. Understanding this cluster is crucial for assessing the effectiveness of marketing efforts in driving
        customer decisions, such as the subscription to fixed-term deposits.
        """, unsafe_allow_html=True)
        anchor_map_macro2 = {
          "cons.conf.idx": "pp_var_-7465342828213106388",
          "euribor3m": "pp_var_5665885795518201355",
          "nr.employed": "pp_var_-9020749104321440970"
        }

        selected_var_macro2 = st.selectbox("🔍 Select a macro-economic feature to replicate above mentioned analysis", list(anchor_map_macro2.keys()))

        url_macro2 = f"https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html#{anchor_map_macro2[selected_var_macro2]}"
        st.markdown(f"""
            <div style="transform: scale(0.8); transform-origin: top left; width: 875px; height: 750px; overflow: auto;">
                <iframe src="{url_macro2}" width="1093" height="938" style="border:none; scrolling="yes""></iframe>
            </div>
        """, unsafe_allow_html=True)

    elif task == "Data Audit - Current Marketing Activities":
        st.subheader("5. Data Audit - Current Marketing Activities")
        st.markdown("""
        One of the central clusters in the dataset comprises variables related to the current marketing campaign. These 
        features capture the direct characteristics of the most recent contact attempt with a client and are therefore 
        of particular relevance for modeling short-term response behavior (see table 4).

        The attribute cluster “Bank Marketing Activities (current)” consists of five variables: contact, month, day_of_week, 
        duration, and campaign. Together, they describe how and when the client was approached during the ongoing campaign, 
        as well as the intensity and length of this contact. These features include both categorical and continuous data 
        types and represent operational decisions within the marketing process (e.g., channel selection and call timing).

        The following section provides a detailed descriptive analysis of each feature within this cluster, including value 
        distributions, frequency counts, and potential data quality issues (e.g., sparsity or encoded missing values). These 
        insights form the basis for any necessary preprocessing decisions in the subsequent CRISP-DM phases.

        """)
        df_mark_cur = load_csv_data(
          filename="data/bank-additional-full.csv",
          sep=";",
          header=True,
          add_row_id=True
        )
        st.write("✅ DEBUG: CSV loaded – Shape:", df_mark_cur.shape)

        attribute_metadata_mark_cur = [
          {
            "ATTRIBUTE NAME": "contact",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "Communication type with client",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df_mark_cur["contact"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Bank marketing activities (current)"
          },
          {
            "ATTRIBUTE NAME": "month",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "Month of the year on which the call was made",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df_mark_cur["month"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Bank marketing activities (current)"
          },
          {
            "ATTRIBUTE NAME": "day_of_week",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "Day of the week on which the call was made",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df_mark_cur["day_of_week"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Bank marketing activities (current)"
          },
          {
            "ATTRIBUTE NAME": "duration",
            "ATTRIBUTE DATA TYPE": "continuous",
            "ATTRIBUTE DESCRIPTION": "Duration of the call/contact (in seconds)",
            "ATTRIBUTE DOMAIN VALUE": "[0, 4918]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Bank marketing activities (current)"
          },
          {
            "ATTRIBUTE NAME": "campaign",
            "ATTRIBUTE DATA TYPE": "continuous",
            "ATTRIBUTE DESCRIPTION": "Number of contacts performed during this campaign for this client (includes last contact)",
            "ATTRIBUTE DOMAIN VALUE": "[1, 56]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Bank marketing activities (current)"
          }
        ]
        metadata_df_mark_cur = pd.DataFrame(attribute_metadata_mark_cur)
        
        def render_html_table4(df: pd.DataFrame) -> str:
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
                td ul {
                    padding-left: 20px !important;
                    margin: 0 !important;
                }
                td li {
                    margin-bottom: 3px !important;
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
                    if isinstance(cell, str) and cell.strip().startswith("<ul>"):
                        html += f"<td>{cell}</td>"  # HTML anzeigen
                    else:
                        html += f"<td>{str(cell)}</td>"  # Normaler Text
                html += "</tr>"
        
            html += "</tbody></table>"
            return html

        html_table_mark_cur = render_html_table4(metadata_df_mark_cur)
        st.subheader("Table 5: Overview of the current bank marketing activity attributes")
        st.markdown(html_table_mark_cur, unsafe_allow_html=True)

        st.markdown("""
        <br>
        The “Contact” variable is a nominal feature indicating the communication channel used to reach the customer 
        during the marketing campaign. It contains two categories: “cellular” (26,144 cases, 63.5 %) and “telephone” 
        (15,044 cases, 36.5 %). There are no missing values, and thus no imputation is necessary.

        From a behavioral perspective, contact via telephone may have had a negative effect on campaign success, as 
        Portugal was transitioning to mobile communication during the data collection period (2008–2010). Customers 
        using landlines at that time were likely older, less tech-savvy, and more cautious—potentially less responsive 
        to spontaneous phone offers. In contrast, those reached via cellular tended to be younger, more mobile, and 
        more open to digital interaction, showing greater responsiveness and trust in modern communication channels. 
        This demographic shift suggests that mobile contact was not only more prevalent but also more effective in 
        engaging customers for term deposit subscriptions.

        The “Month” variable is a nominal feature indicating the calendar month in which the customer was contacted. 
        It contains 10 distinct values, with a strong seasonal skew in the distribution. The most frequent contact 
        months are May (13,769 cases, 33.4 %), July (7,174 cases, 17.4 %), and August (6,178 cases, 15.0 %), together 
        accounting for over 65 % of all contacts. In contrast, contact activity was low in December (182 cases, 0.4 %), 
        March (546, 1.3 %), and September (570, 1.4 %). There are no missing values, so no imputation is required.

        From an operational and behavioral perspective, the month of contact may influence customer availability and 
        responsiveness. The high concentration in late spring and summer months—especially May—may reflect strategic 
        campaign planning ahead of holiday periods, when customers may have more time and financial planning on their 
        minds. In contrast, low contact rates in December and early spring may coincide with lower campaign intensity 
        or reduced customer receptiveness due to holidays, tax season, or winter-related constraints.
        This pronounced seasonality suggests that timing could play a role in campaign effectiveness and will be 
        considered as a potential predictor in downstream modeling efforts.

        The “Day of the Week” variable is a nominal feature indicating on which weekday the customer was contacted. 
        It includes 5 distinct values, with a nearly uniform distribution across the working week. The most frequent 
        contact day is Thursday (8,623 cases, 20.9 %), closely followed by Monday (8,514 cases, 20.7 %), Wednesday 
        (8,134, 19.7 %), Tuesday (8,090, 19.6 %), and Friday (7,827, 19.0 %). There are no missing values, so no 
        imputation is necessary.

        From an operational perspective, the even distribution suggests that campaign calls were spread fairly consistently 
        throughout the week. This balanced approach may aim to maximize reach while avoiding weekday-specific biases. 
        However, subtle behavioral differences may still exist: for example, Monday and Thursday contacts—which slightly 
        lead in frequency—could reflect customer availability patterns or internal scheduling strategies. Further analysis 
        may explore whether certain weekdays are more strongly associated with successful term deposit subscriptions and 
        thus relevant for future campaign planning.

        """, unsafe_allow_html=True)
        anchor_map_mark_cur1 = {
          "contact": "pp_var_-6881398095397069361",
          "month": "pp_var_-1358461216462698437",
          "day_of_week": "pp_var_-1344935568411812751"
        }

        selected_var_mark_cur1 = st.selectbox("🔍 Select a current marketing activity feature to replicate above mentioned analysis", list(anchor_map_mark_cur1.keys()))

        url_mark_cur1 = f"https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html#{anchor_map_mark_cur1[selected_var_mark_cur1]}"
        st.markdown(f"""
            <div style="transform: scale(0.8); transform-origin: top left; width: 875px; height: 750px; overflow: auto;">
                <iframe src="{url_mark_cur1}" width="1093" height="938" style="border:none"; scrolling="yes"></iframe>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <br>
        Although the variable duration (call length in seconds) is strongly correlated with campaign success (emphasized 
        by the primary researchers), it should not be included in a predictive model. This is because duration is only 
        known during or after the call. Using it as a predictor would give the model access to information not available 
        at the time of decision-making—a clear case of data leakage.

        A predictive model should ideally determine a customer’s likelihood to subscribe before making contact. Since 
        duration is unknown at that point, including it would lead to overly optimistic and misleading results. Instead, 
        the variable is better suited for retrospective analyses, such as assessing call quality or agent performance.

        The “Campaign” variable is a discrete numerical feature indicating the number of contact attempts made to a client 
        during the current marketing campaign, including the final successful or unsuccessful call. It reflects the 
        persistence of the bank’s outreach efforts per individual client.

        The values range from 1 to 56, with a mean of 2.57 and a median of 2, suggesting that most clients were contacted 
        only once or twice. The standard deviation is 2.77, and the interquartile range (IQR) is relatively narrow at 2, 
        indicating limited dispersion for the majority of observations. However, the distribution is strongly right-skewed 
        (skewness = 4.76, kurtosis = 36.98), with a small number of clients receiving a disproportionately high number of 
        contact attempts. The top 5 most frequent values (1 to 5) account for over 91 % of all cases, with 42.8 % of 
        clients contacted only once. There are no missing values, so no data imputation is required.

        From a marketing strategy perspective, the number of contact attempts is a key indicator of effort versus return. 
        While a single or few calls may reflect efficient conversion, higher contact counts could suggest customer 
        hesitation or resistance. Excessive attempts (e.g., >7) may even reduce the chance of success due to perceived 
        intrusiveness. Given this, the variable is expected to exhibit a nonlinear relationship with the probability of 
        term deposit subscription and will be modeled accordingly in later phases.

        """, unsafe_allow_html=True)
        anchor_map_mark_cur2 = {
          "duration": "pp_var_5564850440795379581",
          "campaign": "pp_var_-8447834586764100216"
        }

        selected_var_mark_cur2 = st.selectbox("🔍 Select a current marketing activity feature to replicate above mentioned analysis", list(anchor_map_mark_cur2.keys()))

        url_mark_cur2 = f"https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html#{anchor_map_mark_cur2[selected_var_mark_cur2]}"
        st.markdown(f"""
            <div style="transform: scale(0.8); transform-origin: top left; width: 875px; height: 750px; overflow: auto;">
                <iframe src="{url_mark_cur2}" width="1093" height="938" style="border:none"; scrolling="yes"></iframe>
            </div>
        """, unsafe_allow_html=True)


    elif task == "Data Audit - Previous Marketing Activities":
        st.subheader("6. Data Audit - Previous marketing activities")
        st.markdown("""
        After analyzing the current campaign-related attributes, the focus now shifts to the client’s prior interaction 
        history with the bank’s marketing efforts. The attribute cluster “Bank Marketing Activities (previous)” includes 
        three variables—pdays, previous, and poutcome—which capture whether and how the client was involved in earlier 
        campaigns. These features provide valuable context on past engagement and may help explain current response behavior. 
        The following section examines each of these attributes in detail (see table 5).

        """)
        df_mark_pre = load_csv_data(
          filename="data/bank-additional-full.csv",
          sep=";",
          header=True,
          add_row_id=True
        )
        st.write("✅ DEBUG: CSV loaded – Shape:", df_mark_pre.shape)

        attribute_metadata_mark_pre = [
          {
            "ATTRIBUTE NAME": "pdays",
            "ATTRIBUTE DATA TYPE": "continuous",
            "ATTRIBUTE DESCRIPTION": "Number of days that passed by after the client was last contacted from a previous campaign",
            "ATTRIBUTE DOMAIN VALUE": "[0, 999]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Bank marketing activities (previous)"
          },
          {
            "ATTRIBUTE NAME": "previous",
            "ATTRIBUTE DATA TYPE": "continuous",
            "ATTRIBUTE DESCRIPTION": "Number of contacts performed before this campaign and for this client",
            "ATTRIBUTE DOMAIN VALUE": "[0, 7]",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Bank marketing activities (previous)"
          },
          {
            "ATTRIBUTE NAME": "poutcome",
            "ATTRIBUTE DATA TYPE": "categorical",
            "ATTRIBUTE DESCRIPTION": "Result of the last campaign if another contact was made",
            "ATTRIBUTE DOMAIN VALUE": ", ".join(sorted(df_mark_pre["poutcome"].dropna().unique())),
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Bank marketing activities (previous)"
          }
        ]
        metadata_df_mark_pre = pd.DataFrame(attribute_metadata_mark_pre)
        
        def render_html_table3(df: pd.DataFrame) -> str:
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
                td ul {
                    padding-left: 20px !important;
                    margin: 0 !important;
                }
                td li {
                    margin-bottom: 3px !important;
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
                    if isinstance(cell, str) and cell.strip().startswith("<ul>"):
                        html += f"<td>{cell}</td>"  # HTML anzeigen
                    else:
                        html += f"<td>{str(cell)}</td>"  # Normaler Text
                html += "</tr>"
        
            html += "</tbody></table>"
            return html

        html_table_mark_pre = render_html_table3(metadata_df_mark_pre)
        st.subheader("Table 5: Overview of the previous bank marketing activity attributes")
        st.markdown(html_table_mark_pre, unsafe_allow_html=True)

        st.markdown("""
        <br>
        The “Pdays” variable is a numerical feature indicating the number of days since the client was last contacted in a 
        previous campaign. A value of 999 is used as a special code to indicate that the client was not contacted before. 
        This placeholder value dominates the distribution: the median, quartiles, and 95th percentile are all 999, and over 
        95 % of all records contain this value. The mean is 962.5, and the distribution is strongly left-skewed (skewness = −4.92), 
        with very limited variation among the remaining (non-999) values. The IQR is 0, and the mode is clearly 999.

        From a data interpretation perspective, pdays essentially acts as a binary indicator: clients with a value other than 
        999 have been contacted in the past, while those with 999 have not. To improve interpretability and avoid confusion 
        in modeling, it is recommended that all 999 values be recoded to 0 during Phase 3 – Data Preparation. This transforms 
        the variable into a more meaningful numerical scale, where 0 = no prior contact, and >0 = days since last contact, 
        allowing models to better capture the impact of prior interactions on current campaign outcomes.

        The “Previous” variable is a discrete numerical feature indicating the number of contacts made with a client in previous 
        marketing campaigns before the current one. Its values range from 0 to 7, with a mean of 0.17 and a median of 0, 
        indicating that most clients had no prior contact history. This is further confirmed by the distribution: 86.3 % of all 
        records are zero, and 95 % of clients were contacted once or never before. The variable is strongly right-skewed 
        (skewness = 3.83, kurtosis = 20.11), with only a small fraction of clients receiving more than two prior contacts.

        There are no missing values, and all values are non-negative. From a modeling perspective, previous may serve as an 
        indicator of the bank's historical engagement with the client. A higher number of past contacts might reflect either 
        customer interest or repeated targeting due to prior non-responses. However, the low overall variance and the high 
        concentration at zero suggest that its predictive power may be limited and should be interpreted with caution.

        The “Poutcome” variable is a categorical feature that captures the outcome of the last marketing campaign, if the client 
        had previously been contacted. It includes three distinct values: “nonexistent” (35,563 cases, 86.3 %), “failure” 
        (4,252 cases, 10.3 %), and “success” (1,373 cases, 3.3 %). The high share of “nonexistent” values reflects that most 
        clients had not participated in a previous campaign, which aligns with the distribution observed in previous and pdays.

        There are no missing values, and the variable serves as a potential proxy for past campaign effectiveness at the 
        individual level. However, the class imbalance—particularly the dominance of “nonexistent”—suggests that its predictive 
        contribution may be limited unless transformed. In later stages of analysis, particularly during feature engineering 
        for response profiling, a consolidation strategy will be developed. This may involve grouping “nonexistent” and 
        “failure” into a single category to better capture meaningful distinctions between prior non-success and success 
        outcomes.
        """, unsafe_allow_html=True)
        anchor_map_mark_pre = {
          "pdays": "pp_var_-3887625040887036037",
          "previous": "pp_var_8015956454560663791",
          "poutcome": "pp_var_-4282519065781672492"
        }

        selected_var_mark_pre = st.selectbox("🔍 Select a previous marketing activity feature to replicate above mentioned analysis", list(anchor_map_mark_pre.keys()))

        url_mark_pre = f"https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html#{anchor_map_mark_pre[selected_var_mark_pre]}"
        st.markdown(f"""
            <div style="transform: scale(0.8); transform-origin: top left; width: 875px; height: 750px; overflow: auto;">
                <iframe src="{url_mark_pre}" width="1093" height="938" style="border:none"; scrolling="yes"></iframe>
            </div>
        """, unsafe_allow_html=True)

    elif task == "Data Audit - Target Feature":
        st.subheader("7. Data Audit - Target Feature")
        st.markdown("""
        After analyzing the three main attribute clusters representing the independent variables—namely client 
        socio-economic characteristics, macroeconomic attributes, current and previous marketing activities—the focus 
        now turns to the target variable y. This feature indicates whether a client subscribed to a term deposit after 
        the marketing campaign and thus represents the dependent variable for all subsequent predictive modeling.

        The variable y is Boolean, with two distinct values: True (4,640 cases, 11.3 %) and False (36,548 cases, 88.7 %). 
        There are no missing values, but a clear class imbalance is present, as only a small proportion of clients 
        responded positively.

        This imbalance has important implications for predictive modeling. Without corrective measures, most standard 
        classifiers will be biased toward the majority class (False) and may show deceptively high accuracy while failing 
        to detect the minority class (True). To address this issue, different strategies are considered:
         - No resampling: Baseline models may initially use the imbalanced data to assess natural model behavior.
         - Upsampling of the minority class (True) can improve sensitivity but risks overfitting.
         - Use of class weights during model training allows algorithms to penalize misclassifications of the minority 
           class more heavily, often yielding balanced performance without altering the data.
         - Representative sampling: In some exploratory modeling iterations, a 50/50 ratio may be created by randomly 
           selecting a subset of the majority class (False). This approach simplifies interpretation but should be used 
           cautiously, as it may not reflect real-world prevalence.

        For algorithmic compatibility and the application of statistical and machine learning methods in both the data 
        preparation and modeling phases, the categorical target variable will be converted into a binary dummy format: 
        1 for “True” (subscribed), 0 for “False” (not subscribed). This transformation ensures the variable can be properly 
        used in regression-based and classification models.

        Finally, a 70/30 train-test split will be used for the initial modeling iteration. This is a state-of-the-art 
        approach that provides a robust balance between model training capacity and evaluation reliability on unseen data.

        Below you find ydata link to replicate target feature analysis
        <br>        
        """, unsafe_allow_html=True)

        url_target = f"https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html#pp_var_-2707228818546900142"

        st.markdown(f"""
            <div style="transform: scale(0.8); transform-origin: top left; width: 875px; height: 750px; overflow: auto;">
                <iframe src="{url_target}" width="1093" height="938" style="border:none"; scrolling="yes"></iframe>
            </div>
        """, unsafe_allow_html=True)
        
    elif task == "Key Findings of the 2nd Phase":
        st.subheader("8. Key findings & reconmmendations for data (pre-)processing")
        st.markdown("""
        The data understanding phase—complementary to the business understanding phase—has yielded important insights 
        regarding the structure, quality, and interpretability of the dataset used in this project. Through a systematic 
        data audit, informed by both exploratory statistical analyses and the original documentation provided by the 
        primary researchers, several findings and concrete recommendations for the subsequent data preparation phase 
        have been derived.

        Key Findings:
        - The dataset bank-additional-full.csv comprises 41,188 observations and 21 attributes (20 input features and one 
          binary target variable).
        - The features are logically clustered into thematic groups: client demographics, current and previous marketing 
          activities, and macroeconomic context indicators.
        - Categorical attributes such as job, education, default, and poutcome contain missing values represented by the 
          placeholder "unknown". Their proportion and distribution were analyzed to inform further preprocessing steps.
        - The variable duration, although highly correlated with the target outcome, is not usable for predictive modeling 
          in real-world settings, as its value is only known post-contact. Its exclusion from modeling is both methodologically
          and ethically justified.
        - Minimal duplication was observed across records, with only a negligible number of exact duplicates identified. 
          These can be safely removed without information loss.
        <br>
        """, unsafe_allow_html=True)
        show_github_image(
        image_filename="images/key_findings_data_under.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 10: Overview key findings within data understanding phase")
        )
        st.markdown("""

        Derived Recommendations for Data (Pre-)Processing:
        1.	Guidance Compliance:
            - Follow the primary researchers’ instructions by treating "unknown" values as potential class categories or
              applying targeted imputation techniques based on variable type and distribution.
            - Exclude the feature duration from modeling workflows to avoid data leakage and ensure model realism.
        <br>
        2.	Data Cleaning:
            - Remove duplicate entries due to their low frequency and minimal influence on the dataset’s variance structure.
        <br>
        3.	Target Encoding:
            - Recode the binary target variable y from textual categories ("yes"/"no") to numeric format (1/0) to ensure 
              compatibility with machine learning models.
        <br>
        4.	Imputation and Encoding Strategy:
            - For categorical variables with "unknown" entries, apply mode imputation or group-level encoding (e.g., one-hot 
              encoding including an "unknown" category).
            - For continuous variables, apply z-transformation (standardization), ensuring comparability across features 
              with different value ranges.
        <br>    
        5.	Recoding and Binning:
            - Recode the variable pdays, where the value 999 represents "not previously contacted", to 0 = not contacted, 
              else copy.
            - Collapse sparse categorical values where appropriate, such as binning the labels "unknown" and "yes" in the 
              default variable to form a combined category "unknown|yes", reflecting similar credit risk implications.

        These data understanding outcomes provide a robust foundation for the upcoming Data Preparation phase, in which the 
        outlined preprocessing strategies will be operationalized. The informed design of data transformations and cleaning 
        steps ensures consistency with both domain knowledge and modeling requirements.
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

