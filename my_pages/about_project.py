import streamlit as st

def show():
    st.markdown('<a name="top2"></a>', unsafe_allow_html=True)
    st.title("About This Project")

    st.markdown("""
    ## Acknowledgements  
    This project was created as part of a Data Science training program.  
    Special thanks go to **Lucas Varela** for his guidance and to **[datascientest.com](https://datascientest.com)**, 
    the training provider.  

    ---

    ## Authors & Contributions  
    - **Analysis & Evaluation:** Conducted by *Marc Petrovic*  
    - **Implementation & Web App:** Developed using [Streamlit](https://streamlit.io/) and deployed on **Streamlit Cloud**  
    - **Data Source:**  
      The dataset entitled *“Bank Marketing (with social/economic context)”* is publicly available via the  
      [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Bank+Marketing).  

    ---

    ## Imprint & Privacy Notice  
    This project is a **non-commercial academic exercise**.  
    It is intended solely for educational and demonstration purposes.  

    - **Imprint / Contact:** [marc.petrovic@stud.uni-due.de]  
    - **Privacy Notice:** No personal data is collected, stored, or processed by this web application.  
      All data used originates from the **public UCI repository** and is completely anonymized.  

    ---

    ## Project Repository  
    The full source code, methodology report, and documentation are available on GitHub:  
    👉 [View the GitHub Repository](https://github.com/MarcPetrovic/DS_project_streamlit_webapp)  

    Please refer to the **[README.md](https://github.com/MarcPetrovic/DS_project_streamlit_webapp/blob/main/README.md)** for further project details.  

    ---

    ## License  
    This project is distributed under the terms of the **MIT License**.  
    See the [LICENSE](https://github.com/MarcPetrovic/DS_project_streamlit_webapp/blob/main/LICENSE) file for details.  
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
        <a href="#top2" id="scroll-top-link" title="Top">
            <i class="fas fa-arrow-up"></i>
        </a>
    """, unsafe_allow_html=True)
