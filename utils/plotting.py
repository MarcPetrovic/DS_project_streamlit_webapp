import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

def plot_cat_distribution_vs_success(X, y, feature, bins=None, title=None, sig_threshold=0.05, ci_confidence=0.95):
    """
    Creates a combined bar and line chart for a categorical (or grouped) feature.
    
    Shows:
    - Distribution of characteristics (primary axis)
    - Success rate (secondary axis)
    - Confidence intervals (95%)
    - Marking of significant deviations from the overall success rate
    
    Parameters:
    - X: pd.DataFrame with input features
    - y: pd.Series with binary target variable (0/1)
    - feature: Feature name as string
    - bins: List for grouping (optional)
    - title: Plot title (optional)
    - sig_threshold: Significance threshold in percentage points (default: 0.05 = 5pp)
    - ci_confidence: Confidence level (default: 0.95)
    """

    # Feature-pre-preparation
    if bins:
        feature_binned = pd.cut(X[feature], bins=bins)
    else:
        feature_binned = X[feature].astype(str)
    
    # distribution calculation
    distribution = feature_binned.value_counts(normalize=True).sort_index()

    counts = feature_binned.value_counts().sort_index()
    success_counts = pd.crosstab(feature_binned, y)[1].sort_index()

    # success ratio per feature value
    success_ratio = success_counts / counts
    #pd.crosstab(feature_binned, y, normalize='index')[1].sort_index()

    # average success ration calculation
    avg_success = y.mean()

    # ci calculation (binomial, z-Wert)
    z = {0.90: 1.64, 0.95: 1.96, 0.99: 2.58}.get(ci_confidence, 1.96)
    ci = z * np.sqrt((success_ratio * (1 - success_ratio)) / counts)
    
    # Plot pre-preparation
    fig, ax1 = plt.subplots(figsize=(8, 8))
    ax2 = ax1.twinx()

    # bar plot for: distribution
    distribution.plot(kind="bar", color='#097a80', ax=ax1#, width=0.8
                      , rot=25, edgecolor='#d9d9d9', label=f'Distribution of {feature} clustered')

    # line chart for: success ratio per feature value
    ax2.errorbar(
        x=np.arange(len(success_ratio)),
        y=success_ratio.values,
        yerr=ci.values, 
        marker='o', 
        linestyle='-.', 
        color='#191919',
        linewidth=2.2, 
        label=f'Success Ratio of {feature}'
    )

    # line chart for: average success ratio
    avg_success_series = pd.Series(avg_success, index=success_ratio.index)
    avg_success_series.plot(kind='line', marker='o', linestyle='--', color='#C00000',
                        linewidth=2.2, ax=ax2, label='Avg Success Ratio')

    sig_mask = (np.abs(success_ratio - avg_success) >= sig_threshold)
    for idx, (label, sig) in enumerate(zip(success_ratio.index, sig_mask)):
        if sig:
            ax2.text(idx, success_ratio[label] + 0.015, "*", ha='center', fontsize=16, color='red')
    
    # values for the axes
    ax1.set_ylabel('distribution (%)')
    ax2.set_ylabel('success ratios (%)')
    ax1.set_ylim([0.0, 0.9])
    ax2.set_ylim([0.0, 0.75])

    # definition of legend, facecolor etc
   # ax1.legend(loc='upper left')
   # ax2.legend(loc='upper right')
    ax1.set_facecolor('lightgrey')
    ax2.set_facecolor('lightgrey')
    ax2.grid(None)

    from matplotlib.lines import Line2D
    sig_legend = Line2D([], [], color='red', marker='*', linestyle='None',
                        markersize=14, label=f'Significant Deviation (±{int(sig_threshold*100)}pp)')
    
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    
    ax2.legend(handles=handles1 + handles2 + [sig_legend],
               labels=labels1 + labels2 + [sig_legend.get_label()],
               loc='upper left')
    
    # def of title
    if not title:
        title = f"Success Profile for {feature.title()}"
    plt.title(title, fontsize=16, fontweight='bold')
    #plt.xticks(rotation=25)
    plt.tight_layout()
    plt.show()
