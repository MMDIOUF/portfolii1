import streamlit as st
from components.design_system import inject_custom_css
from components.cards import create_info_card, create_metric_card
from components.alerts import create_alert
from components.badges import create_badge

# Configuration de la page
st.set_page_config(
    page_title="MOUHAMADOU MAKHTAR DIOUF - Data Analyst",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏠"
)

# Injection du CSS personnalisé
inject_custom_css()

# === HERO COMPACT ===
st.markdown("""
<div style='text-align: center; padding: 2rem 1rem 1rem;'>
    <h1 style='font-size: 2.8rem; font-weight: 800; color: #1f2937; margin-bottom: 1rem; line-height: 1.2;'>
        Les organisations collectent des données.<br/>
        <span style='background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            Peu savent les exploiter.
        </span>
    </h1>
    <p style='font-size: 1.2rem; color: #6b7280; max-width: 600px; margin: 0 auto 1rem;'>
        Entre fichiers dispersés et décisions tardives, <strong>la donnée devient un frein.</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# === PRÉSENTATION COMPACTE ===
st.markdown("""
<div style='text-align: center; padding: 1.5rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(168, 85, 247, 0.08) 100%); border-radius: 15px; margin: 1rem 0;'>
<h2 style='font-size: 2.2rem; font-weight: 800; color: #1f2937; margin-bottom: 0.5rem;'>
MOUHAMADOU MAKHTAR DIOUF
</h2>
<p style='font-size: 1.2rem; color: #6366f1; font-weight: 600; margin-bottom: 1rem;'>
Data Analyst • Data Science • Systèmes Data Décisionnels
</p>
<p style='font-size: 1rem; color: #374151; margin-bottom: 1rem;'>
Je transforme vos données en <strong>outils de décision</strong>
</p>
<p style='font-size: 0.9rem; color: #6b7280; margin-bottom: 1rem;'>
📍 Dakar, Sénégal • Disponible immédiatement
</p>

<div style='display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;'>
    <a href='tel:+221771479009' style='display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; padding: 0.8rem 2rem; border-radius: 25px; font-size: 1rem; font-weight: 600; text-decoration: none; box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);'>
        📞 Appelez-moi
    </a>
    <a href='mailto:dioufmakhtar77@gmail.com?subject=Projet%20Data%20-%20Contact%20Portfolio' style='display: inline-block; background: linear-gradient(135deg, #dc2626 0%, #ea580c 100%); color: white; padding: 0.8rem 2rem; border-radius: 25px; font-size: 1rem; font-weight: 600; text-decoration: none; box-shadow: 0 4px 15px rgba(220, 38, 38, 0.3);'>
        ✉️ Écrivez-moi
    </a>
</div>
</div>
""", unsafe_allow_html=True)

# === LA SOLUTION ===
st.markdown("""
<div style='text-align: center; padding: 1.5rem; background: #f8fafc; border-radius: 15px; margin: 1rem 0;'>
    <h3 style='font-size: 1.8rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem;'>
        💡 La Solution
    </h3>
    <p style='font-size: 1.1rem; color: #374151; line-height: 1.6;'>
        Je conçois des <strong>systèmes data</strong> qui transforment des données complexes en outils simples, 
        des indicateurs flous en décisions claires.
    </p>
</div>
""", unsafe_allow_html=True)

# === À PROPOS COMPACT ===
st.markdown("""
<div style='padding: 1.5rem; background: white; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 1rem 0;'>
<h3 style='font-size: 1.6rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem; text-align: center;'>
👤 À Propos
</h3>
<p style='font-size: 1rem; color: #374151; text-align: center; margin-bottom: 1rem;'>
<strong>Data Analyst orienté impact.</strong> Mon approche : une donnée n'a de valeur que si elle aide à décider.
</p>

<div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;'>
<div style='text-align: center; padding: 1rem; background: #f8fafc; border-radius: 10px;'>
<div style='font-size: 1.5rem; margin-bottom: 0.5rem;'>🎯</div>
<h4 style='color: #1f2937; font-size: 0.9rem; margin-bottom: 0.3rem;'>Mission</h4>
<p style='color: #6b7280; font-size: 0.8rem;'>Données → Décisions</p>
</div>
<div style='text-align: center; padding: 1rem; background: #f8fafc; border-radius: 10px;'>
<div style='font-size: 1.5rem; margin-bottom: 0.5rem;'>⚡</div>
<h4 style='color: #1f2937; font-size: 0.9rem; margin-bottom: 0.3rem;'>Expertise</h4>
<p style='color: #6b7280; font-size: 0.8rem;'>Collecte → Analyse → Automatisation</p>
</div>
<div style='text-align: center; padding: 1rem; background: #f8fafc; border-radius: 10px;'>
<div style='font-size: 1.5rem; margin-bottom: 0.5rem;'>🚀</div>
<h4 style='color: #1f2937; font-size: 0.9rem; margin-bottom: 0.3rem;'>Valeur</h4>
<p style='color: #6b7280; font-size: 0.8rem;'>Moins d'erreurs, plus de vitesse</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# === PREUVE PAR L'IMPACT ===
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; color: white; margin: 1rem 0;'>
    <h3 style='font-size: 1.8rem; font-weight: 700; margin-bottom: 1rem; text-align: center;'>
        🏢 Preuve par l'Impact : IPSOS
    </h3>
    <p style='font-size: 1rem; opacity: 0.95; margin-bottom: 1rem; text-align: center;'>
        Cabinet d'études avec équipes terrain. Besoin : décisions rapides et fiables.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div style='background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #6366f1; height: 100%;'>
<h4 style='color: #6366f1; font-size: 1.2rem; margin-bottom: 1rem;'>⚙️ Actions</h4>
<ul style='font-size: 0.9rem; color: #374151; line-height: 1.6;'>
<li>Dashboards décisionnels</li>
<li>Automatisation codification</li>
<li>KPIs fiables</li>
<li>Réduction traitements manuels</li>
</ul>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div style='background: white; padding: 1.5rem; border-radius: 12px; border-left: 4px solid #10b981; height: 100%;'>
<h4 style='color: #10b981; font-size: 1.2rem; margin-bottom: 1rem;'>✅ Résultat</h4>
<p style='font-size: 1rem; color: #374151; font-weight: 600;'>
Managers décident avec des <span style='color: #10b981;'>chiffres fiables</span>
</p>
<div style='margin-top: 1rem; padding: 0.8rem; background: #d1fae5; border-radius: 8px;'>
<p style='color: #065f46; font-size: 0.9rem; font-weight: 600; margin: 0;'>
💡 Décisions plus rapides, erreurs réduites
</p>
</div>
</div>
""", unsafe_allow_html=True)

# === MÉTRIQUES COMPACTES ===
st.markdown("""
<div style='text-align: center; padding: 1.5rem; margin: 1rem 0;'>
    <h3 style='font-size: 1.6rem; font-weight: 700; color: #1f2937; margin-bottom: 1rem;'>
        📈 Impact Mesurable
    </h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(create_metric_card("1+", "Années", "⏱️", "success"), unsafe_allow_html=True)

with col2:
    st.markdown(create_metric_card("10+", "Projets", "🚀", "default"), unsafe_allow_html=True)

with col3:
    st.markdown(create_metric_card("70%", "Réduction erreurs", "✅", "success"), unsafe_allow_html=True)

# === CTA FINAL COMPACT ===
st.markdown("""
<div style='background: linear-gradient(135deg, #1f2937 0%, #111827 100%); padding: 2rem; border-radius: 15px; text-align: center; color: white; margin: 1rem 0;'>
    <h3 style='font-size: 1.8rem; font-weight: 800; margin-bottom: 1rem;'>
        Je construis des <span style='background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>outils de décision</span>
    </h3>
    <p style='font-size: 1rem; opacity: 0.9; margin-bottom: 1.5rem;'>
        Disponible immédiatement • Data Analysis, Data Science et Automatisation
    </p>
    <a href='tel:+221771479009' style='display: inline-block; background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; padding: 1rem 2.5rem; border-radius: 25px; font-size: 1.1rem; font-weight: 600; text-decoration: none; box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);'>
        📞 Me Contacter
    </a>
    <p style='font-size: 0.9rem; opacity: 0.7; margin-top: 1rem;'>
        📞 +221 77 147 90 09 | Dakar, Sénégal
    </p>
</div>
""", unsafe_allow_html=True)
