import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card

st.set_page_config(page_title="Applications Déployées", layout="wide")
inject_custom_css()

# === HERO ===
st.markdown("""
<div style="text-align: center; padding: 3rem 2rem 2rem;">
    <h1 style="font-size: 2.5rem; font-weight: 800; color: #1f2937; margin-bottom: 1rem;">
        🚀 Applications Data & Analytics Déployées
    </h1>
    <p style="font-size: 1.2rem; color: #6b7280; max-width: 800px; margin: 0 auto; line-height: 1.6;">
        Une sélection d'applications data concrètes, conçues pour automatiser des processus,
        analyser des données et faciliter la prise de décision.
        Chaque solution est accessible en ligne, fonctionnelle et orientée usage métier.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# === APPLICATIONS ===
st.markdown("""
<div style="padding: 1rem 0;">
    <p style="color: #6b7280; font-size: 1.1rem; text-align: center; margin-bottom: 2rem;">
        Ces applications illustrent ma capacité à transformer des besoins métier
        en outils data opérationnels : automatisation, visualisation, pilotage et analyse.
    </p>
</div>
""", unsafe_allow_html=True)

# PREMIÈRE LIGNE
col1, col2 = st.columns(2)

with col1:
    st.markdown(create_info_card(
        "Codific",
        {
            "Type": "Application métier",
            "Statut": "✅ En ligne",
            "Tech": "Streamlit"
        },
        "🔢",
        "primary"
    ), unsafe_allow_html=True)
    
    with st.expander("📋 Détails"):
        st.markdown("""
        **Description**  
        Application de codification conçue pour structurer, normaliser et exploiter efficacement des données issues d'enquêtes, formulaires ou bases opérationnelles.
        
        **Fonctionnalités**
        - Codification assistée pour données qualitatives et quantitatives
        - Automatisation des règles de traitement et de contrôle
        - Réduction des erreurs manuelles et gain de temps opérationnel
        - Export prêt pour analyse et reporting
        
        **Compétences**  
        Data Cleaning & Quality • Process Automation • Applications Data
        """)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
        <a href="https://codific-tuzy4umskjyflktnd4nrz4.streamlit.app/" target="_blank" 
           title="Ouvrir l'application Codific dans un nouvel onglet"
           style="display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); 
                  color: white; padding: 0.7rem 1.8rem; border-radius: 30px; font-size: 1rem; 
                  font-weight: 600; text-decoration: none; box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);">
            🔗 Accéder à l'application
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(create_info_card(
        "Espace",
        {
            "Type": "Dashboard interactif",
            "Statut": "✅ En ligne",
            "Tech": "Streamlit"
        },
        "🌐",
        "info"
    ), unsafe_allow_html=True)
    
    with st.expander("📋 Détails"):
        st.markdown("""
        **Description**  
        Plateforme de pilotage permettant de centraliser les données, suivre les indicateurs clés et visualiser la performance en temps quasi réel.
        
        **Fonctionnalités**
        - Tableaux de bord dynamiques orientés KPI
        - Visualisations interactives pour l'analyse rapide
        - Suivi de performance et aide à la décision
        
        **Compétences**  
        Business Intelligence • KPI Design • Data Visualization
        """)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
        <a href="https://espace-wcaweyo3lafsgbfkhcbhid.streamlit.app/" target="_blank" 
           title="Ouvrir la plateforme Espace dans un nouvel onglet"
           style="display: inline-block; background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%); 
                  color: white; padding: 0.7rem 1.8rem; border-radius: 30px; font-size: 1rem; 
                  font-weight: 600; text-decoration: none; box-shadow: 0 4px 12px rgba(6, 182, 212, 0.3);">
            🔗 Accéder à l'application
        </a>
    </div>
    """, unsafe_allow_html=True)

# DEUXIÈME LIGNE
col3, col4 = st.columns(2)

with col3:
    st.markdown(create_info_card(
        "PanelRush",
        {
            "Type": "Analytics Dashboard",
            "Statut": "✅ En ligne",
            "Tech": "Streamlit"
        },
        "📊",
        "success"
    ), unsafe_allow_html=True)
    
    with st.expander("📋 Détails"):
        st.markdown("""
        **Description**  
        Dashboard analytique conçu pour explorer des données, analyser des tendances et suivre des indicateurs de performance clés.
        
        **Fonctionnalités**
        - Analyse exploratoire et descriptive des données
        - Visualisations interactives orientées insights
        - Génération de rapports analytiques automatisés
        
        **Compétences**  
        Data Analysis & Exploration • Data Storytelling • Reporting automatisé
        """)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
        <a href="https://panelrush-pgkrzahnbuh64jqvk84miy.streamlit.app/" target="_blank" 
           title="Ouvrir le dashboard PanelRush dans un nouvel onglet"
           style="display: inline-block; background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                  color: white; padding: 0.7rem 1.8rem; border-radius: 30px; font-size: 1rem; 
                  font-weight: 600; text-decoration: none; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);">
            🔗 Accéder à l'application
        </a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(create_info_card(
        "Projet App",
        {
            "Type": "Full-stack App",
            "Statut": "✅ En ligne",
            "Tech": "Streamlit"
        },
        "💼",
        "warning"
    ), unsafe_allow_html=True)
    
    with st.expander("📋 Détails"):
        st.markdown("""
        **Description**  
        Application data multi-modules développée pour expérimenter l'intégration de plusieurs fonctionnalités métier au sein d'une seule interface.
        
        **Fonctionnalités**
        - Modules de gestion et de visualisation de données
        - Interface utilisateur structurée et intuitive
        - Intégration et exploitation de jeux de données multiples
        
        **Compétences**  
        Applications Data-driven • Intégration de données • Data Visualization
        """)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 1rem; margin-bottom: 2rem;">
        <a href="https://projet-app-fapss8tcjth8bawqszazjp.streamlit.app/" target="_blank" 
           title="Ouvrir l'application Projet App dans un nouvel onglet"
           style="display: inline-block; background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); 
                  color: white; padding: 0.7rem 1.8rem; border-radius: 30px; font-size: 1rem; 
                  font-weight: 600; text-decoration: none; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);">
            🔗 Accéder à l'application
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

