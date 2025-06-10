import streamlit as st
import os
#from utils.profiling_viewer import show_profiling_report
import matplotlib.pyplot as plt
import numpy as np

from my_colormaps import my_cmap, my_cmap_r, cmap_4

def show():
    st.header("Methods & Data")

    st.write("""
    In diesem Abschnitt wird der Datensatz vorgestellt und analysiert. 
    Der folgende Report wurde automatisch mit [YData Profiling](https://github.com/ydataai/ydata-profiling) erstellt 
    und bietet eine umfassende Übersicht der Datenqualität, Verteilungen und Korrelationen.
    """)
    st.markdown("""
        <a href="https://marcpetrovic.github.io/DS_project_streamlit_webapp/bank_marketing.html" target="_blank">
            📊 Profiling Report öffnen
        </a>
    """, unsafe_allow_html=True)

    #show_profiling_report("profiling/bank_marketing.html")

# Dummy-Daten
x, y, c = zip(*np.random.rand(30, 3) * 4 - 2)

# Plot mit eigener Colormap
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=c, cmap=cmap_4)
plt.colorbar(scatter, ax=ax)
st.pyplot(fig)
