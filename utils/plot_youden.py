import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc

def plot_roc_with_youden(y_true, probs_logreg, probs_xgb):
    fpr_logreg, tpr_logreg, thresholds_logreg = roc_curve(y_true, probs_logreg)
    fpr_xgb, tpr_xgb, thresholds_xgb = roc_curve(y_true, probs_xgb)

    # Youden's J = Sensitivity + Specificity - 1 = TPR - FPR
    j_scores_logreg = tpr_logreg - fpr_logreg
    optimal_idx_logreg = np.argmax(j_scores_logreg)
    optimal_threshold_logreg = thresholds_logreg[optimal_idx_logreg]

    j_scores_xgb = tpr_xgb - fpr_xgb
    optimal_idx_xgb = np.argmax(j_scores_xgb)
    optimal_threshold_xgb = thresholds_xgb[optimal_idx_xgb]

    roc_auc_logreg = auc(fpr_logreg, tpr_logreg)
    roc_auc_xgb = auc(fpr_xgb, tpr_xgb)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(fpr_logreg, tpr_logreg, color='#097a80', lw=2, linestyle='-.',
            marker='v', markerfacecolor='none', markeredgecolor='#097a80', markersize=1.8,
            label=f'Logistic Regression (AUC = {roc_auc_logreg:.3f})')
    ax.plot(fpr_xgb, tpr_xgb, color='#191919', lw=2, linestyle='-.',
            label=f'XGBoost (AUC = {roc_auc_xgb:.3f})')
    ax.plot([0, 1], [0, 1], color='#C00000', lw=2, linestyle='--', label='Random (AUC = 0.5)')

    # Optimalpunkte
    ax.scatter(fpr_logreg[optimal_idx_logreg], tpr_logreg[optimal_idx_logreg], color='red', zorder=5,
               label="Optimum Youden’s J (LogReg)")
    ax.scatter(fpr_xgb[optimal_idx_xgb], tpr_xgb[optimal_idx_xgb], color='red', zorder=5)

    ax.annotate(f'Opt. threshold LogReg: {optimal_threshold_logreg:.3f}',
                xy=(fpr_logreg[optimal_idx_logreg], tpr_logreg[optimal_idx_logreg]),
                xytext=(0.25, 0.55),
                arrowprops=dict(facecolor='#097a80', shrink=0.05),
                fontsize=10, color='#097a80')

    ax.annotate(f'Opt. threshold XGBoost: {optimal_threshold_xgb:.3f}',
                xy=(fpr_xgb[optimal_idx_xgb], tpr_xgb[optimal_idx_xgb]),
                xytext=(0.10, 0.85),
                arrowprops=dict(facecolor='#191919', shrink=0.05),
                fontsize=10, color='#191919')

    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('\nROC-Curves – Trade-Off Optimization (Youden’s J)\n', fontsize=16, fontweight='bold')
    ax.legend(loc='lower right')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_facecolor('lightgrey')
    ax.grid(True, linestyle='--', color='grey')

    return fig
