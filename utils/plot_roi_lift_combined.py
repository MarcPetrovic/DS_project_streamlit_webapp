import matplotlib.pyplot as plt
import pandas as pd

def plot_decile_lift_roi(df_logreg, df_xgb):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
    fig.suptitle("Lift and ROI per Decile", fontsize=16)

    # Sortiere Deciles korrekt absteigend (9 = höchster Score)
    df_logreg = df_logreg.sort_values(by='decile', ascending=False)
    df_xgb = df_xgb.sort_values(by='decile', ascending=False)

    # Berechne globale ROI-Skala mit Sicherheitsabstand
    roi_all = pd.concat([df_logreg['roi'], df_xgb['roi']])
    roi_min = roi_all.min() - 0.5
    roi_max = roi_all.max() + 0.5

    # === Logistic Regression ===
    ax1 = axes[0]
    ax1.bar(df_logreg['decile'].astype(str), df_logreg['lift'], color="#097a80")
    ax1.set_title("Logistic Regression")
    ax1.set_xlabel("Decile (9 = highest score)")
    ax1.set_ylabel("Lift")
    ax1.grid(True, axis="y", linestyle="--", alpha=0.5)

    ax1b = ax1.twinx()
    ax1b.plot(df_logreg['decile'].astype(str), df_logreg['roi'], color="#C00000", marker='o', label="ROI")
    ax1b.set_ylabel("ROI", color='black')  # Farbneutral für Vergleichbarkeit
    ax1b.set_ylim(roi_min, roi_max)

    # === XGBoost ===
    ax2 = axes[1]
    ax2.bar(df_xgb['decile'].astype(str), df_xgb['lift'], color="#191919")
    ax2.set_title("XGBoost")
    ax2.set_xlabel("Decile (9 = highest score)")
    ax2.grid(True, axis="y", linestyle="--", alpha=0.5)

    ax2b = ax2.twinx()
    ax2b.plot(df_xgb['decile'].astype(str), df_xgb['roi'], color="#FF9900", marker='o', label="ROI")
    ax2b.set_ylabel("ROI", color='black')
    ax2b.set_ylim(roi_min, roi_max)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    return fig

