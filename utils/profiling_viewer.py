import streamlit as st

def show_profiling_report(html_path: str):
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=1000, scrolling=True)
