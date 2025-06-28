import streamlit as st
from utils.image_loader import show_github_image

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    st.header("Introduction")
    if st.checkbox("🔍 Show Porter's Value Chain Quote", value=True):
        show_github_image(
            image_filename="images/porter.PNG",
            repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
            caption="Porter's Value Chain Quote"
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
    st.markdown("""
        <!-- Font Awesome einbinden -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

        <style>
        #scroll-top-link {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 100;
    
            width: 60px;
            height: 60px;
            border: none;
            border-radius: 50%;
            cursor: pointer;
    
            display: flex;
            align-items: center;
            justify-content: center;
    
            background-color: black;
            color: white;
            text-decoration: none;
            font-size: 24px;
            transition: background-color 0.3s ease, opacity 0.2s ease;
        }
    
        @media (prefers-color-scheme: dark) {
            #scroll-top-link {
                background-color: #222;
                color: white;
            }
        }
    
        @media (prefers-color-scheme: light) {
            #scroll-top-link {
                background-color: #e0e0e0;
                color: black;
            }
        }
    
        /* Optional: Hover-Effekt */
        #scroll-top-link:hover {
            opacity: 0.85;
        }
        </style>
    
        <!-- Button mit Icon -->
        <a href="#top" id="scroll-top-link" title="Top">
            <i class="fas fa-arrow-up"></i>
        </a>
    """, unsafe_allow_html=True)
