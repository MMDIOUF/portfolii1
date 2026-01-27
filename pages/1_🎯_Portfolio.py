import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card

st.set_page_config(page_title="Portfolio - Projets Data", layout="wide")
inject_custom_css()

# === 1. HERO — SILENCE VISUEL ===
st.markdown("""
<div style="text-align: center; padding: 5rem 2rem 4rem;">
    <h1 style="font-size: 3.2rem; font-weight: 800; color: #1f2937; margin-bottom: 1.5rem;">
        Portfolio Data
    </h1>
    <p style="font-size: 1.4rem; color: #6b7280; max-width: 860px; margin: 0 auto; line-height: 1.6;">
        Des projets concrets, orientés terrain,
        couvrant toute la chaîne data :
        de la collecte à la décision.
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# === 2. ACTE I — LA BASE : PIPELINES & ARCHITECTURE ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        ☁️ La fondation
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Toute analyse fiable repose sur une architecture data robuste.
    </p>
""", unsafe_allow_html=True)

# CARDS RÉSUMÉ
col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Pipeline Multi-Cloud Immobilier",
        {
            "Objectif": "Automatiser collecte et préparation",
            "Cloud": "Environnements AWS et GCP",
            "Valeur": "Données fiables pour décision"
        },
        "☁️",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Big Data & Automatisation",
        {
            "Objectif": "Traiter volumes importants",
            "Mode": "Batch et flux automatisés",
            "Valeur": "Réduction interventions manuelles"
        },
        "🔄",
        "success"
    ), unsafe_allow_html=True)

# EXPANDERS (DÉTAIL SUR DEMANDE)
with st.expander("🔍 Voir les détails — Pipeline Multi-Cloud"):
    st.markdown("""
    **Problématique**  
    Les données immobilières étaient dispersées, hétérogènes et difficiles à exploiter.
    
    **Approche**  
    Mise en place d'un pipeline automatisé multi-cloud pour centraliser, nettoyer, stocker et analyser les données.
    
    **Résultats**
    - Données structurées et fiables
    - Analyse quasi temps réel
    - Architecture scalable et sécurisée
    - Forte réduction des opérations manuelles
    
    **Compétences**  
    Data Engineering • Cloud Architecture • Automatisation
    """)

with st.expander("🔍 Voir les détails — Big Data & Automatisation"):
    st.markdown("""
    **Problématique**  
    Volumes de données élevés nécessitant des traitements robustes et continus.
    
    **Approche**  
    Conception de pipelines Big Data avec ingestion automatisée, contrôles de qualité et supervision des flux.
    
    **Résultats**
    - Automatisation complète des traitements
    - Suivi et traçabilité des données
    - Détection rapide des anomalies
    - Meilleure fiabilité globale des flux
    
    **Compétences**  
    Big Data Processing • ETL Automation • Data Quality Management
    """)

st.markdown("---")

# === 3. ACTE II — PRÉDIRE AU LIEU DE CONSTATER ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🤖 Anticiper
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Aller au-delà du constat pour anticiper les comportements.
    </p>
""", unsafe_allow_html=True)

# CARTES ML (SYNTHÈSE)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_info_card(
        "Prédiction Churn Client",
        {
            "Usage": "Rétention client",
            "Résultat": "Modèle performant et exploitable",
            "Décision": "Actions ciblées en amont"
        },
        "📉",
        "warning"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Souscription Assurance",
        {
            "Usage": "Ciblage marketing",
            "Résultat": "Modèle prédictif fiable",
            "Décision": "Optimisation des campagnes"
        },
        "🏦",
        "info"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_info_card(
        "Prévision de Salaire",
        {
            "Usage": "Aide à la décision RH",
            "Résultat": "Modèle explicatif et cohérent",
            "Décision": "Pilotage et équité"
        },
        "💰",
        "success"
    ), unsafe_allow_html=True)

# EXPANDERS (ULTRA STRATÉGIQUES)
with st.expander("🔍 Détails — Prédiction Churn Client"):
    st.markdown("""
    **Objectif**  
    Identifier les clients à risque afin d'agir avant la rupture.
    
    **Approche**  
    - Analyse comportementale et historique client
    - Feature engineering orienté métier
    - Modèles de classification et validation rigoureuse
    
    **Valeur**  
    - Meilleure anticipation des départs
    - Actions de rétention plus ciblées
    - Décisions basées sur des données fiables
    
    **Compétences**  
    Machine Learning appliqué • Modélisation prédictive • Feature Engineering
    """)

with st.expander("🔍 Détails — Prédiction Souscription Assurance"):
    st.markdown("""
    **Objectif**  
    Identifier les profils les plus susceptibles de souscrire.
    
    **Approche**  
    - Exploitation de données clients et campagnes
    - Modélisation prédictive et scoring
    - Tests et évaluation des performances
    
    **Valeur**  
    - Réduction du gaspillage marketing
    - Meilleur ciblage des prospects
    - Augmentation de l'efficacité commerciale
    
    **Compétences**  
    Deep Learning appliqué • Classification • Data Analysis
    """)

with st.expander("🔍 Détails — Prévision de Salaire"):
    st.markdown("""
    **Objectif**  
    Apporter un appui objectif aux décisions RH.
    
    **Approche**  
    - Modèles de régression et analyse des facteurs clés
    - Étude de l'impact des compétences et de l'expérience
    - Visualisation claire des résultats
    
    **Valeur**  
    - Aide à l'équité salariale
    - Vision claire des leviers de rémunération
    - Support à la décision RH
    
    **Compétences**  
    Régression & Modélisation • Data Analysis • Data Visualization
    """)

st.markdown("---")

# === 4. ACTE III — VOIR POUR DÉCIDER ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        📊 Voir pour décider
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Rendre les données lisibles pour faciliter la décision.
    </p>
</div>
""", unsafe_allow_html=True)

