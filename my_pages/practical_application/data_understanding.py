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
        "Key Results of the 2nd Phase"
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
            <div style="transform: scale(0.8); transform-origin: top left; width: 875px; height: 750px; overflow: auto;">
                <iframe src="{url2}" width="1093" height="938" style="border:none; scrolling="yes""></iframe>
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
                <iframe src="{url_macro}" width="1093" height="938" style="border:none; scrolling="yes""></iframe>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <br>
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

        """, unsafe_allow_html=True)


    elif task == "Data Audit - Current Marketing Activities":
        st.subheader("5. Data Audit - Current Marketing Activities")
        st.markdown("""
        In the data understanding phase, which should be interpreted as complementary to the business understanding
        phase, the focus is on identifying, collecting and analysing the data sets that can help you achieve the
        project objectives. In this context, the quality of the data must be checked and ensured. This phase also 
        includes the task of describing the data using statistical analyses and determining attributes and their 
        characteristics. This phase also consists of a total of four tasks:
        1.	Collect initial data: Acquire the necessary data and (if necessary) load it into your analysis tool.
        2.	Describe data: Examine the data and document its surface properties like data format, number of records, 
        or field identities.
        3.	Explore data: Dig deeper into the data. Query it, visualize it, and identify relationships among the 
        data.
        4.	Verify data quality: How clean/dirty is the data? Document any quality issues.
        """)
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

