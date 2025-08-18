import streamlit as st

def show_about():
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
