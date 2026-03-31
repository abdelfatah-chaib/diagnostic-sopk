import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import json
from pathlib import Path

st.title("Comparaison Globale - Tous les Modèles")

st.markdown(
    """
    Tableau comparatif exhaustif des modèles testés sur les 3 pipelines avec leurs métriques exactes.
    """
)

# --- DONNÉES EXACTES ET COMPLÈTES DES MODÈLES (3 PIPELINES) ---
pipe1_rows = [
    {
        "Méthode (Modèle)": "CatBoost (Pipe 1)",
        "Log Loss (↓)": 0.4439,
        "FPR (↓)": 0.1171,
        "AUC-ROC (↑)": 0.6588,
        "Recall (↑)": 0.3644,
        "Cohen's Kappa (↑)": 0.3688,
        "MCC (↑)": 0.3551,
        "Dice Score (F1) (↑)": 0.4857,
    },
    {
        "Méthode (Modèle)": "Gradient Boosting (Pipe 1)",
        "Log Loss (↓)": 0.4475,
        "FPR (↓)": 0.1147,
        "AUC-ROC (↑)": 0.6575,
        "Recall (↑)": 0.3601,
        "Cohen's Kappa (↑)": 0.3672,
        "MCC (↑)": 0.3541,
        "Dice Score (F1) (↑)": 0.4839,
    },
    {
        "Méthode (Modèle)": "Markov RF (Pipe 1)",
        "Log Loss (↓)": 0.4497,
        "FPR (↓)": 0.1130,
        "AUC-ROC (↑)": 0.6653,
        "Recall (↑)": 0.3601,
        "Cohen's Kappa (↑)": 0.3700,
        "MCC (↑)": 0.3582,
        "Dice Score (F1) (↑)": 0.4862,
    },
    {
        "Méthode (Modèle)": "ACP + RF (Pipe 1)",
        "Log Loss (↓)": 0.4578,
        "FPR (↓)": 0.1332,
        "AUC-ROC (↑)": 0.6406,
        "Recall (↑)": 0.3601,
        "Cohen's Kappa (↑)": 0.3426,
        "MCC (↑)": 0.3275,
        "Dice Score (F1) (↑)": 0.4659,
    },
    {
        "Méthode (Modèle)": "ACM (Pipe 1)",
        "Log Loss (↓)": 1.3431,
        "FPR (↓)": 0.1246,
        "AUC-ROC (↑)": 0.5599,
        "Recall (↑)": 0.2288,
        "Cohen's Kappa (↑)": 0.1835,
        "MCC (↑)": 0.1800,
        "Dice Score (F1) (↑)": 0.3235,
    },
    {
        "Méthode (Modèle)": "Q-Learning (Pipe 1)",
        "Log Loss (↓)": 0.5147,
        "FPR (↓)": 0.1558,
        "AUC-ROC (↑)": 0.5960,
        "Recall (↑)": 0.3347,
        "Cohen's Kappa (↑)": 0.2827,
        "MCC (↑)": 0.2647,
        "Dice Score (F1) (↑)": 0.4263,
    },
    {
        "Méthode (Modèle)": "Borderline-SMOTE + RF (Pipe 1)",
        "Log Loss (↓)": 0.4527,
        "FPR (↓)": 0.1065,
        "AUC-ROC (↑)": 0.6638,
        "Recall (↑)": 0.3763,
        "Cohen's Kappa (↑)": 0.3825,
        "MCC (↑)": 0.3704,
        "Dice Score (F1) (↑)": 0.4982,
    },
]

pipe2_rows = []
pipe2_json_path = Path("images") / "metrics_pipeline2.json"
pipe2_name_map = {
    "Naive Bayes": "Naive Bayes (Pipe 2)",
    "Random Forest (Optimisé)": "Random Forest Optimisé (Pipe 2)",
    "SVM (RBF)": "SVM RBF (Pipe 2)",
    "Réseau de Neurones (Adam)": "Réseau de Neurones MLP (Adam) (Pipe 2)",
    "Algo Génétique + RF": "Algo Génétique + RF (Pipe 2)",
}
pipe2_order = [
    "Naive Bayes",
    "Random Forest (Optimisé)",
    "SVM (RBF)",
    "Réseau de Neurones (Adam)",
    "Algo Génétique + RF",
]

