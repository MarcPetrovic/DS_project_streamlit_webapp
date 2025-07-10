import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, f1_score
import numpy as np


def plot_precision_recall_with_f1_thresholds(y_true, y_probs_logreg, y_probs_xgb):
    precision_logreg, recall_logreg, thresholds_logreg = precision_recall_curve(y_true, y_probs_logreg)
    precision_xgb, recall_xgb, thresholds_xgb = precision_recall_curve(y_true, y_probs_xgb)

    # F1 berechnen
    f1_logreg = 2 * (precision_logreg * recall_logreg) / (precision_logreg + recall_logreg + 1e-10)
    f1_xgb = 2 * (precision_xgb * recall_xgb) / (precision_xgb + recall_xgb + 1e-10)

    best_idx_logreg = np.argmax(f1_logreg)
    best_idx_xgb = np.argmax(f1_xgb)

    best_threshold_logreg = thresholds_logreg[best_idx_logreg] if best_idx_logreg < len(thresholds_logreg) else 1.0
    best_threshold_xgb = thresholds_xgb[best_idx_xgb] if best_idx_xgb < len(thresholds_xgb) else 1.0

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(recall_logreg, precision_logreg, color='#097a80', marker='o', label='Logistic Regression')
    ax.plot(recall_xgb, precision_xgb, color='#191919', lw=2, label='XGBoost')

    # Optima markieren
    ax.scatter(recall_logreg[best_idx_logreg], precision_logreg[best_idx_logreg], color='red', zorder=5)
    ax.scatter(recall_xgb[best_idx_xgb], precision_xgb[best_idx_xgb], color='red', zorder=5)

    ax.annotate(f'Threshold F1\nLogReg: {best_threshold_logreg:.3f}',
                xy=(recall_logreg[best_idx_logreg], precision_logreg[best_idx_logreg]),
                xytext=(0.2, 0.34),
                arrowprops=dict(facecolor='#097a80', shrink=0.05),
                fontsize=10, color='#097a80')

    ax.annotate(f'Threshold F1\nXGBoost: {best_threshold_xgb:.3f}',
                xy=(recall_xgb[best_idx_xgb], precision_xgb[best_idx_xgb]),
                xytext=(0.6, 0.7),
                arrowprops=dict(facecolor='#191919', shrink=0.05),
                fontsize=10, color='#191919')

    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_facecolor("lightgrey")
    ax.set_title("Precision–Recall Curve\nOptimized via F1-Score", fontsize=14, fontweight="bold")
    ax.grid(True, linestyle="--", color="grey")
    ax.legend(loc="lower left")

    return fig
