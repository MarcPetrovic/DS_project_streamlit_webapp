import streamlit as st

# ----------------------------
# Session-State Setup
# ----------------------------
if "main_page" not in st.session_state:
    st.session_state.main_page = "Introduction"
if "sub_section" not in st.session_state:
    st.session_state.sub_section = None

# ----------------------------
# Sidebar Navigation
# ----------------------------

# Hauptnavigation
main_page = st.sidebar.radio("Navigation", [
    "Introduction",
    "Theoretical Framework",
    "Methods & Data",
    "Technical Environment & Modeling",
    "Key Results",
    "Conclusion & Discussion"
], index=[
    "Introduction",
    "Theoretical Framework",
    "Methods & Data",
    "Technical Environment & Modeling",
    "Key Results",
    "Conclusion & Discussion"
].index(st.session_state.main_page))

# Session-State aktualisieren
st.session_state.main_page = main_page
st.session_state.sub_section = None  # Nur beibehalten, wenn benötigt

# Subnavigation
if main_page == "Theoretical Framework":
    sub_section = st.sidebar.radio("Subtopics", [
        "PORTER'S VALUE CHAIN APPROACH AND COST OPTIMIZATION",
        "THE RELEVANCE OF DATA MINING FOR DIRECT MARKETING CAMPAIGNS",
        "SUPERVISED LEARNING AND THE RESPONSE-MODEL",
        "BRIEF INTRODUCTION TO CRISP-DM"
    ])
    st.session_state.sub_section = sub_section

# ----------------------------
# Breadcrumb anzeigen (nachdem Session-Status aktualisiert wurde!)
# ----------------------------

breadcrumb_html = """
<style>
.breadcrumb-container {
    background-color: #f8f9fa;
    padding: 12px 16px;
    border-radius: 8px;
    font-size: 16px;
    margin-bottom: 25px;
    border: 1px solid #dee2e6;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background-color: #ffffff;
}
.breadcrumb-link {
    color: #0074cc;
    text-decoration: none;
    font-weight: 500;
    margin-right: 5px;
    cursor: pointer;
}
.breadcrumb-current {
    color: #212529;
    font-weight: 600;
    margin-left: 5px;
}
</style>
<div class='breadcrumb-container'>
  📍 <span class='breadcrumb-link'>Home</span>
"""

# Breadcrumb erweitern
breadcrumb_html += f"&nbsp;&gt;&nbsp;<span class='breadcrumb-link'>{st.session_state.main_page}</span>"
if st.session_state.sub_section:
    breadcrumb_html += f"&nbsp;&gt;&nbsp;<span class='breadcrumb-current'>{st.session_state.sub_section.title()}</span>"

breadcrumb_html += "</div>"
st.markdown(breadcrumb_html, unsafe_allow_html=True)

# ----------------------------
# Inhaltslogik
# ----------------------------

if st.session_state.main_page == "Introduction":
    from my_pages import introduction
    introduction.show()

elif st.session_state.main_page == "Theoretical Framework":
    from my_pages import theoretical_framework_overview
    theoretical_framework_overview.show()

    if st.session_state.sub_section == "PORTER'S VALUE CHAIN APPROACH AND COST OPTIMIZATION":
        from my_pages.theoretical_framework import porters_value_chain
        porters_value_chain.show()

    elif st.session_state.sub_section == "THE RELEVANCE OF DATA MINING FOR DIRECT MARKETING CAMPAIGNS":
        from my_pages.theoretical_framework import relevance_data_mining
        relevance_data_mining.show()

    elif st.session_state.sub_section == "SUPERVISED LEARNING AND THE RESPONSE-MODEL":
        from my_pages.theoretical_framework import supervised_learning
        supervised_learning.show()

    elif st.session_state.sub_section == "BRIEF INTRODUCTION TO CRISP-DM":
        from my_pages.theoretical_framework import introduction_crisp_dm
        introduction_crisp_dm.show()

elif st.session_state.main_page == "Methods & Data":
    from my_pages import methods_data
    methods_data.show()

elif st.session_state.main_page == "Technical Environment & Modeling":
    from my_pages import technical_environment_modeling
    technical_environment_modeling.show()

elif st.session_state.main_page == "Key Results":
    from my_pages import key_results
    key_results.show()

elif st.session_state.main_page == "Conclusion & Discussion":
    from my_pages import conclusion_discussion
    conclusion_discussion.show()
