import streamlit as st
from pathlib import Path


st.title("Pipeline 2 - Logique Floue & Algorithme Génétique")

st.markdown(
    """
    Ce pipeline exploite le **dataset fusionné**
    (**PCOS_data_without_infertility + PCOS_infertility**) afin d'améliorer
    la capacité de généralisation des modèles.
    """
)

st.subheader("Innovations méthodologiques")
st.markdown(
    """
    - Construction d'un **Score de Risque SOPK** via la **Logique Floue**
      (scikit-fuzzy), en combinant des variables cliniquement pertinentes.
    - **Sélection de variables par Algorithme Génétique** pour identifier
      les sous-ensembles de features les plus discriminants.
    """
)

st.subheader("Modèles testés (exhaustif)")
st.markdown(
    """
    1. **Naive Bayes**
    2. **Random Forest (Optimisé)**
    3. **SVM (RBF)**
    4. **Réseau de Neurones MLP (Adam)**
    5. **Algo Génétique + RF**
    """
)

st.header("Explicabilité Médicale et Résultats")

st.subheader("Interprétabilité des Biomarqueurs")
col1, col2 = st.columns(2)

with col1:
    img_path = Path("images") / "confusion_matrix_pipe2.png"
    if img_path.exists():
        st.image(str(img_path), caption="Matrice de confusion du meilleur modèle", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

with col2:
    img_path = Path("images") / "feature_importance_pipe2.png"
    if img_path.exists():
        st.image(str(img_path), caption="Top 10 des variables les plus discriminantes", width="stretch")
    else:
        st.warning(f"Image manquante: {img_path}")

st.subheader("Distribution du Score d'Innovation")
img_path = Path("images") / "roc_curve_pipe2.png"
if img_path.exists():
    st.image(str(img_path), caption="Courbe ROC - Pipeline 2", width="stretch")
else:
    st.warning(f"Image manquante: {img_path}")

st.markdown(
    """
    Ce graphique illustre la capacité du **modèle** à séparer efficacement
    les patientes saines des patientes atteintes du **SOPK**, renforçant ainsi
    l'interprétabilité médicale du pipeline.
    """
)
