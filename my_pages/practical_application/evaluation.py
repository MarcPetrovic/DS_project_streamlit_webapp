import streamlit as st
from utils.image_loader import show_github_image

def show():
    st.header("Evaluation")
    st.markdown("""
    Sie vergleicht die Leistungskennzahlen von:

Zwei Modelle: Logistic Regression und XGBoost

Mit vier Schwellenstrategien:

"2nd": Vermutlich die Default-Schwelle oder eine auf zweiter Validierungsebene bestimmte (z. B. 0.5 oder ROC-basiert)

"PreRec Distance": Schwelle, bei der Precision ≈ Recall (Differenz minimiert)

"F1": Schwelle mit maximalem F1-Score

"Trade-off": vermutlich Kosten/Nutzen-optimierter Threshold (z. B. erwartete Kosten oder anderes Trade-off-Kriterium)

Bewertungskriterien:
Klassische Metriken: Accuracy, FPRate, FNRate, Precision, Recall, F1

Robuste Metriken: Cohen's Kappa, Matthews Corr.

Business Metric: OPEX (operative Kosten in Mio. €) → sehr wertvoll!

1. Default / 2nd (LogReg & XGB)
Höchste Accuracy (0.895 / 0.899) – aber:

Extrem hohe FN-Rate (0.796 / 0.728) → 80 % bzw. 73 % der positiven Fälle gehen verloren

Recall katastrophal niedrig (0.204 / 0.272)

Precision ist gut (0.635 / 0.650) – aber das täuscht

📌 Fazit: Klassisch optimierter Schwellenwert schneidet bei Imbalance schlecht ab – ignoriert Recall und ist realwirtschaftlich teuer (OPEX: 3.9 / 3.6 Mio. €)

2. Precision ≈ Recall (Distance-Methode)
Recall deutlich höher (0.476 / 0.502)

Precision gesunken (0.476 / 0.502) → aber ausgeglichen

F1-Score verbessert (0.476 / 0.502)

OPEX reduziert (2.91 / 2.77 Mio. €) – fast 1 Mio. günstiger

📌 Fazit: Gute Balance – ein robuster Kompromiss zwischen Fehlerarten und auch ökonomisch sinnvoll.

3. F1-Optimierung
Maximiert F1 (0.486 / 0.511)

Recall höher (0.518 / 0.529), Precision niedriger

OPEX weiter reduziert (2.78 / 2.67 Mio. €)

📌 Fazit: Optimal, wenn du F1 als Zielgröße willst – sehr gute Wahl für harmonischen Kompromiss, besser als Distance in vielen Fällen.

Das heißt: Die "Trade-off"-Spalte in deiner Tabelle basiert auf dem Youden’s J-Index, also:

Youden’s J = TPR – FPR = Sensitivität – 1 – Spezifität

Ziel: Schwelle mit maximaler Trennschärfe zwischen Positiven und Negativen.
    
✅ Stärken
Recall ist am höchsten → viele tatsächliche Positivfälle erkannt (niedrige FN-Rate).

Dadurch geringste OPEX-Kosten → sinnvoll bei kritischen Positivklassen.

XGBoost schafft sogar besseren Kompromiss (weniger False Positives als LogReg).

⚠️ Schwächen
Precision bricht ein → viele False Positives (z. B. LogReg FPRate = 17.4 %).

Kann gefährlich sein, wenn FPs auch teuer sind (z. B. ungewollte medizinische Interventionen, falsche Kreditzusagen etc.).

Youden’s J ignoriert Klassenverhältnis → ist nicht ideal für stark unbalancierte Daten, aber: funktioniert hier gut, weil Recall wirtschaftlich am wichtigsten ist.

🧩 Fazit: Youden als Trade-off in deinem Fall
Obwohl theoretisch weniger geeignet bei Imbalance, hat sich Youden in deinem Fall praktisch als wirtschaftlich beste Methode gezeigt.

Der Grund: Dein Businessziel (OPEX minimieren) korreliert stark mit Recall, und Youden maximiert indirekt den Unterschied TPR–FPR → liefert sehr recall-starke Schwellen.    """)
