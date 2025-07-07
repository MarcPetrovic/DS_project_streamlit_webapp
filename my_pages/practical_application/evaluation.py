import streamlit as st
import io
from utils.image_loader import show_github_image
from utils.data_loader import load_csv_data
import pandas as pd
import numpy as np
from utils.my_colormaps import my_cmap_r
from utils.cost_calc import calculate_costs

def show():
    st.header("evaluation with flexible CSV-Loading")

    st.markdown("""
    ### Data preprocessing according to the key results of data understanding phases
    
    """, unsafe_allow_html=True)


