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
    # Lokaler Pfad zur HTML-Datei
    local_path = "profiling/profiling_report.html"

    if os.path.exists(local_path):
        # Relativen Pfad für Streamlit freigeben
        st.markdown(f"""
            <a href="{local_path}" target="_blank">
                👉 Profiling Report in neuem Tab öffnen
            </a>
        """, unsafe_allow_html=True)
    else:
        st.warning("Profiling-Report wurde nicht gefunden.")

    #show_profiling_report("profiling/bank_marketing.html")