# CARTES VISUALISATION
col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Dashboards BI — IPSOS",
        {
            "Usage": "Suivi opérationnel des équipes",
            "Impact": "Automatisation du reporting",
            "Valeur": "Gain de temps et visibilité"
        },
        "📊",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Dashboard Ventes USA",
        {
            "Usage": "Analyse commerciale",
            "Fonctions": "KPIs, filtres et visualisations",
            "Valeur": "Lecture rapide des performances"
        },
        "📈",
        "info"
    ), unsafe_allow_html=True)

# EXPANDERS
with st.expander("🔍 Détails — Dashboards BI IPSOS"):
    st.markdown("""
    **Contexte**  
    Environnement d'études avec équipes terrain et téléphoniques.
    
    **Solution**  
    - Tableaux de bord dynamiques et décisionnels
    - Suivi des KPIs par agent et campagne
    - Automatisation des reportings manuels
    
    **Résultats**  
    - Gain de temps significatif
    - Meilleure lisibilité de la performance
    - Suivi opérationnel optimisé
    
    **Compétences**  
    Business Intelligence • Dashboards décisionnels • Process Automation
    """)

with st.expander("🔍 Détails — Dashboard Ventes USA"):
    st.markdown("""
    **Objectif**  
    Analyser les ventes par région, produit et client.
    
    **Fonctionnalités**  
    - Indicateurs clés en temps réel
    - Visualisations interactives
    - Filtres multi-critères
    
    **Valeur**  
    - Identification rapide des tendances
    - Aide au pilotage commercial
    - Décisions basées sur des données claires
    
    **Compétences**  
    Data Visualization • KPI Design • Applications Data interactives
    """)

st.markdown("---")

# === 5. ACTE IV — FIABILITÉ & DONNÉES SENSIBLES ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🛡️ Fiabilité & sécurité
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Quand la précision et la sécurité sont non négociables.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Détection Faux Billets",
        {
            "Usage": "Contrôle automatique",
            "Résultat": "Détection fiable",
            "Valeur": "Réduction des risques"
        },
        "💵",
        "danger"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Administration Oracle",
        {
            "Usage": "Bases critiques",
            "Impact": "Optimisation et stabilité",
            "Valeur": "Performance et sécurité"
        },
        "🗄️",
        "success"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Détection Faux Billets"):
    st.markdown("""
    **Objectif**  
    Automatiser la détection de faux billets.
    
    **Approche**  
    - Traitement d'images et extraction de caractéristiques
    - Modèle de classification
    - Tests et validation
    
    **Résultats**  
    - Détection fiable
    - Réduction des risques
    - Automatisation du contrôle
    
    **Compétences**  
    Computer Vision appliquée • Classification • Deep Learning
    """)

with st.expander("🔍 Détails — Administration Oracle"):
    st.markdown("""
    **Contexte**  
    Bases critiques nécessitant stabilité et performance.
    
    **Travaux réalisés**  
    - Mise à niveau de l'environnement
    - Optimisation des requêtes
    - Sécurisation des accès
    - Développement de fonctionnalités
    
    **Résultats**  
    - Meilleures performances
    - Stabilité accrue
    - Sécurité renforcée
    
    **Compétences**  
    Administration de bases critiques • SQL avancé • Optimisation de requêtes
    """)

st.markdown("---")

# === 6. ACTE V — LA DATA DANS LE PRODUIT FINAL ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        💻 Le produit final
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Transformer la data en applications utilisables.
    </p>
""", unsafe_allow_html=True)

st.markdown(create_info_card(
    "Système de Réservation — API Amadeus",
    {
        "Type": "Application full-stack",
        "Intégration": "API externe temps réel",
        "Valeur": "Produit complet livré"
    },
    "✈️",
    "primary"
), unsafe_allow_html=True)

with st.expander("🔍 Détails — Système de Réservation"):
    st.markdown("""
    **Objectif**  
    Concevoir une application complète connectée à une API externe.
    
    **Réalisations**  
    - Logique métier et gestion des réservations
    - Interface utilisateur fonctionnelle
    - Intégration API temps réel
    - Génération de rapports
    
    **Valeur**  
    - Application livrée de bout en bout
    - Workflow automatisé
    - Intégration maîtrisée
    
    **Compétences**  
    Développement d'applications data • Intégration d'API • Process Automation
    """)

st.markdown("---")

# === 7. CTA — CONVERSION ===
st.markdown("""
<div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%); border-radius: 20px;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem;">
        Disponible pour des opportunités data
    </h2>
    <p style="font-size: 1.3rem; color: #6b7280; margin-bottom: 2.5rem; max-width: 760px; margin-left: auto; margin-right: auto;">
        Je conçois des solutions data concrètes,
        orientées terrain, automatisation et prise de décision.
    </p>
    <div style="display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap;">
        <a href="tel:+221771479009" style="display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; padding: 1rem 2.5rem; border-radius: 50px; font-size: 1.2rem; font-weight: 600; text-decoration: none; box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4); transition: transform 0.3s ease;">
            📞 Appelez-moi
        </a>
        <a href='mailto:dioufmakhtar77@gmail.com?subject=Projet%20Data%20-%20Contact%20Portfolio' style='display: inline-block; background: linear-gradient(135deg, #dc2626 0%, #ea580c 100%); color: white; padding: 1rem 2.5rem; border-radius: 50px; font-size: 1.2rem; font-weight: 600; text-decoration: none; box-shadow: 0 8px 20px rgba(220, 38, 38, 0.4); transition: transform 0.3s ease;'>
            ✉️ Écrivez-moi
        </a>
    </div>
""", unsafe_allow_html=True)
