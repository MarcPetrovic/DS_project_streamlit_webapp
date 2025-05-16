import streamlit as st
from utils.profiling_viewer import show_profiling_report

def show():
    st.header("Methods & Data")

    st.write("""
    In diesem Abschnitt wird der Datensatz vorgestellt und analysiert. 
    Der folgende Report wurde automatisch mit [YData Profiling](https://github.com/ydataai/ydata-profiling) erstellt 
    und bietet eine umfassende Übersicht der Datenqualität, Verteilungen und Korrelationen.
    """)

    # HTML-Report einbinden
    show_profiling_report("profiling/bank_marketing.html")
