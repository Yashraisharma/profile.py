import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Yash Rai Sharma | Profile", layout="wide")

# --- KVS STYLE CSS ---
st.markdown("""
    <style>
    /* KVS Corporate Color Palette */
    :root {
        --kvs-navy: #1a365d;
        --kvs-gold: #c0a062;
        --kvs-text: #333333;
    }

    .stApp { background-color: #ffffff; }

    /* Top Navigation Simulation */
    .top-nav {
        background-color: var(--kvs-navy);
        padding: 10px 50px;
        display: flex;
        justify-content: space-between;
        color: white;
        font-weight: 600;
        border-bottom: 4px solid var(--kvs-gold);
    }

    /* Hero Branding Section */
    .hero-brand {
        padding: 40px 10% 20px 10%;
        background-color: white;
    }

    .name-title {
        font-size: 42px;
        font-weight: 800;
        color: var(--kvs-navy);
        text-transform: uppercase;
        margin-bottom: 0px;
    }

    .sub-title {
        color: var(--kvs-gold);
        font-size: 18px;
        letter-spacing: 2px;
        font-weight: 700;
        margin-top: -5px;
    }

    /* Destination/Service Blocks (The KVS Look) */
    .service-block {
        border: 1px solid #eeeeee;
        padding: 30px;
        background-color: #fdfdfd;
        border-top: 5px solid var(--kvs-navy);
        height: 100%;
    }

    .service-block:hover {
        border-top: 5px solid var(--kvs-gold);
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }

    .block-header {
        color: var(--kvs-navy);
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    /* CTA Section */
    .cta-strip {
        background-color: var(--kvs-navy);
        color: white;
        padding: 40px;
        text-align: center;
        margin-top: 50px;
    }

    /* Typography */
    h2 { color: var(--kvs-navy) !important; font-weight: 700 !important; }
    p { color: #555555; line-height: 1.8; }

    /* Buttons */
    .stButton>button {
        background-color: var(--kvs-gold) !important;
        color: white !important;
        border: none !important;
        border-radius: 0px !important;
        padding: 10px 30px !important;
    }

    /* Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SIMULATION ---
st.markdown("""
    <div class="top-nav">
        <div>YASH RAI SHARMA</div>
        <div>GROWTH • ENGINEERING • SOFTWARE</div>
    </div>
    """, unsafe_allow_html=True)

# --- HERO BRANDING ---
st.markdown("""
    <div class="hero-brand">
        <div class="name-title">YASH RAI SHARMA</div>
        <div class="sub-title">SENIOR GROWTH CONTENT ENGINEER</div>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN PROFILE BODY ---
container = st.container()
with container:
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.header("Professional Overview")
        st.write("""
            Based in **Hyderabad**, I am a high-impact Growth Engineer with a solid foundation in **Software Engineering**. 
            My expertise lies in the intersection of technical infrastructure and marketing velocity.
        """)
        st.write("""
            Currently, as an **Assistant Growth Manager at Apollo 247**, I manage mission-critical 
            marketing automation and data synchronization projects that drive user retention and acquisition at scale.
        """)
        
    with col2:
        st.header("Quick Contact")
        st.write("📞 Request Callback")
        st.write("📧 your.email@example.com")
        st.button("BOOK CONSULTATION")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- THE "KVS STYLE" GRID ---
st.header("Areas of Specialization")
grid_col1, grid_col2, grid_col3 = st.columns(3)

with grid_col1:
    st.markdown("""
        <div class="service-block">
            <div class="block-header">ENGINEERING</div>
            <p>Advanced Python automation and Google Apps Script workflows. 
            Specializing in complex API syncs for 48,000+ user databases.</p>
        </div>
    """, unsafe_allow_html=True)

with grid_col2:
    st.markdown("""
        <div class="service-block">
            <div class="block-header">GROWTH STRATEGY</div>
            <p>Lifecycle marketing via CleverTap and Segment. 
            Optimizing triggers across WhatsApp, SMS, and Push notifications.</p>
        </div>
    """, unsafe_allow_html=True)

with grid_col3:
    st.markdown("""
        <div class="service-block">
            <div class="block-header">AI INTEGRATION</div>
            <p>Leveraging Flash 3 models for precision content engineering 
            and automated marketing experiment generation.</p>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER CTA ---
st.markdown("""
    <div class="cta-strip">
        <h2>Let's Scale Your Growth Engine</h2>
        <p>Available for technical consulting and growth strategy audits.</p>
    </div>
    """, unsafe_allow_html=True)
