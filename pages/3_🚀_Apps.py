import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card

st.set_page_config(page_title="Applications Déployées", layout="wide")
inject_custom_css()

# === HERO ===
st.markdown("""
<div style="text-align: center; padding: 3rem 2rem 2rem;">
    <h1 style="font-size: 2.5rem; font-weight: 800; color: #1f2937; margin-bottom: 1rem;">
        🚀 Applications Déployées
    </h1>
    <p style="font-size: 1.2rem; color: #6b7280; max-width: 700px; margin: 0 auto; line-height: 1.5;">
        Découvrez mes réalisations en ligne, accessibles et opérationnelles.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# === APPLICATIONS ===
st.markdown("""
<div style="padding: 1rem 0;">
    <p style="color: #6b7280; font-size: 1.1rem; text-align: center; margin-bottom: 2rem;">
        Chaque application est déployée et prête à être explorée.
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
        Application de codification pour la gestion et le traitement de données structurées.
        
        **Fonctionnalités**
        - Interface intuitive de codification
        - Traitement automatisé des données
        - Export des résultats
        
        **Technologies**  
        `Streamlit` • `Python` • `Pandas`
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
        Plateforme de gestion complète avec tableaux de bord interactifs et suivi en temps réel.
        
        **Fonctionnalités**
        - Dashboard de gestion centralisé
        - Visualisations dynamiques
        - Suivi des indicateurs clés
        
        **Technologies**  
        `Streamlit` • `Python` • `Plotly`
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
        Tableau de bord analytique avancé pour l'analyse de données et la visualisation de KPIs.
        
        **Fonctionnalités**
        - Analyses statistiques avancées
        - Graphiques interactifs
        - Rapports automatisés
        
        **Technologies**  
        `Streamlit` • `Python` • `Pandas` • `Plotly`
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
        Application complète intégrant plusieurs fonctionnalités métier et modules de gestion.
        
        **Fonctionnalités**
        - Gestion multi-modules
        - Interface utilisateur complète
        - Intégration de données
        
        **Technologies**  
        `Streamlit` • `Python` • `Pandas`
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

# === CTA ===
st.markdown("""
<div style="text-align: center; padding: 3rem 2rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%); border-radius: 20px;">
    <h2 style="font-size: 1.8rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem;">
        Besoin d'une application similaire ?
    </h2>
    <p style="font-size: 1.1rem; color: #6b7280; margin-bottom: 2rem; max-width: 600px; margin-left: auto; margin-right: auto;">
        Je développe des applications web sur mesure, du prototype au déploiement.
    </p>
    <div style="display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap;">
        <a href="tel:+221771479009" style="display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; padding: 0.8rem 2rem; border-radius: 50px; font-size: 1rem; font-weight: 600; text-decoration: none; box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4);">
            📞 Appelez-moi
        </a>
        <a href='mailto:dioufmakhtar77@gmail.com?subject=Projet%20Application%20-%20Contact' style='display: inline-block; background: linear-gradient(135deg, #dc2626 0%, #ea580c 100%); color: white; padding: 0.8rem 2rem; border-radius: 50px; font-size: 1rem; font-weight: 600; text-decoration: none; box-shadow: 0 8px 20px rgba(220, 38, 38, 0.4);'>
            ✉️ Écrivez-moi
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
