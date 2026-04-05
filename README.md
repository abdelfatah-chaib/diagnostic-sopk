#  Diagnostic Prédictif du SOPK

> Application web d'aide au diagnostic du **Syndrome des Ovaires Polykystiques (SOPK)** par intelligence artificielle.

---

##  Description

Le SOPK (Syndrome des Ovaires Polykystiques) est l'un des troubles hormonaux les plus répandus chez les femmes en âge de procréer. Il peut entraîner des cycles irréguliers, des difficultés de fertilité, des troubles métaboliques et un impact important sur la qualité de vie.

Ce projet universitaire explore et compare plusieurs approches d'IA afin de concevoir un outil d'aide au diagnostic **rapide, fiable et interprétable**, structuré autour de trois pipelines parallèles.

---

##  Fonctionnalités

- **Tableau de bord interactif** avec navigation entre les pipelines
- **Visualisations** : radar charts, heatmaps, matrices de confusion, courbes ROC
- **Comparaison globale** des modèles sur des métriques adaptées à la classification médicale binaire
- **Architecture modulaire** en pipelines indépendants et comparables

---


##  Pipelines

### Pipeline 1 — Données Cliniques (ML classique)
- **Dataset** : `pcos_prediction_dataset.csv`
- **Prétraitement** : imputation des valeurs manquantes, Label Encoding, Borderline-SMOTE
- **Modèles** : Random Forest, Gradient Boosting, CatBoost, Markov RF, Q-Learning, KNN, GaussianNB
- **Meilleur résultat** : Borderline-SMOTE + RF (AUC-ROC ≈ 0.66)

### Pipeline 2 — Approche Hybride (Logique Floue & Algorithme Génétique)
- **Dataset** : fusion `PCOS_data_without_infertility` + `PCOS_infertility`
- **Feature engineering** : `Total_Follicles`, `LH_FSH_Ratio`
- **Innovations** : score de risque par logique floue (scikit-fuzzy), sélection de features par algorithme génétique
- **Modèles** : Random Forest optimisé, SVM (RBF), MLP (Adam)
- **Meilleur résultat** : Algo Génétique + RF (AUC-ROC ≈ 0.83)

### Pipeline 3 — Clustering & IQR (Non supervisé)
- **Dataset** : fusion `PCOS_data_without_infertility` + `PCOS_infertility`
- **Prétraitement** : filtrage des outliers par IQR, normalisation MinMaxScaler
- **Approche** : AFC (Analyse Factorielle des Correspondances), Fuzzy C-Means
- **Modèles supervisés** : Random Forest, MLP, SVM, Naive Bayes, KNN
- **Meilleur résultat** : Random Forest (AUC-ROC ≈ 0.93)

---



## Stack technique

| Outil | Usage |
|-------|-------|
| Python 3.10+ | Langage principal |
| Streamlit ≥ 1.32 | Interface web interactive |
| scikit-learn | Modèles ML (RF, SVM, KNN…) |
| scikit-fuzzy | Logique floue |
| Pandas ≥ 2.0 | Manipulation des données |
| NumPy ≥ 1.24 | Calcul numérique |
| Plotly ≥ 5.18 | Visualisations interactives |
| Matplotlib ≥ 3.8 | Graphiques statiques |

---

##  Installation & Lancement

### Prérequis

- Python 3.10 ou supérieur
- pip

### Installation

```bash
git clone https://github.com/abdelfatah-chaib/diagnostic-sopk.git
cd diagnostic-sopk
pip install -r requirements.txt
```

### Lancement

```bash
# Dashboard principal
streamlit run app.py

# Ou page d'accueil alternative
streamlit run Accueil.py
```


---

##  Datasets

Les datasets utilisés proviennent de Kaggle :

- [PCOS Detection Dataset](https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos) — données cliniques et hormonales
- Dataset de prédiction SOPK (`pcos_prediction_dataset.csv`) — variables cliniques simplifiées

> ⚠️ Les fichiers de données ne sont pas inclus dans ce dépôt. Placez-les dans le dossier racine du projet avant de lancer l'application.

