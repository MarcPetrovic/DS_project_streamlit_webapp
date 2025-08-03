import matplotlib.pyplot as plt

def plot_decile_lift_roi(logreg_df, xgb_df):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

    # ROI-Grenzen global berechnen
    roi_all = pd.concat([df_logreg['roi'], df_xgb['roi']])
    roi_min = roi_all.min()
    roi_max = roi_all.max()

    # Plot: Logistic Regression
    ax1 = axes[0]
    ax1.bar(df_logreg['decile'], df_logreg['lift'], color="#097a80", label="Lift")
    ax1.set_xlabel("Decile (0 = highest score)")
    ax1.set_ylabel("Lift")
    ax1.set_title("Logistic Regression")
    ax1.grid(True, axis="y", linestyle="--", alpha=0.5)

    ax1b = ax1.twinx()
    ax1b.plot(df_logreg['decile'], df_logreg['roi'], color="#C00000", marker='o', label="ROI")
    ax1b.set_ylabel("ROI", color="#C00000")
    ax1b.set_ylim(roi_min, roi_max)  # 🔥 Fix gleiche ROI-Skala

    # Plot: XGBoost
    ax2 = axes[1]
    ax2.bar(df_xgb['decile'], df_xgb['lift'], color="#191919", label="Lift")
    ax2.set_xlabel("Decile (0 = highest score)")
    ax2.set_title("XGBoost")
    ax2.grid(True, axis="y", linestyle="--", alpha=0.5)

    ax2b = ax2.twinx()
    ax2b.plot(df_xgb['decile'], df_xgb['roi'], color="#FF9900", marker='o', label="ROI")
    ax2b.set_ylabel("ROI", color="#FF9900")
    ax2b.set_ylim(roi_min, roi_max)  # 🔥 Fix gleiche ROI-Skala
    
    fig.suptitle("Lift & ROI per Decile", fontsize=16)
    plt.tight_layout()
    return fig
