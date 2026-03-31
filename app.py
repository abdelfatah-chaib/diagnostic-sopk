import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="Dashboard SOPK",
    page_icon="🩺",
    layout="wide",
)

st.sidebar.title("🧭 Navigation")
pages = [
    "🏠 Accueil & Contexte",
    "📊 Pipeline 1 (Données Cliniques)",
    "🧬 Pipeline 2 (Logique Floue & Algo Génétique)",
    "🔍 Pipeline 3 (Clustering & IQR)",
    "🏆 Comparaison Finale des Modèles",
]
selected_page = st.sidebar.radio("Aller à", pages)

st.markdown(
    """
    <style>
        .main {
            background: linear-gradient(180deg, #f8fbff 0%, #ffffff 40%);
        }
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }
        .hero-box {
            border: 1px solid #dbe7f3;
            background: linear-gradient(135deg, #eaf4ff 0%, #f5fbff 100%);
            border-radius: 14px;
            padding: 0.9rem 1rem;
            margin-bottom: 1rem;
        }
        .hero-title {
            margin: 0;
            color: #0f3057;
            font-weight: 700;
            font-size: 1.08rem;
        }
        .hero-sub {
            margin: 0.2rem 0 0 0;
            color: #355070;
            font-size: 0.95rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_hero(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="hero-box">
            <p class="hero-title">{title}</p>
            <p class="hero-sub">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if selected_page == "🏠 Accueil & Contexte":
    render_hero(
        "Tableau de bord SOPK - Présentation du projet",
        "Vision globale, contexte médical et stratégie IA en pipelines parallèles.",
    )
    st.title("🩺 Prédiction du SOPK: vers un diagnostic intelligent et précoce")

    st.markdown(
        """
        ### 🌸 Qu'est-ce que le SOPK ?
        Le **Syndrome des Ovaires Polykystiques (SOPK)** est un trouble hormonal fréquent chez les femmes en âge de procréer.
        Il peut entraîner des cycles irréguliers, des difficultés de fertilité, des troubles métaboliques et un impact important sur la qualité de vie.

        Un diagnostic **rapide, fiable et interprétable** est essentiel pour améliorer la prise en charge.
        """
    )

    st.info(
        "🧠 Notre projet universitaire explore des approches IA complémentaires pour identifier le meilleur modèle de diagnostic du SOPK."
    )

    st.markdown(
        """
        ### 🚀 Démarche de l'équipe
        Nous avons conçu **3 pipelines parallèles**, chacun testant une stratégie différente:

        - **📊 Pipeline 1 - Données cliniques** : modèles classiques de Machine Learning sur des variables médicales.
        - **🧬 Pipeline 2 - Logique floue & algorithme génétique** : optimisation intelligente et prise en compte de l'incertitude.
        - **🔍 Pipeline 3 - Clustering & IQR** : segmentation des profils patients et nettoyage robuste des données.

        L'objectif final est de **comparer les performances** (précision, robustesse, interprétabilité) pour retenir
        le meilleur compromis pour un diagnostic assisté par IA.
        """
    )

    st.info("👉 Utilisez le menu à gauche pour explorer les pipelines et la comparaison finale.")

elif selected_page == "📊 Pipeline 1 (Données Cliniques)":
    render_hero(
        "Pipeline 1 - Données Cliniques",
        "Prétraitement classique + modèles innovants pour établir une baseline robuste.",
    )
    st.title("📊 Pipeline 1 - Données Cliniques")
    st.markdown("Analyse du dataset **pcos_prediction_dataset.csv**.")

    with st.expander("🧹 Prétraitement", expanded=True):
        st.markdown(
            """
            - Remplacement des valeurs manquantes de **Acne Severity** par **No Acne**.
            - Encodage des variables catégorielles via **Label Encoding**.
            - Gestion du déséquilibre des classes via **Borderline SMOTE**.
            """
        )

    with st.expander("🧠 Modèles Innovants", expanded=True):
        st.markdown(
            """
            Les approches testées dans ce pipeline incluent:

            - **Random Forest** (baseline classique robuste)
            - **Gradient Boosting**
            - **Markov Random Forest** (approche innovante)
            - **Q-Learning** (apprentissage par renforcement)
            """
        )

    with st.expander("🏁 Résultats", expanded=True):
        st.info("🏆 Meilleur modèle: **SMOTE + Clustering + RF**")

        results_df = pd.DataFrame(
            {
                "Metric": [
                    "Accuracy",
                    "Log Loss",
                    "FPR",
                    "AUC-ROC",
                    "Recall",
                    "Kappa",
                    "MCC",
                    "Dice Score",
                ],
                "Value": [0.61, 0.38, 0.37, 0.50, 0.37, 0.003, 0.004, 0.16],
            }
        )

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", "0.61")
        col2.metric("Log Loss", "0.38")
        col3.metric("AUC-ROC", "0.50")
        col4.metric("Recall", "0.37")

        st.dataframe(results_df, width="stretch")

        fig = px.bar(
            results_df,
            x="Metric",
            y="Value",
            title="Performance du modèle SMOTE + Clustering + RF",
            text="Value",
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(
            yaxis_title="Score",
            xaxis_title="Métrique",
            template="plotly_white",
            title_x=0.02,
        )
        st.plotly_chart(fig, width="stretch")

elif selected_page == "🧬 Pipeline 2 (Logique Floue & Algo Génétique)":
    render_hero(
        "Pipeline 2 - Intelligence Hybride",
        "Logique floue + sélection génétique pour optimiser interprétabilité et performance.",
    )
    st.title("🧬 Pipeline 2 - Logique Floue & Algorithme Génétique")
    st.markdown(
        "Ce pipeline exploite le dataset fusionné **PCOS_data_without_infertility + PCOS_infertility**."
    )

    with st.expander("🛠️ Feature Engineering", expanded=True):
        st.markdown(
            """
            Variables construites pour enrichir le signal clinique:

            - **Total_Follicles** = nombre total de follicules (ovaire gauche + ovaire droit)
            - **LH_FSH_Ratio** = ratio hormonal LH/FSH, souvent pertinent dans le contexte SOPK
            """
        )

    with st.expander("✨ Innovations majeures", expanded=True):
        st.markdown(
            """
            Deux contributions clés du pipeline:

            - **Score de Risque via Logique Floue (scikit-fuzzy)**:
              combinaison de l'**IMC** et du profil folliculaire pour construire un score continu
              interprétable de risque SOPK.
            - **Sélection de variables par Algorithme Génétique**:
              exploration guidée de sous-ensembles de features pour maximiser les performances prédictives.
            """
        )
        st.info("🧠 Objectif: améliorer à la fois la performance et l'interprétabilité clinique.")

    with st.expander("🤖 Modèles entraînés", expanded=True):
        st.markdown(
            """
            - **Random Forest optimisé**
            - **SVM (noyau RBF)**
            - **Deep Learning** : **MLP** entraîné avec l'optimiseur **Adam**
            """
        )

elif selected_page == "🔍 Pipeline 3 (Clustering & IQR)":
    render_hero(
        "Pipeline 3 - Exploration Non Supervisée",
        "Nettoyage IQR + AFC + Fuzzy C-Means pour révéler les profils cliniques latents.",
    )
    st.title("🔍 Pipeline 3 - Clustering & IQR")
    st.markdown(
        "Ce pipeline utilise également le dataset fusionné **PCOS_data_without_infertility + PCOS_infertility**."
    )

    with st.expander("🧹 Prétraitement spécifique", expanded=True):
        st.markdown(
            """
            Différences majeures par rapport aux autres pipelines:

            - **Filtrage des outliers par la méthode IQR (Interquartile Range)**
            - **Normalisation avec MinMaxScaler** pour homogénéiser les échelles de variables
            """
        )

    with st.expander("🧭 Approche non-supervisée", expanded=True):
        st.markdown(
            """
            Ce pipeline met l'accent sur l'exploration de structures latentes:

            - **AFC (Analyse Factorielle des Correspondances)**
            - **Fuzzy C-Means Clustering** pour une appartenance souple aux groupes
            """
        )

    st.info("🖼️ Insérer les Violin Plots générés par Seaborn ici.")
    st.empty()

elif selected_page == "🏆 Comparaison Finale des Modèles":
    render_hero(
        "Comparaison Finale",
        "Sélection du modèle le plus fiable pour un futur déploiement clinique.",
    )
    st.title("🏆 Comparaison Finale des Modèles")
    st.markdown(
        "Comparaison des meilleures approches sur des métriques adaptées à la **classification binaire** du SOPK."
    )
    st.info(
        "ℹ️ Les métriques de type RMSLE ou SSIM ne sont pas utilisées ici car elles ne sont pas pertinentes pour ce problème de classification binaire."
    )

    df = pd.DataFrame(
        {
            "Méthode": [
                "Borderline-SMOTE + Clustering + RF (Pipe 1)",
                "Logique Floue + Algo Génétique + RF (Pipe 2)",
                "Deep Learning (MLP Adam) (Pipe 2)",
            ],
            "Log Loss": [0.38, 0.29, 0.31],
            "FPR": [0.37, 0.24, 0.27],
            "AUC-ROC": [0.50, 0.83, 0.81],
            "Recall": [0.37, 0.72, 0.74],
            "Cohen's Kappa": [0.003, 0.31, 0.28],
            "MCC": [0.004, 0.34, 0.30],
            "Dice Score (F1)": [0.16, 0.72, 0.73],
        }
    )

    st.subheader("📋 Tableau récapitulatif")
    st.dataframe(df.style.background_gradient(cmap="RdYlGn"), width="stretch")

    st.subheader("🕸️ Radar Chart des performances")
    radar_axes = ["AUC-ROC", "Recall", "Cohen's Kappa", "MCC", "Dice Score (F1)"]

    fig_radar = go.Figure()
    for _, row in df.iterrows():
        values = [row[axis] for axis in radar_axes]
        values_closed = values + [values[0]]
        theta_closed = radar_axes + [radar_axes[0]]

        fig_radar.add_trace(
            go.Scatterpolar(
                r=values_closed,
                theta=theta_closed,
                fill="toself",
                name=row["Méthode"],
            )
        )

    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        template="plotly_white",
        title="Comparaison des modèles sur AUC-ROC, Recall, Kappa, MCC et Dice Score",
        title_x=0.02,
    )
    st.plotly_chart(fig_radar, width="stretch")

    best_model = df.sort_values(["MCC", "AUC-ROC"], ascending=False).iloc[0]
    st.markdown(
        f"""
        ### ✅ Conclusion pour le déploiement clinique
        Le modèle retenu est **{best_model['Méthode']}**,
        car il présente le meilleur compromis global avec un **MCC = {best_model['MCC']:.2f}**
        et un **AUC-ROC = {best_model['AUC-ROC']:.2f}**.

        Ce choix favorise une meilleure fiabilité de classification en contexte clinique,
        tout en conservant une bonne capacité de détection des cas positifs.
        """
    )

else:
    st.title(selected_page)
    st.info("Cette section est en cours de construction. Elle sera ajoutée à l'étape suivante.")
