import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Yash Rai Sharma | Portfolio", layout="wide")

# --- ADVANCED UI/UX CSS ---
st.markdown("""
    <style>
    /* Professional Color Palette & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }

    .stApp {
        background-color: #ffffff;
    }

    /* Hero Section */
    .hero-container {
        padding: 5rem 2rem;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        border-radius: 0 0 50px 50px;
        color: white;
        text-align: center;
        margin-bottom: 4rem;
    }

    .hero-title { font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem; }
    .hero-subtitle { font-size: 1.25rem; opacity: 0.9; font-weight: 400; }

    /* Service/Competency Cards */
    .card-container {
        display: flex;
        gap: 20px;
        margin-bottom: 3rem;
    }

    .ux-card {
        background: #f8fafc;
        padding: 2.5rem;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .ux-card:hover {
        transform: translateY(-12px);
        background: white;
        border-color: #3b82f6;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }

    .card-icon { font-size: 2.5rem; margin-bottom: 1.5rem; display: block; }
    .card-title { font-size: 1.5rem; font-weight: 700; color: #1e293b; margin-bottom: 1rem; }
    .card-text { color: #64748b; line-height: 1.6; }

    /* Success/Achievement Banner */
    .stat-banner {
        background: #f1f5f9;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        border-left: 10px solid #3b82f6;
        margin-top: 2rem;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown(f"""
    <div class="hero-container">
        <div class="hero-title">Yash Rai Sharma</div>
        <div class="hero-subtitle">Senior Growth Content Engineer & Software Professional</div>
        <div style="margin-top: 20px; opacity: 0.8;">📍 Hyderabad, India</div>
    </div>
    """, unsafe_allow_html=True)

# --- ABOUT SECTION ---
col1, col2 = st.columns([2, 1])
with col1:
    st.header("Strategic Growth Architecture")
    st.write("""
        Highly analytical Growth Engineer with a background in Software Engineering. 
        I specialize in bridging the gap between complex technical infrastructure and 
        high-velocity marketing growth.
    """)
    st.write("""
        Currently serving as an **Assistant Growth Manager at Apollo 247**, I lead 
        marketing automation experiments and technical integrations that scale.
    """)

# --- COMPETENCIES (CARD UI) ---
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="ux-card">
            <span class="card-icon">⚙️</span>
            <div class="card-title">Technical Stack</div>
            <div class="card-text">Python, SQL, and Google Apps Script. Mastery in CleverTap & Segment API integrations.</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="ux-card">
            <span class="card-icon">🚀</span>
            <div class="card-title">Growth Strategy</div>
            <div class="card-text">Lifecycle experiments across WhatsApp, SMS, and Push Notification triggers.</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="ux-card">
            <span class="card-icon">🤖</span>
            <div class="card-title">AI Implementation</div>
            <div class="card-text">Utilizing Flash 3 models for high-velocity content generation and prompt engineering.</div>
        </div>
    """, unsafe_allow_html=True)

# --- ACHIEVEMENTS ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div class="stat-banner">
        <h3 style="margin-bottom:5px; color:#1e3a8a;">48,000+ Users Managed</h3>
        <p style="color:#475569; margin:0;">Real-time data synchronization infrastructure built with 70% reduction in manual overhead.</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
f1, f2, f3 = st.columns(3)
with f1: st.button("LinkedIn")
with f2: st.button("GitHub")
with f3: st.button("Email Me")
