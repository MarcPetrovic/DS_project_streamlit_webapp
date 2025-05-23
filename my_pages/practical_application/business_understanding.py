import streamlit as st
from utils.image_loader import show_github_image

def show():
  # Dropdown für die Phasen
    phase = st.selectbox("Select a subchapter of CRISP-DM-phase Business Understanding:", [
        "General Business Knowledge",
        "Cost-optimized Assesment Metrics",
        "General Evaluation Metrics",
        "Technical Framework & Environment",
        "Key Results of the 1st Phase"
    ])
    # Inhalte je nach Auswahl
    if phase == "General Business Knowledge":
        st.subheader("1. General business knowledge")
        st.markdown("""
        In the following, a well-founded understanding of the business process of investing term deposits at banks 
        will be conveyed. Without this expertise, it is not possible to use data and technology effectively and 
        efficiently to achieve the project goal. At its core, the current data project is about helping banks to 
        improve their marketing efforts by reducing costs and saving resources such as call center agents. It is 
        a classification problem involving the prediction of contract signings of term deposits. In general, a 
        marketing campaign represents the stimulus, and in the context of this project, the stimulus is represented 
        by a specific call from an internal bank call center agent. The stimulus is concrete in the context of the 
        call: This is an offer of a specific fixed-term deposit contract with interest rates above the market average. 
        The response side is represented by a bank customer and his reaction to the agent's call respectively to the 
        offer. The recorded reaction of the bank customer is binary and distinguishes between “Yes”, conclusion of 
        a fixed-term deposit contract, or “No”, no conclusion of a fixed-term deposit contract.
       """)
          # Bild von der URL laden und anzeigen 
        show_github_image(
        image_filename="images/target_group_marketing.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 6: Target groups in marketing: Who is the fixed-term deposit suitable for?")
        )
        st.markdown("""
        A fixed-term deposit is an investment with a fixed term in which money is paid into an account at a financial 
        institution. Fixed-term deposits generally have short-term terms of one month to several years and have 
        different minimum deposits. When concluding a fixed-term deposit contract, investors must be aware that they 
        will not be able to access their money again until the contractually agreed term has expired. In some cases, 
        the account holder may allow the investor to terminate - or withdraw - the deposit early if they give several 
        days' notice. There is also a penalty for early cancellation. Fixed-term deposits offer consumers a high degree 
        of planning security, as the interest rates are fixed and guaranteed. It is therefore suitable for customers 
        who prefer a conservative, secure investment to preserve their assets. Fixed-term deposits are suitable for 
        short-term investments, for example if you want to ‘park’ money that you will only need for an investment at 
        a later date. However, you can also use fixed-term deposits to build up assets or as part of your retirement 
        provision. As fixed-term deposits are not affected by price fluctuations, they are a particularly safe form 
        of investment.
       """)
          # Bild von der URL laden und anzeigen 
        show_github_image(
        image_filename="images/business_logic.PNG",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption=( "Figure 7: Presentation of the business logic in the financial services sector with special \n"
                 "emphasis on the three players involved in financial transactions")
        )
    elif phase == "Cost-optimized Assesment Metrics":
        st.subheader("2. Cost-optimized assesment metrics for a cost-sensitive classification problem")
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
    elif phase == "General Evaluation Metrics":
        st.subheader("3. General metrics for evaluating a classification problem")
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
    elif phase == "Technical Framework & Environment":
        st.subheader("4. Technical framework & environment")
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
    elif phase == "Key Results of the 1st Phase":
        st.subheader("5. Key results of the 1st phase of CRISP-DM")
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
