import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import numpy as np

def plot_roc_curves_with_early_area(y_true, probs_logreg, probs_xgb, strategy_label=None):
    fpr_logreg, tpr_logreg, _ = roc_curve(y_true, probs_logreg)
    fpr_xgb, tpr_xgb, _ = roc_curve(y_true, probs_xgb)
    
    auc_logreg = auc(fpr_logreg, tpr_logreg)
    auc_xgb = auc(fpr_xgb, tpr_xgb)

        # TPR bei FPR ≈ 0.2
    def get_tpr_at_fpr(target_fpr, fpr, tpr):
        idx = np.argmin(np.abs(fpr - target_fpr))
        return fpr[idx], tpr[idx]

    fpr_target = 0.2
    fpr_logreg_val, tpr_logreg_val = get_tpr_at_fpr(fpr_target, fpr_logreg, tpr_logreg)
    fpr_xgb_val, tpr_xgb_val = get_tpr_at_fpr(fpr_target, fpr_xgb, tpr_xgb)

    fig, ax = plt.subplots(figsize=(8, 6))

    # ROC Curve: Logistic Regression
    ax.plot(fpr_logreg, tpr_logreg, color='#097a80', lw=2, linestyle='-.',
            marker='v', markerfacecolor='none', markeredgecolor='#097a80', markersize=3,
            label=f'Logistic Regression (AUC = {auc_logreg:.3f})')

    # ROC Curve: XGBoost
    ax.plot(fpr_xgb, tpr_xgb, color='#191919', lw=2, linestyle='-.',
            label=f'XGBoost (AUC = {auc_xgb:.3f})')

    # Zufallslinie
    ax.plot([0, 1], [0, 1], color='#C00000', lw=2, linestyle='--', label='Random (AUC = 0.5)')

    # Early Retrieval Area (z. B. FPR <= 0.2)
    ax.fill_between([0, 0.2], [0, 0], [1, 1], color='red', alpha=0.3, label='Early Retrieval Area (FPR ≤ 20%)')

        # TPR-Werte als Marker + Text
    ax.scatter(fpr_logreg_val, tpr_logreg_val, color='#097a80', s=80, edgecolor='white', zorder=5)
    ax.text(fpr_logreg_val + 0.02, tpr_logreg_val, f'TPR @ 20% FPR: {tpr_logreg_val:.3f}', color='#097a80')

    ax.scatter(fpr_xgb_val, tpr_xgb_val, color='#191919', s=80, edgecolor='white', zorder=5)
    ax.text(fpr_xgb_val + 0.02, tpr_xgb_val - 0.05, f'TPR @ 20% FPR: {tpr_xgb_val:.3f}', color='#191919')

    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    title = f'ROC Curves with Early Retrieval\nStrategy: {strategy_label}' if strategy_label else 'ROC Curves with Early Retrieval'
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(loc='lower right')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_facecolor('lightgrey')
    ax.grid(True, linestyle='--', color='grey')

    return fig
