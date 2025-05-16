import streamlit as st
import os
#from utils.profiling_viewer import show_profiling_report

def show():
    st.header("Methods & Data")

    st.write("""
    In diesem Abschnitt wird der Datensatz vorgestellt und analysiert. 
    Der folgende Report wurde automatisch mit [YData Profiling](https://github.com/ydataai/ydata-profiling) erstellt 
    und bietet eine umfassende Übersicht der Datenqualität, Verteilungen und Korrelationen.
    """)
    st.markdown("""
        <a href="/static/bank_marketing.html" target="_blank">
            👉 Profiling Report in neuem Tab öffnen
        </a>
    """, unsafe_allow_html=True)

    #show_profiling_report("profiling/bank_marketing.html")

