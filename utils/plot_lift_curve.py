import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_lift_curve_with_ci(y_true, y_probs, model_name, color, ax=None, n_bootstraps=1000, ci=0.95):
    """
    Plot a lift curve with confidence intervals onto a given matplotlib axis (ax).
    If no axis is provided, a new one is created. Returns the ax.
    """
    data = pd.DataFrame({'y_true': y_true, 'y_prob': y_probs})
    data = data.sort_values(by='y_prob', ascending=False).reset_index(drop=True)
    total_positives = data['y_true'].sum()

    def calc_lift(df):
        df['cumulative_positives'] = df['y_true'].cumsum()
        proportions = np.arange(1, len(df) + 1) / len(df)
        lift = df['cumulative_positives'] / (proportions * total_positives)
        return proportions, lift

    proportions, lift = calc_lift(data)

    # Bootstrapping für CI
    boot_lifts = []
    for _ in range(n_bootstraps):
        sample = data.sample(frac=1, replace=True).reset_index(drop=True)
        _, boot_lift = calc_lift(sample)
        boot_lifts.append(boot_lift.values)
    boot_lifts = np.array(boot_lifts)

    lower_bound = np.percentile(boot_lifts, (1 - ci) / 2 * 100, axis=0)
    upper_bound = np.percentile(boot_lifts, (1 + ci) / 2 * 100, axis=0)

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(proportions, lift, label=model_name, color=color)
    ax.fill_between(proportions, lower_bound, upper_bound, color=color, alpha=0.2)
    return ax
