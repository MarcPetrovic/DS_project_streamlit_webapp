import streamlit as st
from utils.image_loader import show_github_image

def show():
    st.header("Introduction")
    st.markdown("""
    <hi style='font-size: 32px; font-weight: bold;'>AI for bank marketing campaigns – <br>A data-driven path to cost-optimized direct customer contact in term deposit sales business</hi>
    """, unsafe_allow_html=True)
    
    # Bild von der URL laden und anzeigen
    show_github_image(
        image_filename="images/porter.png",
        repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
        caption="Porter's Value Chain"
    )
    st.markdown("""
    Over the last two decades, globalization and ever-increasing regulation by the banking supervisory 
    authorities have presented the financial sector with major challenges: On the one hand, open markets 
    have led to an intensification of competitive pressure, which has simultaneously led to a decline in 
    profit margins. On the other hand, financial service providers had to implement cross-border requirements 
    to protect their customers and secure their own liquidity, the implementation of which was associated 
    with additional financial costs. Banks could and can only withstand the economic pressure described 
    above if they see digitalization as an opportunity. Modern marketing management at financial service 
    providers therefore combines business and artificial intelligence concepts with machine learning methods 
    (e.g. decision trees, regression or dimension reduction) in order to generate cost-optimized 
    communication campaigns.
    
    ## Ziel der Untersuchung
    Dein Ziel könnte sein, Lösungen zu finden, die helfen, dieses Problem zu adressieren.
    """)
