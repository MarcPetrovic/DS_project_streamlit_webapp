import pandas as pd
from utils.compute_metrics import compute_metrics
from utils.find_best_threshold import find_best_threshold
from utils.cost_calc import calculate_cost

def evaluate_all_strategies(y_true, logreg_proba, xgb_proba):
    strategies = ['default', 'cost', 'youden', 'f1', 'pr_gap']
    records = []

    for strategy in strategies:
        kwargs = {"cost_function": calculate_cost} if strategy == "cost" else {}

        # Default threshold (0.5)
        if strategy == "default":
            threshold_logreg = 0.5
            threshold_xgb = 0.5
        else:
            threshold_logreg = find_best_threshold(y_true, logreg_proba, strategy, **kwargs)
            threshold_xgb = find_best_threshold(y_true, xgb_proba, strategy, **kwargs)

        # Compute metrics
        metrics_logreg = compute_metrics(y_true, logreg_proba, threshold_logreg)
        metrics_xgb = compute_metrics(y_true, xgb_proba, threshold_xgb)

        # Append to record list
        records.append({
            "Strategy": strategy.capitalize().replace("_", "-"),
            "Model": "Logistic Regression",
            **metrics_logreg
        })
        records.append({
            "Strategy": strategy.capitalize().replace("_", "-"),
            "Model": "XGBoost",
            **metrics_xgb
        })

    df_summary = pd.DataFrame(records)

    # Kosten in k€
    df_summary["Total Cost (€) (k €)"] = df_summary["Total Cost (€)"] / 1000
    return df_summary
