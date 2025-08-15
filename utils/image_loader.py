import streamlit as st
import requests

def show_github_image(image_filename: str, repo_url: str, caption=None, branch="main"):
    """
    Zeigt ein Bild aus einem GitHub-Repository an.

    :param image_filename: Pfad im Repo (z. B. "images/demo.png")
    :param repo_url: GitHub-Repo-Link (z. B. https://github.com/user/repo)
    :param caption: Optionaler Bildtitel
    :param branch: Branch-Name (Standard: "main")
    """
    if "github.com" not in repo_url:
        st.error("Ungültige GitHub-URL.")
        return

    # Extrahiere Pfad-Komponenten
    repo_path = repo_url.replace("https://github.com/", "")
    raw_url = f"https://raw.githubusercontent.com/{repo_path}/{branch}/{image_filename}"

    # Prüfen, ob Bild existiert (HEAD oder GET)
    try:
        response = requests.head(raw_url)
        if response.status_code != 200:
            st.warning(f"Bild konnte nicht geladen werden: {raw_url}")
        else:
            st.image(raw_url, caption=caption, use_container_width=True)
            #st.image(raw_url, caption=caption, width=600)  # z. B. 600 Pixel Breite
    except Exception as e:
        st.error(f"Fehler beim Laden des Bildes: {e}")
