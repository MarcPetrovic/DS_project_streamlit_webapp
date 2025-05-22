import streamlit as st
from utils.image_loader import show_github_image

def show():
    st.header("Introduction")
    st.markdown("""
    <hi style='font-size: 32px; font-weight: bold;'>AI for bank marketing campaigns – <br>A data-driven path to cost-optimized direct customer contact in term deposit sales business</hi>
    """, unsafe_allow_html=True)
    
    # Bild von der URL laden und anzeigen
    show_github_image(
    image_filename="images/porter.PNG",
    repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
    caption="Porter's Value Chain"
    )
