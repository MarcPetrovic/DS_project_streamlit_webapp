import streamlit as st

def show():
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
    # Bild von der URL laden und anzeigen
    show_github_image(
    image_filename="images/taxonomy_ai.PNG",
    repo_url="https://github.com/MarcPetrovic/DS_project_streamlit_webapp",
    caption=( "Figure 3: Taxonomy of Artificial Intelligence use in Marketing")
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
