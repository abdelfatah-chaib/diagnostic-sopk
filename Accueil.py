import streamlit as st

st.set_page_config(page_title="Diagnostic SOPK", layout="wide")

st.title("Diagnostic Prédictif du SOPK")
st.write("Application d'aide au diagnostic du Syndrome des Ovaires Polykystiques (SOPK).")

st.header("Objectif du Projet")
st.write("Fournir un outil d'aide à la décision médicale robuste, capable d'identifier les patientes atteintes du SOPK avec une haute précision tout en minimisant les erreurs de diagnostic (faux négatifs).")

st.header("Démarche Suivie")
st.markdown('''
L'architecture du projet est structurée autour de trois axes analytiques :
* **Pipeline 1 (Machine Learning Classique)** : Évaluation de modèles supervisés standards et ensemblistes sur les données cliniques brutes.
* **Pipeline 2 (Approche Hybride)** : Création d'un système expert intégrant la Logique Floue pour modéliser l'incertitude médicale (Score de Risque), optimisé par un Algorithme Génétique pour la sélection des biomarqueurs clés.
* **Pipeline 3 (Apprentissage Non-Supervisé)** : Utilisation du Clustering (K-Means) et de la Réduction de Dimensionnalité (PCA) pour découvrir des sous-groupes de patientes sans a priori.
''')

st.header("Jeux de Données (Datasets)")
st.write("Le modèle s'appuie sur une cohorte de données cliniques (échographies, bilans hormonaux, métabolisme). Le déséquilibre naturel des classes (surreprésentation des patientes saines) a été corrigé via la technique de suréchantillonnage Borderline-SMOTE afin de garantir l'impartialité des algorithmes.")

st.info("Utilisez le menu latéral de navigation pour explorer les pipelines et consulter l'évaluation globale des modèles.")
