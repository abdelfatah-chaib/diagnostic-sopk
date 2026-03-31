import streamlit as st
from pathlib import Path


st.title("Pipeline 1 - Données Cliniques")

st.markdown(
    """
    Ce pipeline s'appuie sur le **dataset initial** du projet SOPK.
    Il vise à construire une base solide de référence via un prétraitement structuré
    et l'évaluation de plusieurs familles de modèles.
    """
)

st.subheader("Prétraitement")
st.markdown(
    """
    - **Imputation** des valeurs manquantes (ex: variables cliniques et symptômes)
    - **Label Encoding** pour transformer les variables catégorielles
    - **Borderline SMOTE** pour gérer le déséquilibre des classes
    """
)

st.subheader("Modèles testés (exhaustif)")
st.markdown(
    """
    1. **SMOTE + Clustering + RF**
    2. **Markov RF + SMOTE**
    3. **RF + Q-Learning**
    4. **ACP + RF**
    5. **KNN + SMOTE**
    6. **EasyEnsemble + BorderlineSMOTE**
    7. **GaussianNB + SMOTE**
    """
)

st.header("Résultats & Visualisations")

st.subheader("Comparaison des Modèles (Top 5)")
img_path = Path("images") / "fig3_radar_top5_pipe1.png"
if img_path.exists():
    st.image(str(img_path), caption="Radar chart des 5 meilleurs modèles - Pipeline 1", width="stretch")
else:
    st.warning(f"Image manquante: {img_path}")

st.subheader("Heatmap des Performances")
img_path = Path("images") / "fig4_heatmap_pipe1.png"
if img_path.exists():
    st.image(str(img_path), caption="Heatmap des performances - Pipeline 1", width="stretch")
else:
    st.warning(f"Image manquante: {img_path}")

st.subheader("Matrices de Confusion des Meilleurs Modèles")
col1, col2, col3 = st.columns(3)

with col1:
    img_path = Path("images") / "cm_SMOTE_plus_Clustering_plus_RF_pipe1.jpeg"
    if img_path.exists():
        st.image(str(img_path), caption="CM: SMOTE + Clustering + RF", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

with col2:
    img_path = Path("images") / "cm_Markov_RF_plus_SMOTE_pipe1.jpeg"
    if img_path.exists():
        st.image(str(img_path), caption="CM: Markov RF + SMOTE", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

with col3:
    img_path = Path("images") / "cm_KNN_plus_SMOTE_pipe1.jpeg"
    if img_path.exists():
        st.image(str(img_path), caption="CM: KNN + SMOTE", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

st.subheader("Courbe ROC - Markov Random Forest + SMOTE")
img_path = Path("images") / "roc_Markov_RF_plus_SMOTE_pipe1.jpeg"
if img_path.exists():
    st.image(str(img_path), caption="ROC Curve - Markov RF + SMOTE", width="stretch")
else:
    st.warning(f"Image manquante: {img_path}")
