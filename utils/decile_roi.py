import numpy as np
import pandas as pd

def decile_roi_analysis(y_true, y_probs, threshold, model_name, gain_per_tp=3350, cost_fp=550, cost_fn=3350):
    df = pd.DataFrame({'y_true': y_true, 'y_prob': y_probs})
    df['decile'] = pd.qcut(df['y_prob'], 10, labels=False, duplicates='drop')
    df['y_pred'] = (df['y_prob'] >= threshold).astype(int)

    global_pos_rate = df['y_true'].mean()
    results = []

    for decile in sorted(df['decile'].unique(), reverse=True):
        sub = df[df['decile'] == decile]
        tp = ((sub['y_true'] == 1) & (sub['y_pred'] == 1)).sum()
        fp = ((sub['y_true'] == 0) & (sub['y_pred'] == 1)).sum()
        fn = ((sub['y_true'] == 1) & (sub['y_pred'] == 0)).sum()

        revenue = tp * gain_per_tp
        cost = (fp * cost_fp) + (fn * cost_fn)
        profit = revenue - cost
        roi = profit / cost if cost > 0 else np.nan

        results.append({
            'decile': int(decile),
            'total': len(sub),
            'lift': sub['y_true'].mean() / global_pos_rate,
            'roi': roi,
            'model': model_name
        })

    return pd.DataFrame(results)
