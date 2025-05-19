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
    
    This report describes the implementation of an AI project based on the CRISP-DM methodology. The used data 
    were collected by a Portuguese bank that used its own contact centre for targeted marketing campaigns. The 
    bank customers were contacted by telephone with human agents as dialogue partners and received an attractive 
    offer for long-term deposits with good interest rates (so-called fixed-term deposits). The dataset consists 
    of 17 telephone campaigns conducted between May 2008 and November 2010, totaling 41,188 contacts. A large 
    number of characteristics were recorded for each contact (see CRISP PHASE II - DATA STATEMENT in detail) 
    and also whether the offer (conclusion of a fixed-term deposit contract, the target variable) was accepted 
    by the contacted customer. The total data sample comprises 4,640 contracts, which corresponds to a success 
    rate of 11.3 %. 

    The central aim of the project is to develop a statistically relevant (response) model that can explain the 
    success of a telephone contact (described model from the field of business intelligence). Such a response 
    model should increase the efficiency of a campaign by identifying the most important characteristics that 
    influence success and contribute to the optimal use of available resources (e.g. working time and number of 
    telephone calls). Essentially, the generated model should produce cost-optimized results in the segmentation 
    of a high-quality group of potential customers (prediction model as a methodology of basic machine learning).

    The project report is organized as follows: Sect. 2 provides some theoretical background on Data Mining, 
    Machine Learning, and their applications in Marketing. Section 3 illustrates the methodology adopted for 
    covering the Data Mining practical project. Section 4 presents the findings and describes in detail the pros 
    and cons of the selected model. Finally, the last section discusses conclusions and acknowledges the 
    limitations of the study, highlighting opportunities for further approaches.
    
    """)
