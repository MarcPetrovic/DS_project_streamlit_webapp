import matplotlib.pyplot as plt

def plot_decile_lift_roi(logreg_df, xgb_df):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

    # Logistic Regression
    ax = axes[0]
    df = logreg_df.sort_values('decile')
    ax.bar(df['decile'], df['lift'], color='#097a80')
    ax.set_xlabel('Decile (9 = highest score)')
    ax.set_ylabel('Lift')
    ax.set_title("Logistic Regression")
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax2 = ax.twinx()
    ax2.plot(df['decile'], df['roi'], color='#C00000', marker='o')
    ax2.set_ylabel("ROI")

    # XGBoost
    ax = axes[1]
    df = xgb_df.sort_values('decile')
    ax.bar(df['decile'], df['lift'], color='#191919')
    ax.set_xlabel('Decile (9 = highest score)')
    ax.set_title("XGBoost")
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax2 = ax.twinx()
    ax2.plot(df['decile'], df['roi'], color='#FF9900', marker='o')
    ax2.set_ylabel("ROI")

    fig.suptitle("Lift & ROI per Decile", fontsize=16)
    plt.tight_layout()
    return fig
