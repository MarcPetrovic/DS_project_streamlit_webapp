import streamlit as st

# Hauptnavigation
main_page = st.sidebar.radio("Navigation", [
    "Introduction",
    "Theoretical Framework",
    "Methods & Data",
    "Technical Environment & Modeling",
    "Key Results",
    "Conclusion & Discussion"
])

# Introduction
if main_page == "Introduction":
    from pages import introduction
    introduction.show()

# Theoretical Framework + Subnavigation
elif main_page == "Theoretical Framework":
    from pages import theoretical_framework_overview
    theoretical_framework_overview.show()

    sub_section = st.sidebar.radio("Subtopics", [
        "PORTER'S VALUE CHAIN APPROACH AND COST OPTIMIZATION",
        "THE RELEVANCE OF DATA MINING FOR DIRECT MARKETING CAMPAIGNS",
        "SUPERVISED LEARNING AND THE RESPONSE-MODEL",
        "BRIEF INTRODUCTION TO CRISP-DM"
    ])

    if sub_section == "PORTER'S VALUE CHAIN APPROACH AND COST OPTIMIZATION":
        from pages.theoretical_framework import porters_value_chain
        porters_value_chain.show()

    elif sub_section == "THE RELEVANCE OF DATA MINING FOR DIRECT MARKETING CAMPAIGNS":
        from pages.theoretical_framework import relevance_data_mining
        relevance_data_mining.show()

    elif sub_section == "SUPERVISED LEARNING AND THE RESPONSE-MODEL":
        from pages.theoretical_framework import supervised_learning
        supervised_learning.show()

    elif sub_section == "BRIEF INTRODUCTION TO CRISP-DM":
        from pages.theoretical_framework import introduction_crisp_dm
        introduction_crisp_dm.show()

# Methods & Data
elif main_page == "Methods & Data":
    from pages import methods_data
    methods_data.show()

# Technical Environment & Modeling
elif main_page == "Technical Environment & Modeling":
    from pages import technical_environment_modeling
    technical_environment_modeling.show()

# Key Results
elif main_page == "Key Results":
    from pages import key_results
    key_results.show()

# Conclusion & Discussion
elif main_page == "Conclusion & Discussion":
    from pages import conclusion_discussion
    conclusion_discussion.show()
