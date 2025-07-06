import streamlit as st
from utils.image_loader import show_github_image

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    st.header("Supervised Learning and the Response model")
    st.markdown("""
    The response model is a well-known technique often used by direct marketing analysts and can be categorized 
    as a supervised learning method. A response model predicts the likelihood that a customer will respond to 
    a promotion or offer. Response models are usually created on the basis of historical purchase data. The 
    model allows companies to identify a subset of customers who are more likely to respond than other customer 
    sup-groups. The main purpose of these models is to select the customers who are most interested in a 
    particular product offering so that the largest possible percentage of target customers respond positively 
    to the product offering. In this way, companies can maximize their profits when selling products or services 
    and minimize the costs of the marketing campaign. In addition, the use of data mining techniques improves 
    return on investment, customer relationships and customer loyalty.

    The response model is usually a binary classification problem. Customers are divided into two classes, e.g. 
    respondents and non-respondents. Various classification methods are used for response modelling, e.g. 
    statistical and machine learning methods such as neural networks or other classification algorithms. All 
    data pattern recognition methods, including the response model, can be viewed as a process that proceeds in 
    stages from problem formulation, data acquisition, data pre-processing, feature construction, feature 
    selection, class matching, actual algorithmic pattern recognition and interpretation (modelling and evaluation) 
    to model implementation. Once the model has been introduced and is in use, adjustments are usually necessary 
    again and again, which leads to a cyclical restart of the process. The procedure described corresponds to 
    the generally recognized and widely used industry standard CRISP-DM (‘Cross-industry Standard Process for 
    Data Mining’).
    """)

    show_github_image(
    image_filename="images/crisp_dm_model.PNG",
    repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
    caption=( "Figure 6: Model of iteration cycles of the CRIPS-DM")
    )
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
