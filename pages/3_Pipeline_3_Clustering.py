import streamlit as st
from pathlib import Path


st.title("Pipeline 3 - Clustering & Exploration Non-Supervisée")

st.markdown(
    """
    Ce pipeline est orienté **analyse structurelle des profils patientes**,
    avec un focus sur le nettoyage robuste des données et la visualisation
    des patterns latents.
    """
)

st.subheader("Prétraitement spécifique")
st.markdown(
    """
    - Détection et filtrage des valeurs aberrantes via la méthode **IQR**
      (Interquartile Range)
    - Normalisation des variables avec **MinMaxScaler**
    """
)

st.subheader("Analyse Univariée et Clustering")
col1, col2 = st.columns(2)

with col1:
    img_path = Path("images") / "ANN_summary_pipe3.png"
    if img_path.exists():
        st.image(str(img_path), caption="Résumé du modèle ANN (Pipeline 3)", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

with col2:
    img_path = Path("images") / "KNN_summary_pipe3.png"
    if img_path.exists():
        st.image(str(img_path), caption="Résumé du modèle KNN (Pipeline 3)", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

st.subheader("Projet Clustering & Comparaison des Métriques")
col_comp = st.columns(2)

with col_comp[0]:
    img_path = Path("images") / "metrics_comparison_pipe3.png"
    if img_path.exists():
        st.image(str(img_path), caption="Comparaison des métriques (Pipeline 3)", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

with col_comp[1]:
    img_path = Path("images") / "NaiveBayes_summary_pipe3.png"
    if img_path.exists():
        st.image(str(img_path), caption="Résumé du modèle Naive Bayes (Pipeline 3)", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

st.markdown(
    """
    Ces visualisations confirment la capacité de l'algorithme à identifier
    des **sous-groupes naturels** dans les données cliniques, sans utiliser
    les étiquettes (labels), ce qui renforce la pertinence de l'approche
    non-supervisée dans ce pipeline.
    """
)
