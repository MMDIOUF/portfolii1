import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card
from components.badges import create_badge

st.set_page_config(page_title="Expertise Technique", layout="wide")
inject_custom_css()

# === HERO ===
st.markdown("""
<div style="text-align: center; padding: 5rem 2rem 4rem;">
    <h1 style="font-size: 3.2rem; font-weight: 800; color: #1f2937; margin-bottom: 1.5rem;">
        ⚡ Expertise Data & Analytics
    </h1>
    <p style="font-size: 1.4rem; color: #6b7280; max-width: 860px; margin: 0 auto; line-height: 1.6;">
        Des compétences techniques solides,
        mises au service de problématiques réelles :
        analyse, automatisation, pilotage et prise de décision.
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# === DATA ANALYSIS & BI ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        📊 Data Analysis & Business Intelligence
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Comprendre les données, révéler les insights et éclairer les décisions métier.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Visualisation & Dashboards",
        {
            "Dashboards": "Conception d'applications décisionnelles",
            "Visualisations": "Graphiques dynamiques orientés analyse",
            "Exploration": "Analyse visuelle et descriptive",
            "Reporting": "Suivi de KPI et analyses opérationnelles"
        },
        "📊",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Analyse de Données",
        {
            "Data Science": "Python pour l'analyse et la modélisation",
            "Statistiques": "Analyse statistique et exploration",
            "SQL": "Extraction, transformation et analyse",
            "Interprétation": "Résultats pour décisions métier"
        },
        "🔍",
        "info"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Data Analysis & BI"):
    st.markdown("""
    **Exemples de travaux réalisés**
    - Tableaux de bord de suivi de performance et d'activité
    - Automatisation de reportings récurrents
    - Analyses exploratoires pour comprendre comportements et tendances
    - Construction et suivi d'indicateurs clés orientés décision
    """)

st.markdown("---")

# === DATA ENGINEERING ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        ⚙️ Data Engineering & Automatisation
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Structurer, automatiser et fiabiliser les flux de données.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "ETL & Pipelines",
        {
            "Conception": "Pipelines de données automatisés",
            "Intégration": "Transformation multi-sources",
            "Orchestration": "Workflows data complexes",
            "Fiabilisation": "Contrôle qualité des flux"
        },
        "🔄",
        "success"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Big Data",
        {
            "Traitement": "Volumes de données importants",
            "Analyse": "Distribuée et scalable",
            "Préparation": "Données pour analytics avancés",
            "Ingestion": "Batch & Streaming"
        },
        "📦",
        "warning"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Data Engineering"):
    st.markdown("""
    **Cas d'usage**
    - Automatisation de chaînes de traitement de données
    - Mise en place de contrôles de qualité et de cohérence
    - Optimisation des performances de traitements
    - Préparation de données pour BI et analytics
    """)

st.markdown("---")

# === MACHINE LEARNING ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🤖 Machine Learning & IA
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Exploiter les données pour anticiper, segmenter et prédire.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Machine Learning",
        {
            "Développement": "Modèles prédictifs",
            "Expérimentation": "Évaluation et validation",
            "Approches": "Supervisé et non supervisé",
            "Deep Learning": "Cas d'usage business"
        },
        "🤖",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Techniques ML",
        {
            "Prédiction": "Classification & Régression",
            "Analyses": "Tendances et prévisions",
            "Segmentation": "Clustering & Profiling",
            "Détection": "Anomalies et patterns"
        },
        "🎯",
        "info"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Machine Learning"):
    st.markdown("""
    **Exemples de projets**
    - Modèles de prédiction (churn, souscription, estimation)
    - Segmentation et scoring de clients
    - Détection de patterns et d'anomalies
    """)

st.markdown("---")

# === WEB & DATABASES ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🌐 Web Development & Databases
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Concevoir des applications data exploitables de bout en bout.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Développement Web",
        {
            "Applications": "Data-driven interactives",
            "Intégration": "APIs et données externes",
            "Interfaces": "Simples et fonctionnelles",
            "Production": "Déploiement d'outils data"
        },
        "🌐",
        "success"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Bases de Données",
        {
            "Modélisation": "Bases relationnelles",
            "Optimisation": "Requêtes et performances",
            "Gestion": "Données applicatives et analytiques",
            "Environnements": "On-premise et cloud"
        },
        "🗄️",
        "warning"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Web & Databases"):
    st.markdown("""
    **Réalisations**
    - Applications web data-driven
    - Dashboards interactifs déployés
    - Intégration de bases de données et APIs
    """)

st.markdown("---")

# === CLOUD & DEVOPS ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        ☁️ Cloud & DevOps
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Déployer, sécuriser et faire évoluer des solutions data.
    </p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Cloud Platforms",
        {
            "Déploiement": "Applications et pipelines data",
            "Stockage": "Traitement cloud scalable",
            "Gestion": "Accès et ressources",
            "Architecture": "Multi-cloud et hybride"
        },
        "☁️",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Outils & Pratiques",
        {
            "Versions": "Gestion et collaboration",
            "Conteneurisation": "Applications portables",
            "Automatisation": "Déploiements continus",
            "Monitoring": "Fiabilité et maintenance"
        },
        "🛠️",
        "info"
    ), unsafe_allow_html=True)

with st.expander("🔍 Détails — Cloud & DevOps"):
    st.markdown("""
    **Pratiques mises en œuvre**
    - Déploiement d'applications data
    - Gestion de code et documentation
    - Approche orientée fiabilité et maintenabilité
    """)

st.markdown("---")

# === SOFT SKILLS ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🎯 Compétences Transversales
    </h2>
    <p style="color: #6b7280; font-size: 1.2rem;">
        Savoir collaborer, expliquer et s'adapter aux enjeux métier.
    </p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_info_card(
        "Communication",
        {
            "Présentation": "Résultats techniques clairs",
            "Vulgarisation": "Analyses complexes",
            "Collaboration": "Profils non techniques"
        },
        "💬",
        "primary"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Gestion de Projet",
        {
            "Organisation": "Structuration du travail",
            "Priorisation": "Impact métier",
            "Autonomie": "Sens des responsabilités"
        },
        "📋",
        "success"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(create_info_card(
        "Mindset",
        {
            "Approche": "Pragmatique orientée solution",
            "Apprentissage": "Continu",
            "Adaptabilité": "Contextes variés"
        },
        "🧠",
        "info"
    ), unsafe_allow_html=True)

st.markdown("---")

# === FORMATION ===
st.markdown("""
<div style="padding: 2rem 0 1rem;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 0.5rem;">
        🎓 Formation & Certifications
    </h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎓 Diplômes
    - **Master Data Science & IA** - ISI Dakar (2024-2026)
    - **Master Big Data** - ISM Dakar (2023-2024)
    - **Licence Génie Logiciel** - ISM Dakar (2020-2023)
    """)

with col2:
    st.markdown("""
    ### 📚 Formations Continues
    - Power BI Advanced Analytics
    - AWS Cloud Practitioner
    - Machine Learning Specialization
    - Big Data Engineering
    """)

st.markdown("---")



# === CTA ===
st.markdown("""
<div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%); border-radius: 20px;">
    <h2 style="font-size: 2.2rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem;">
        Ouvert aux opportunités data
    </h2>
    <p style="font-size: 1.3rem; color: #6b7280; margin-bottom: 2.5rem; max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.5;">
        Je souhaite mettre en pratique mes connaissances, apprendre de nouvelles compétences, relever de nouveaux défis et participer activement à des projets data stimulants au sein d’entreprises innovantes.
    </p>
    <a href="tel:+221771479009" style="display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; padding: 1rem 3rem; border-radius: 50px; font-size: 1.2rem; font-weight: 600; text-decoration: none; box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4); transition: transform 0.3s ease;">
        📞 Me Contacter
    </a>
</div>
""", unsafe_allow_html=True)
