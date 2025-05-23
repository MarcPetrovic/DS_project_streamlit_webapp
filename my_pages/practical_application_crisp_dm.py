import streamlit as st
from utils.image_loader import show_github_image

def show():
    st.header("Practical Application According to CRISP-DM")
    st.markdown("""
    The following chapter will goes through the first 5 phases of CRISP-DM in detail, with the key results 
    from each phase listed in Figure 6. Each of the following sections is structured in such a way that the 
    core results are listed at the end. This is based on the hierarchical CRISP-DM levels (phases, generic 
    tasks, special activities) described in Chapter 2 of this research paper
    """)
    # Bild von der URL laden und anzeigen
    with st.expander("🔍 Show CRISP-DM overview diagram"):
        show_github_image(
            image_filename="images/crisp_dm_project_phases.PNG",
            repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
            caption="CRISP-DM overview diagram"
            )
