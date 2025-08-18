import streamlit as st

def show():
    st.title("📚 Bibliography")

    st.markdown("""
    ### References  

    - Moro, S., Cortez, P., & Rita, P. (2014). *A Data-Driven Approach to Predict the Success of Bank Telemarketing*. Decision Support Systems, 62, 22–31.  
      Dataset: [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Bank+Marketing)  

    - Fayyad, U., Piatetsky-Shapiro, G., & Smyth, P. (1996). *From Data Mining to Knowledge Discovery in Databases*. AI Magazine, 17(3), 37–54.  

    - Han, J., Pei, J., & Kamber, M. (2011). *Data Mining: Concepts and Techniques*. Elsevier.  

    - Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O’Reilly.  

    - Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.  

    ---
    📌 For a complete list of references, see the project documentation (PDF/Word report).
    """)
