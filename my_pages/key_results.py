import streamlit as st

def show():
    st.header("Key Results")
    st.write("Hier formulierst du deine Kernresultate.")
# 1️⃣ Anker oben einfügen
    st.markdown('<a name="top2"></a>', unsafe_allow_html=True)
    
    # 2️⃣ Inhalt zum Scrollen erzeugen
    for i in range(30):
        st.write(f"Line {i+1}")
    
    # 3️⃣ Scroll-Pfeil
    st.markdown("""
    <a href="#top2" style="
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 48px;
        background-color: rgba(0,0,0,0.7);
        color: white;
        padding: 10px 15px;
        border-radius: 50%;
        text-decoration: none;
        z-index: 1000;">⬆️</a>
    """, unsafe_allow_html=True)
