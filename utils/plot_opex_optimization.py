import numpy as np
import matplotlib.pyplot as plt
from utils.cost_calc import calculate_cost
from utils.thresholding import find_best_threshold  # Stelle sicher, dass das korrekt importiert ist

def plot_opex_optimization(y_true, y_proba_logreg, y_proba_xgb, steps=200, language="de"):
    """
    Erzeugt einen Plot zur OPEX-Kostenoptimierung basierend auf dem Schwellenwert.
    
    Args:
        y_true (array-like): Wahre Labels
        y_proba_logreg (array-like): Wahrscheinlichkeiten von Logistic Regression
        y_proba_xgb (array-like): Wahrscheinlichkeiten von XGBoost
        steps (int): Anzahl Threshold-Stufen
        language (str): 'de' für Deutsch, 'en' für Englisch

    Returns:
        matplotlib.figure.Figure: Matplotlib-Figur für Streamlit
    """
    thresholds = np.linspace(0, 1, steps)

    # OPEX-Kosten berechnen (durch 1000 teilen für bessere Lesbarkeit)
    costs_logreg = [calculate_cost(y_true, (y_proba_logreg >= t).astype(int)) / 1000 for t in thresholds]
    best_threshold_logreg = find_best_threshold(y_true, y_proba_logreg, strategy='cost', cost_function=calculate_cost)

    costs_xgb = [calculate_cost(y_true, (y_proba_xgb >= t).astype(int)) / 1000 for t in thresholds]
    best_threshold_xgb = find_best_threshold(y_true, y_proba_xgb, strategy='cost', cost_function=calculate_cost)

    # Label je nach Sprache
    if language == "de":
        cost_label = "Total OPEX (TSD€)"
        title_logreg = "Threshold-Optimierung\nLogistische Regression (OPEX)"
        title_xgb = "Threshold-Optimierung\nXGBoost (OPEX)"
        xlabel = "Threshold"
        ylabel = "Gesamtkosten (TSD€)"
    else:
        cost_label = "Total OPEX (k€)"
        title_logreg = "Threshold Optimization\nLogistic Regression (OPEX)"
        title_xgb = "Threshold Optimization\nXGBoost (OPEX)"
        xlabel = "Threshold"
        ylabel = "Total Cost (k€)"

    # Plot erstellen
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Logistic Regression
    axes[0].plot(thresholds, costs_logreg, color='#C00000', label=cost_label)
    axes[0].axvline(best_threshold_logreg, linestyle='--', lw=2, color='#097a80',
                    label=f'Opt. Threshold = {best_threshold_logreg:.2f}')
    axes[0].set_title(title_logreg)
    axes[0].set_xlabel(xlabel)
    axes[0].set_ylabel(ylabel)
    axes[0].grid(True, linestyle='--', color='grey')
    axes[0].set_facecolor('lightgrey')
    axes[0].legend()

    # XGBoost
    axes[1].plot(thresholds, costs_xgb, color='#C00000', label=cost_label)
    axes[1].axvline(best_threshold_xgb, linestyle='-.', lw=2, color='#191919',
                    label=f'Opt. Threshold = {best_threshold_xgb:.2f}')
    axes[1].set_title(title_xgb)
    axes[1].set_xlabel(xlabel)
    axes[1].set_ylabel(ylabel)
    axes[1].grid(True, linestyle='--', color='grey')
    axes[1].set_facecolor('lightgrey')
    axes[1].legend()

    fig.tight_layout()
    return fig

