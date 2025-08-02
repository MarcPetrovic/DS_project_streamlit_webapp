import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Dummy train_and_predict Funktion (ersetzt du mit deinem echten Code)
def train_and_predict(model_type="logistic"):
    np.random.seed(42)
    y_test = np.random.binomial(1, 0.2, size=1000)
    # Simulierte Wahrscheinlichkeiten für Logistic und XGBoost
    if model_type == "logistic":
        probs = np.clip(np.random.normal(0.2, 0.1, 1000), 0, 1)
    else:
        probs = np.clip(np.random.normal(0.25, 0.12, 1000), 0, 1)
    return None, probs, y_test

@st.cache_resource
def get_predictions():
    _, logreg_probs, y_test = train_and_predict(model_type="logistic")
    _, xgb_probs, _ = train_and_predict(model_type="xgboost")
    return logreg_probs, xgb_probs, y_test

def create_stats(y_probs, bands):
    df = pd.DataFrame({'y_probs': y_probs, 'band': bands})
    stats = df.groupby('band').agg(
        n=('y_probs', 'count'),
        mean_prob=('y_probs', 'mean'),
        min_prob=('y_probs', 'min'),
        max_prob=('y_probs', 'max'),
    ).reset_index()
    stats['label'] = stats.apply(lambda r: f"{r.min_prob:.2f} - {r.max_prob:.2f}", axis=1)
    return stats

def plot_score_bands(stats_df_log, stats_df_xgb, selected_criteria, threshold):
    col1, col2 = st.columns(2)

    def plot_single(ax, stats_df, model_name, color):
        bars = ax.bar(stats_df['band'], stats_df['n'], color=color, alpha=0.7)
        ax.set_xlabel("Score-Band")
        ax.set_ylabel("Anzahl Fälle")
        ax.set_title(f"Score-Bänder ({model_name})")

        # Labels über Balken
        for bar, label in zip(bars, stats_df['label']):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, label, ha='center', va='bottom', fontsize=8, rotation=45)

        # Y-Achse fix auf 4000 setzen
        ax.set_ylim(0, 4000)

        # Optional: Hervorhebung Top 3 Bänder mit >= threshold Fälle
        if selected_criteria.get("top3", False):
            top3_bands = stats_df.sort_values(by='mean_prob', ascending=False).head(3)['band'].tolist()
            for i, bar in enumerate(bars):
                if i in top3_bands:
                    bar.set_edgecolor('red')
                    bar.set_linewidth(2)

        # Optional: Exponentieller Verlauf als Trendlinie
        if selected_criteria.get("exp", False):
            x = stats_df['band']
            y = stats_df['mean_prob']
            # Fit exponentiell: y ~ a * exp(bx)  → linearize log(y) ~ bx + c
            y = y.clip(lower=1e-6)  # keine Nullen für log
            z = np.polyfit(x, np.log(y), 1)
            exp_fit = np.exp(np.poly1d(z)(x))
            ax.plot(x, exp_fit * max(stats_df['n']), 'r--', label='Exp Trend (skaliert)')
            ax.legend()

    with col1:
        fig, ax = plt.subplots(figsize=(6,4))
        plot_single(ax, stats_df_log, "Logistic Regression", "skyblue")
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(6,4))
        plot_single(ax, stats_df_xgb, "XGBoost", "orange")
        st.pyplot(fig)


def show():
    st.header("Conclusion & Discussion")
    #st.write("Hier formulierst du deine Schlussfolgerungen und Diskussion.")
    st.markdown("""
    Im Rahmen dieses Projektes wurde die Klassifikation für den Abschluss eines Festgeldvertrages optimiert.  
    Ein Aspekt, der **nicht Bestandteil** war, ist die Kalibrierung der Score-Bänder basierend auf den Trefferwahrscheinlichkeiten der Modelle.
    """)

    # Checkbox zwischen Absatz 1 und 2
    show_dialog = st.checkbox("🧠 Optional: Score-Binning-Dialog anzeigen")

    st.markdown("""
    Abschließend werden hier einige Gedanken und erste Schritte zu einem möglichen Kalibrierungsprozess gezeigt.
    """)

    if show_dialog:

        st.markdown("### 1️⃣ Threshold auswählen")
        # Modelle laden
        logreg_probs, xgb_probs, y_test = get_predictions()

        model_choice = st.selectbox("Modellauswahl", ["logistic", "xgboost"])
        y_probs = logreg_probs if model_choice == "logistic" else xgb_probs

        threshold = st.slider("Threshold wählen", 0.0, 1.0, 0.5, 0.01)

        st.markdown("### 2️⃣ Score-Bänder initial erstellen")
        n_bins = st.radio("Anzahl Score-Bänder", [10, 20])

        # Score Bänder erzeugen
        bands_log = pd.qcut(logreg_probs, q=n_bins, labels=False, duplicates="drop")
        bands_xgb = pd.qcut(xgb_probs, q=n_bins, labels=False, duplicates="drop")

        stats_log = create_stats(logreg_probs, bands_log)
        stats_xgb = create_stats(xgb_probs, bands_xgb)

        # Schritt 3: Optimierungskriterien auswählen
        st.markdown("### 3️⃣ Optimierungskriterien auswählen")
        opt_a = st.checkbox("A) Treffer ≥ Threshold in Top 3 Bändern")
        opt_b = st.checkbox("B) Mittelwert der Wahrscheinlichkeiten erhalten")
        opt_c = st.checkbox("C) Exponentieller Verlauf der Trefferwahrscheinlichkeiten")
        opt_d = st.checkbox("D) Gleichmäßige Verteilung der Fälle")

        selected_criteria = {
            "top3": opt_a,
            "mean": opt_b,
            "exp": opt_c,
            "equal": opt_d
        }

        # Plot immer anzeigen, sobald n_bins + threshold gesetzt sind
        plot_score_bands(stats_log, stats_xgb, selected_criteria, threshold)