if pipe2_json_path.exists():
    with pipe2_json_path.open("r", encoding="utf-8") as f:
        pipe2_metrics = json.load(f)

    for model_name in pipe2_order:
        model_metrics = pipe2_metrics.get(model_name)
        if model_metrics is None:
            continue

        pipe2_rows.append(
            {
                "Méthode (Modèle)": pipe2_name_map.get(model_name, f"{model_name} (Pipe 2)"),
                "Log Loss (↓)": model_metrics.get("Log Loss (↓)", np.nan),
                "FPR (↓)": model_metrics.get("FPR (↓)", np.nan),
                "AUC-ROC (↑)": model_metrics.get("AUC (ROC) (↑)", np.nan),
                "Recall (↑)": model_metrics.get("Recall / Sensitivity (↑)", np.nan),
                "Cohen's Kappa (↑)": model_metrics.get("Cohen's Kappa (↑)", np.nan),
                "MCC (↑)": model_metrics.get("MCC (↑)", np.nan),
                "Dice Score (F1) (↑)": model_metrics.get("Dice Score (F1) (↑)", np.nan),
            }
        )
else:
    st.warning("Fichier introuvable: images/metrics_pipeline2.json")

pipe3_rows = [
    {
        "Méthode (Modèle)": "Random Forest (Pipe 3)",
        "Log Loss (↓)": 0.3105,
        "FPR (↓)": 0.0510,
        "AUC-ROC (↑)": 0.9268,
        "Recall (↑)": 0.8396,
        "Cohen's Kappa (↑)": 0.7900,
        "MCC (↑)": 0.8000,
        "Dice Score (F1) (↑)": 0.8504,
    },
    {
        "Méthode (Modèle)": "MLP (Pipe 3)",
        "Log Loss (↓)": 0.3400,
        "FPR (↓)": 0.0620,
        "AUC-ROC (↑)": 0.9036,
        "Recall (↑)": 0.8208,
        "Cohen's Kappa (↑)": 0.7600,
        "MCC (↑)": 0.7700,
        "Dice Score (F1) (↑)": 0.8142,
    },
    {
        "Méthode (Modèle)": "SVM (Pipe 3)",
        "Log Loss (↓)": np.nan,
        "FPR (↓)": np.nan,
        "AUC-ROC (↑)": 0.8784,
        "Recall (↑)": 0.7547,
        "Cohen's Kappa (↑)": np.nan,
        "MCC (↑)": np.nan,
        "Dice Score (F1) (↑)": 0.7602,
    },
    {
        "Méthode (Modèle)": "Naive Bayes (Pipe 3)",
        "Log Loss (↓)": np.nan,
        "FPR (↓)": np.nan,
        "AUC-ROC (↑)": 0.8359,
        "Recall (↑)": 0.8019,
        "Cohen's Kappa (↑)": np.nan,
        "MCC (↑)": np.nan,
        "Dice Score (F1) (↑)": 0.7760,
    },
    {
        "Méthode (Modèle)": "KNN (Pipe 3)",
        "Log Loss (↓)": np.nan,
        "FPR (↓)": np.nan,
        "AUC-ROC (↑)": 0.8436,
        "Recall (↑)": 0.6132,
        "Cohen's Kappa (↑)": np.nan,
        "MCC (↑)": np.nan,
        "Dice Score (F1) (↑)": 0.6558,
    },
]

all_rows = pipe1_rows + pipe2_rows + pipe3_rows
df_res = pd.DataFrame(all_rows).set_index("Méthode (Modèle)")

st.subheader("Tableau récapitulatif")
try:
    styled_df = df_res.style.background_gradient(cmap="RdYlGn", vmin=0, vmax=1).format(na_rep="-", precision=4)
except ImportError:
    # Streamlit Cloud images may omit matplotlib; keep the table readable without gradient.
    styled_df = df_res.style.format(na_rep="-", precision=4)

st.markdown(
    """
    <style>
    .global-comparison-table {
        width: 100%;
        overflow: visible;
    }
    .global-comparison-table table {
        width: 100% !important;
        table-layout: fixed;
        border-collapse: collapse;
    }
    .global-comparison-table th,
    .global-comparison-table td {
        white-space: normal !important;
        word-break: break-word;
        font-size: 0.86rem;
        padding: 0.42rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"<div class='global-comparison-table'>{styled_df.to_html()}</div>",
    unsafe_allow_html=True,
)

# Identification automatique du meilleur modèle
# On utilise l'AUC-ROC car certains modèles n'ont pas de MCC renseigné
meilleur_modele = df_res["AUC-ROC (↑)"].idxmax()
meilleur_score_auc = df_res.loc[meilleur_modele, "AUC-ROC (↑)"]
meilleur_score_f1 = df_res.loc[meilleur_modele, "Dice Score (F1) (↑)"]

st.success(
    f"**LE MEILLEUR MODELE GLOBAL EST : {meilleur_modele}** avec une **AUC-ROC de {meilleur_score_auc:.4f}** et un F1-Score de **{meilleur_score_f1:.4f}**."
)
