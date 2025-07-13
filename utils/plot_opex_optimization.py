import numpy as np
import matplotlib.pyplot as plt
from utils.cost_calc import calculate_cost
from utils.find_best_threshold import find_best_threshold  

def plot_opex_optimization(y_true, y_proba_logreg, y_proba_xgb, steps=200):
    """
    Erzeugt einen Vergleichsplot zur Schwellenwertoptimierung bzgl. OPEX-Kosten
    für Logistic Regression und XGBoost.

    Args:
        y_true (array-like): Wahre Labels
        y_proba_logreg (array-like): Vorhersagewahrscheinlichkeiten LogReg
        y_proba_xgb (array-like): Vorhersagewahrscheinlichkeiten XGBoost
        steps (int): Anzahl der Threshold-Stufen

    Returns:
        matplotlib.figure.Figure: Die erzeugte Figure zur Einbindung in Streamlit
    """
    thresholds = np.linspace(0, 1, steps)

    # === Logistic Regression ===
    costs_logreg = [calculate_cost(y_true, (y_proba_logreg >= t).astype(int)) for t in thresholds]
    best_threshold_logreg = find_best_threshold(y_true, y_proba_logreg, strategy='cost', cost_function=calculate_cost)

    # === XGBoost ===
    costs_xgb = [calculate_cost(y_true, (y_proba_xgb >= t).astype(int)) for t in thresholds]
    best_threshold_xgb = find_best_threshold(y_true, y_proba_xgb, strategy='cost', cost_function=calculate_cost)

    # === Plot ===
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # LogReg
    axes[0].plot(thresholds, costs_logreg, color='#C00000', label="Total OPEX (TSD€)")
    axes[0].axvline(best_threshold_logreg, linestyle='--', lw=2, color='#097a80',
                    label=f'Opt. Threshold = {best_threshold_logreg:.2f}')
    axes[0].set_title("Threshold Optimization\nLogistic Regression (OPEX)")
    axes[0].set_xlabel("Threshold")
    axes[0].set_ylabel("Total OPEX (€)")
    axes[0].grid(True, linestyle='--', color='grey')
    axes[0].set_facecolor('lightgrey')
    axes[0].legend()

    # XGBoost
    axes[1].plot(thresholds, costs_xgb, color='#C00000', label="Total OPEX (TSD€)")
    axes[1].axvline(best_threshold_xgb, linestyle='-.', lw=2, color='#191919',
                    label=f'Opt. Threshold = {best_threshold_xgb:.2f}')
    axes[1].set_title("Threshold Optimization\nXGBoost (OPEX)")
    axes[1].set_xlabel("Threshold")
    axes[1].set_ylabel("Total OPEX (€)")
    axes[1].grid(True, linestyle='--', color='grey')
    axes[1].set_facecolor('lightgrey')
    axes[1].legend()

    fig.tight_layout()
    return fig
