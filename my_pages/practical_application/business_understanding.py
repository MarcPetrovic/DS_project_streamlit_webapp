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
        The Business Understanding phase focuses on understanding the objectives and requirements of the project.
        Aside from the third general task, the three other tasks in this phase are foundational project management
        activities:
        1.	Define the business objectives: Based on a deep understanding of the business customer perspective, 
        the business success criteria can then be determined.
        2.	Assessment of the situation in the business environment: What (technical and financial) resources are 
        available, what requirements are placed on the project, what costs are associated with what returns 
        and what risks can be calculated.
        3.	Determine the objectives of data mining: In addition to defining the business objectives, the type of 
        data mining should be explained (e.g. classification) and, based on this, the success criteria of data 
        mining (e.g. accuracy) must be derived.
        4.	Produce project plan: Select technologies and tools and define detailed plans for each project phase.
       """)
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
