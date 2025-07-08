from sklearn.metrics import f1_score, precision_recall_curve, roc_curve
import numpy as np
from utils.cost_calc import calculate_cost

def find_best_threshold(y_true, y_proba, strategy='f1', cost_function=None):
    """
    Calculation of the best threshold based on selected strategy.

    Args:
        y_true (array-like): empirical labels.
        y_proba (array-like): predicted probability for class 1 (z. B. predict_proba[:, 1]).
        strategy (str): Eine der folgenden Optionen:
            - 'f1': Maximum of F1-Scores
            - 'cost': Minimum of costs opex
            - 'youden': Youden-Index (Sensitivität + Spezifität - 1)
            - 'pr_gap': Minimum of difference between Precision and Recall
            - 'default': Standard threshold of 0.5
        cost_function (callable, optional): Required for strategy='cost'.

    Returns:
        float: Optimum Threshold.
    """
    if strategy == 'f1':
        precision, recall, thresholds = precision_recall_curve(y_true, y_proba)
        thresholds = np.append(thresholds, 1.0)  # Längenangleichung
        f1_scores = 2 * (precision * recall) / (precision + recall + 1e-6)
        best_idx = np.argmax(f1_scores)
        return thresholds[best_idx]
    
    elif strategy == 'cost':
        if cost_function is None:
            raise ValueError("cost_function must be provided for strategy='cost'")
        thresholds = np.linspace(0, 1, 200)
        costs = [cost_function(y_true, (y_proba >= t).astype(int)) for t in thresholds]
        return thresholds[np.argmin(costs)]
    
    elif strategy == 'youden':
        fpr, tpr, thresholds = roc_curve(y_true, y_proba)
        youden_index = tpr - fpr
        best_idx = np.argmax(youden_index)
        return thresholds[best_idx]

    elif strategy == 'pr_gap':
        precision, recall, thresholds = precision_recall_curve(y_true, y_proba)
        thresholds = np.append(thresholds, 1.0)
        diff = np.abs(precision - recall)
        best_idx = np.argmin(diff)
        return thresholds[best_idx]

    elif strategy == 'default':
        return 0.5

    else:
        raise ValueError(f"Unknown strategy: {strategy}")
