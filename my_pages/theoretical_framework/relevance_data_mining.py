import streamlit as st
from utils.image_loader import show_github_image

def show():
    st.markdown('<a name="top"></a>', unsafe_allow_html=True)
    st.header("Relevance of Data Mining")
    st.markdown("""
    A growing number of companies, especially financial service providers, banks and insurance companies, are 
    using customer relationship management with the sole aim of customer profiling. Recent studies clearly 
    show that there is not only a linear relationship between marketing expenditure and profit margins per 
    customer, but that a competitive advantage can be achieved through the systematic use of modern methods 
    of data pattern recognition, such as data mining and knowledge discovery in databases (KDD). Data mining 
    refers to the examination and analysis of large amounts of data in order to discover meaningful patterns 
    and rules. Direct marketing has developed into an important area of application for data mining, 
    particularly in connection with customer targeting, so that a taxonomy for strategic use in marketing 
    management has now become established (see Figure 3). 
    """)

    show_github_image(
    image_filename="images/taxonomy_ai.PNG",
    repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
    caption=( "Figure 5: Taxonomy of Artificial Intelligence use in Marketing")
    )
    st.markdown("""
    Methods for recognizing data patterns that aim to identify causal relationships are roughly divided into 
    supervised and unsupervised learning methods, as they are known from robotics. The first group includes 
    predictions based on classic regression methods, classifications with decision trees or artificial neural 
    networks (ANN) and time series analyses. What these methods have in common is that they learn the (known) 
    dependency of the underlying variables from data sets and make them available as a prediction model. The 
    second group of machine learning methods (so called unsupervised learning) includes association analyses 
    such as market basket analysis, sequence pattern analysis and the Apriori algorithm as well as segmentation 
    (clustering). No ‘learning patterns’ are available to these algorithms. Instead, they independently 
    determine hypotheses from the data material (see Figure 4).

    """)

    show_github_image(
    image_filename="images/groups_ml.PNG",
    repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
    caption=( "Figure 6: Schematic representation main groups of machine learning")
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
