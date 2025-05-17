import streamlit as st

# ----------------------------
# Sidebar Navigation
# ----------------------------

# Hauptnavigation – direkt an den Session-State gebunden
st.sidebar.radio(
    "Navigation",
    [
        "Introduction",
        "Theoretical Framework",
        "Methods & Data",
        "Technical Environment & Modeling",
        "Key Results",
        "Conclusion & Discussion"
    ],
    key="main_page"
)

# Subnavigation nur, wenn nötig – ebenfalls direkt an den Session-State gebunden
if st.session_state.main_page == "Theoretical Framework":
    st.sidebar.radio("Subtopics", [
        "PORTER'S VALUE CHAIN APPROACH AND COST OPTIMIZATION",
        "THE RELEVANCE OF DATA MINING FOR DIRECT MARKETING CAMPAIGNS",
        "SUPERVISED LEARNING AND THE RESPONSE-MODEL",
        "BRIEF INTRODUCTION TO CRISP-DM"
    ], key="sub_section")
else:
    st.session_state.sub_section = None

# ----------------------------
# Breadcrumb anzeigen (mit Links)
# ----------------------------

breadcrumb_html = """
<style>
/* Sticky-Stil für Breadcrumb-Leiste */
.breadcrumb-container {
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    left: 0;
    right: 0;
    background-color: #f8f9fa;
    padding: 12px 16px;
    font-size: 16px;
    z-index: 999;
    border-bottom: 1px solid #dee2e6;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

/* Verhindert Überlappung des Inhalts */
.breadcrumb-spacer {
    height: 65px; /* gleiche Höhe wie .breadcrumb-container */
}

/* Link- und Textstile */
.breadcrumb-link {
    color: #0074cc;
    font-weight: 500;
    cursor: pointer;
}

.breadcrumb-current {
    color: #212529;
    font-weight: 600;
}
</style>

<!-- Abstandhalter für den fixierten Header -->
<div class='breadcrumb-spacer'></div>

<!-- Sticky Breadcrumb selbst -->
<div class='breadcrumb-container'>
    📍 <a class='breadcrumb-link' href="javascript:void(0);" onclick="window.location.reload();">Home</a> &nbsp;&gt;&nbsp;
    <span class='breadcrumb-link'>""" + st.session_state.main_page + """</span>
"""

if st.session_state.sub_section:
    breadcrumb_html += f"&nbsp;&gt;&nbsp;<span class='breadcrumb-current'>{st.session_state.sub_section.title()}</span>"

breadcrumb_html += "</div>"

st.markdown(breadcrumb_html, unsafe_allow_html=True)

# ----------------------------
# Inhaltslogik je nach Auswahl
# ----------------------------

# Setze den Session-State zurück, wenn auf "Home" (Introduction) geklickt wird
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
