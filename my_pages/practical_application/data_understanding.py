import streamlit as st
from utils.image_loader import show_github_image
from utils.data_loader import load_csv_data
import pandas as pd
import numpy as np

def show():
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
        st.write("✅ DEBUG: CSV geladen – Shape:", df2.shape)
        #st.dataframe(df2.head())  
            # Metadaten definieren
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
            "ATTRIBUTE DOMAIN VALUE": "<ul>" + "".join(
              f"<li>{val}</li>" for val in sorted(df2["job"].dropna().unique())
            ) + "</ul>",
            "ATTRIBUTE MODEL TYPE": "feature",
            "ATTRIBUTE CLUSTER": "Client socio-economic attributes"
          }
        ]
        metadata_df = pd.DataFrame(attribute_metadata)
        st.subheader("📊 Tabelle 2: Übersicht Client Attributes")
        st.dataframe(metadata_df)
        # --- HTML-Tabelle erzeugen ---
        def render_html_table(df: pd.DataFrame) -> str:
            html = """
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                    table-layout: fixed;
                }
                th, td {
                    border: 1px solid lightgray;
                    text-align: left;
                    padding: 8px;
                    word-wrap: break-word;
                    max-width: 250px;
                    font-size: 14px;
                }
                th {
                    background-color: #097a80;
                }
                td {
                    background-color: white;
                }
                td ul {
                    padding-left: 20px;
                    margin: 0;
                }
                td li {
                    margin-bottom: 3px;
                }
            </style>
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
        
        # --- Anzeige in Streamlit ---
        st.subheader("📊 Tabelle 2: Übersicht Client Socio-Economic Attributes")
        st.markdown(render_html_table(metadata_df), unsafe_allow_html=True)

    elif task == "Data Audit - Economic Environment":
        st.subheader("4. Data Audit - Economic Environment")
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
