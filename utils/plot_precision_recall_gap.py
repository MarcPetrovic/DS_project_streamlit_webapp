import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_recall_curve

def plot_precision_recall_gap(y_true, prob_logreg, prob_xgb):
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    for i, (probs, model_name, color_p, color_r) in enumerate([
        (prob_logreg, "Logistic Regression", "#C00000", "#424242"),
        (prob_xgb, "XGBoost", "#1976D2", "#388E3C")
    ]):
        precision, recall, thresholds = precision_recall_curve(y_true, probs)
        diff = np.abs(precision - recall)
        optimal_idx = np.argmin(diff)
        optimal_threshold = thresholds[optimal_idx]

        ax[i].plot(thresholds, precision[:-1], label='Precision', color=color_p, linestyle='--')
        ax[i].plot(thresholds, recall[:-1], label='Recall', color=color_r)
        ax[i].axvline(x=optimal_threshold, color='#097a80', linestyle='--', linewidth=2,
                      label=f'Opt. Threshold: {optimal_threshold:.3f}')
        ax[i].set_title(f"Precision–Recall Gap Minimization\n{model_name}", fontsize=14)
        ax[i].set_xlabel("Thresholds")
        ax[i].set_ylabel("Precision / Recall")
        ax[i].set_xlim(0, 1)
        ax[i].set_ylim(0, 1)
        ax[i].legend()
        ax[i].grid(True, linestyle='--', color='grey')
        ax[i].set_facecolor('lightgrey')

    fig.tight_layout()
    return fig
