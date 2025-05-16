import streamlit as st

def show_github_image(image_filename: str, repo_url: str, caption=None):
    """
    Zeigt ein Bild aus einem GitHub-Repository an.
    
    :param image_filename: Pfad im Repo (z. B. "images/demo.png")
    :param repo_url: GitHub-Repo-Link ohne /blob (z. B. https://github.com/user/repo)
    :param caption: Optionaler Bildtitel
    """
    raw_url = repo_url.replace("github.com", "raw.githubusercontent.com").replace("/blob", "") + f"/main/{image_filename}"
    st.image(raw_url, caption=caption, use_container_width=True)
