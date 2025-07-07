import numpy as np

def calculate_cost(y_true, y_pred):
    """
    Calculation of total OPEX based on predictions.

    False Positive costs 550 €, False Negative costs 3350 €.
    """
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    costs = (fp * 550) + (fn * 3350)
    return costs
