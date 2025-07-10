import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from utils.my_colormaps import my_cmap_r  # dein eigenes Farbschema

def plot_confusion_matrices(y_true, y_pred, model_name="", strategy="", cmap=my_cmap_r):
    cm_abs = confusion_matrix(y_true, y_pred)
    cm_rel = cm_abs.astype("float") / cm_abs.sum(axis=1)[:, np.newaxis]
    accuracy = accuracy_score(y_true, y_pred)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Absolute Matrix
    sns.heatmap(cm_abs, annot=True, fmt='d', ax=axes[0], cmap=cmap,
                xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'],
                linewidths=.3, square=True, cbar=True)
    axes[0].set_title("Confusion Matrix (Absolute)", size = 14)
    axes[0].set_xlabel("Predicted label")
    axes[0].set_ylabel("Actual label")
    
    # Relative Matrix
    sns.heatmap(cm_rel, annot=True, fmt='.3f', ax=axes[1], cmap=cmap,
                xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'],
                linewidths=0.3, square=True, cbar=True)
    axes[1].set_title("Confusion Matrix (Relative)", size = 14)
    axes[1].set_xlabel("Predicted label")
    axes[1].set_ylabel("Actual label")

    fig.suptitle(
        f"{model_name} – {strategy} Strategy\nAccuracy: {accuracy:.3f}",
        fontsize=16
    )
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    return fig
