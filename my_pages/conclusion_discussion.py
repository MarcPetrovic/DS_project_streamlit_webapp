import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from utils.my_colormaps import my_cmap_r, cmap_4, my_cmap
from utils.model_pipeline import train_and_predict, train_model

# --------------------------
# Caching: Modelle & Daten
# --------------------------

@st.cache_resource
def get_predictions():
    _, logreg_probs, y_test = train_and_predict(model_type="logistic")
    _, xgb_probs, _ = train_and_predict(model_type="xgboost")
    return logreg_probs, xgb_probs, y_test

@st.cache_resource
def get_model_fit():
    logreg_model, X_train, X_test, y_train, y_test = train_model(model_type="logistic")
    xgb_model, _, _, _, _ = train_model(model_type="xgboost")
    return logreg_model, xgb_model, X_train, y_train

# --------------------------
# Score-Binning Funktion
# --------------------------

def threshold_aware_binning(y_probs, n_bins, threshold, top_n=3):
    y_probs = pd.Series(y_probs).reset_index(drop=True)
    df = pd.DataFrame({'y_probs': y_probs})

    above_thresh = df[df['y_probs'] >= threshold].copy()
    below_thresh = df[df['y_probs'] < threshold].copy()

    if len(above_thresh) >= top_n:
        above_thresh['band'] = pd.qcut(above_thresh['y_probs'], q=top_n, labels=range(top_n), duplicates='drop')
    else:
        above_thresh['band'] = 0

    remaining_bins = n_bins - top_n
    if len(below_thresh) >= remaining_bins and remaining_bins > 0:
        below_thresh['band'] = pd.qcut(below_thresh['y_probs'], q=remaining_bins, labels=range(top_n, n_bins), duplicates='drop')
    else:
        below_thresh['band'] = top_n

    combined = pd.concat([above_thresh, below_thresh]).sort_index()
    return combined['band'].astype(int)

# --------------------------
# Visualisierung
# --------------------------

def plot_score_bands(stats_df_log, stats_df_xgb, selected_criteria, threshold):
    col1, col2 = st.columns(2)

    def plot_single(ax, stats_df, model_name, color):
        bars = ax.bar(stats_df['band'], stats_df['n'], color=color, alpha=0.8)
        ax.set_xlabel("Score-Band")
        ax.set_ylabel("Anzahl Fälle")
        ax.set_title(f"Score-Bänder ({model_name})")
        ax.set_ylim(0, 3000)

        for bar, label in zip(bars, stats_df['label']):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, label, ha='center', va='bottom', fontsize=8, rotation=45)

        if selected_criteria.get("exp", False):
            x = stats_df['band']
            y = stats_df['mean_prob'].clip(lower=1e-6)
            z = np.polyfit(x, np.log(y), 1)
            exp_fit = np.exp(np.poly1d(z)(x))
            ax.plot(x, exp_fit * 4000, 'r--', label='Exp. Trend (skaliert)')
            ax.legend()

    with col1:
        fig, ax = plt.subplots(figsize=(6, 4))
        plot_single(ax, stats_df_log, "Logistic Regression", "#4C72B0")
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(6, 4))
        plot_single(ax, stats_df_xgb, "XGBoost", "#DD8452")
        st.pyplot(fig)

# --------------------------
# Haupt-UI
# --------------------------

def show():
    st.header("Conclusion & Discussion")
    #st.write("Hier formulierst du deine Schlussfolgerungen und Diskussion.")
    st.markdown("""
    Im Rahmen dieses Projektes wurde die Klassifikation für den Abschluss eines Festgeldvertrages optimiert.  
    Ein Aspekt, der **nicht Bestandteil** war, ist die Kalibrierung der Score-Bänder basierend auf den Trefferwahrscheinlichkeiten der Modelle.
    """)
    
    show_score_binning_dialog = st.checkbox("🧠 Erweiterte Score-Band Kalibrierung anzeigen")

    if show_score_binning_dialog:
        st.markdown("### Schritt 1: Threshold auswählen")
        threshold = st.slider("Threshold für 'positiv' (Youden J oder manuell)", 0.01, 1.0, 0.15, 0.01)

        st.markdown("### Schritt 2: Anzahl Score-Bänder wählen")
        n_bins = st.radio("Anzahl Score-Bänder:", options=[10, 20], horizontal=True)

        st.markdown("### Schritt 3: Optimierungskriterien auswählen")
        selected_criteria = {
            "top3": st.checkbox("A) Positive Fälle auf erste 3 Score-Bänder verteilen (≥ Threshold)", value=True),
            "mean": st.checkbox("B) Mittelwert der Wahrscheinlichkeiten erhalten"),
            "exp": st.checkbox("C) Exponentiellen Verlauf der Wahrscheinlichkeiten erzeugen"),
            "even": st.checkbox("D) Möglichst gleichmäßige Verteilung der Fallzahlen")
        }

        # Hole Wahrscheinlichkeiten
        logreg_probs, xgb_probs, y_test = get_predictions()

        # Score-Binning mit Threshold-Logik
        if selected_criteria["top3"]:
            bands_log = threshold_aware_binning(logreg_probs, n_bins, threshold, top_n=3)
            bands_xgb = threshold_aware_binning(xgb_probs, n_bins, threshold, top_n=3)
        else:
            bands_log = pd.qcut(logreg_probs, q=n_bins, labels=False, duplicates="drop")
            bands_xgb = pd.qcut(xgb_probs, q=n_bins, labels=False, duplicates="drop")

        # Statistiken pro Band
        def compute_stats(y_probs, bands):
            df = pd.DataFrame({'prob': y_probs, 'band': bands})
            stats_df = df.groupby('band').agg(
                mean_prob=('prob', 'mean'),
                n=('prob', 'count'),
                min_prob=('prob', 'min'),
                max_prob=('prob', 'max')
            ).reset_index()
            stats_df['label'] = stats_df['min_prob'].round(2).astype(str) + " – " + stats_df['max_prob'].round(2).astype(str)
            return stats_df

        stats_log = compute_stats(logreg_probs, bands_log)
        stats_xgb = compute_stats(xgb_probs, bands_xgb)

        # Plots anzeigen
        st.markdown("### Visualisierung der Score-Bänder")
        plot_score_bands(stats_log, stats_xgb, selected_criteria, threshold)

    st.markdown("----")
