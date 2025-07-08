from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    cohen_kappa_score, matthews_corrcoef, confusion_matrix
)
from utils.cost_calc import calculate_cost

def compute_metrics(y_true, y_proba, threshold):
    """
    Calculation of different metrics based on given probabilities and a threshold.

    Args:
        y_true (array-like): empirical label.
        y_proba (array-like): predicted probability for class 1.
        threshold (float): threshold for binary classification.

    Returns:
        dict: Dictionary with relevant classification metrics.
    """
    y_pred = (y_proba >= threshold).astype(int)
    cm = confusion_matrix(y_true, y_pred)
    TN, FP, FN, TP = cm.ravel()

    return {
        "Threshold": threshold,
        "False Positive Rate": FP / (FP + TN) if (FP + TN) > 0 else 0,
        "False Negative Rate": FN / (FN + TP) if (FN + TP) > 0 else 0,
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall (TPR)": recall_score(y_true, y_pred, zero_division=0),
        "F1 Score": f1_score(y_true, y_pred, zero_division=0),
        "Accuracy": accuracy_score(y_true, y_pred),
        "Cohen's Kappa": cohen_kappa_score(y_true, y_pred),
        "Matthews Corr. Coef.": matthews_corrcoef(y_true, y_pred),
        "Total Cost (€)": calculate_cost(y_true, y_pred)
    }
