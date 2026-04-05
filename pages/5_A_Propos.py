import streamlit as st

st.title("ℹ️ À Propos")

st.markdown(
    """
    ## Diagnostic Prédictif du SOPK

    Cette application est un outil d'aide au diagnostic du **Syndrome des Ovaires Polykystiques (SOPK)**,
    développé dans le cadre d'un projet universitaire d'intelligence artificielle appliquée à la médecine.

    Le SOPK est l'un des troubles hormonaux les plus répandus chez les femmes en âge de procréer.
    Un diagnostic précoce et fiable est essentiel pour limiter ses effets sur la fertilité, le métabolisme
    et la qualité de vie des patientes.

    ---

    ### 🎯 Objectif

    Concevoir et comparer plusieurs approches d'IA pour identifier les patientes atteintes du SOPK
    avec la meilleure précision possible, en minimisant les faux négatifs — cas où une patiente malade
    ne serait pas détectée.

    ---

    ### 🏗️ Architecture du projet

    Le projet est structuré autour de **trois pipelines parallèles**, chacun explorant une stratégie différente :

    | Pipeline | Approche | Points clés |
    |---|---|---|
    | **Pipeline 1** | Machine Learning classique | Borderline-SMOTE, Clustering, Random Forest, Q-Learning |
    | **Pipeline 2** | Approche hybride | Logique Floue, Algorithme Génétique, MLP (Adam) |
    | **Pipeline 3** | Apprentissage non-supervisé | IQR, MinMaxScaler, AFC, Fuzzy C-Means |

    ---

    ### 🛠️ Technologies utilisées

    - **Python 3.10+**
    - **Streamlit** — interface web interactive
    - **scikit-learn** — modèles de Machine Learning
    - **scikit-fuzzy** — logique floue
    - **Plotly** — visualisations interactives
    - **Pandas / NumPy** — manipulation des données

    ---

    ### 📊 Jeux de données

    - `pcos_prediction_dataset.csv` — données cliniques (Pipeline 1)
    - `PCOS_data_without_infertility` + `PCOS_infertility` — dataset fusionné hormonal et échographique (Pipelines 2 & 3)

    ---

    ### 👩‍💻 Équipe

    Projet universitaire réalisé par des étudiants en Master IA / Data Science.

    ---

    > *« L'intelligence artificielle au service d'un diagnostic plus rapide, plus juste et plus humain. »*
    """
)
