import streamlit as st
from utils.image_loader import show_github_image

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
        Within the second phase of CRISP-DM, we have to understand the data, especially the structure. The data audit is 
        an essential sub-step within the second phase. Within the data audit, the available data sample is structured on 
        the basis of various properties. For example, a distinction is made between dependent and independent variables. 
        The data type of the respective characteristics of the sample is determined and the relevant value range (feature 
        domain) is also listed. A central concern of the data audit is to identify missing values and, depending on the 
        data type and relevant feature structure, to select a representative, statistical procedure to convert the missing 
        values in a targeted manner. Figure 8 shows that the available data set can basically be differentiated into four 
        feature clusters. All four feature clusters are examined in more detail in the following subsections. First, a 
        general definition of the respective characteristics of each cluster is formulated. In addition, an explorative, 
        descriptive data analysis is carried out in order to subsequently identify missing values and, against the 
        background of the industrial CRISP-DM approach, to make a pragmatic selection of procedures for converting the 
        missing values.
        """)
          # Bild von der URL laden und anzeigen 
        show_github_image(
          image_filename="images/attribute_cluster.PNG",
          repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
          caption=( "Figure 9: Overview of the four data type clusters within the used database")
          )

    elif task == "Instructions Primary Researcher":
        st.subheader("2. Instructions from the Primary Researcher")
          # Bild von der URL laden und anzeigen 
        show_github_image(
        image_filename="images/instructions_primary_researcher.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 10: Instructions from the primary researcher")
        )
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
