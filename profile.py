import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Yash Rai Sharma | Technocrat", layout="wide")

# --- KVS CORPORATE UI/UX STYLING ---
st.markdown("""
    <style>
    :root {
        --kvs-navy: #1a365d;
        --kvs-gold: #c0a062;
        --kvs-light-bg: #fdfdfd;
    }

    .stApp { background-color: #ffffff; }

    /* Top Navy Banner */
    .top-nav {
        background-color: var(--kvs-navy);
        padding: 12px 60px;
        display: flex;
        justify-content: space-between;
        color: white;
        font-weight: 600;
        font-size: 0.9rem;
        border-bottom: 5px solid var(--kvs-gold);
    }

    /* Corporate Header */
    .header-section {
        padding: 50px 10%;
        background-color: white;
        border-bottom: 1px solid #eeeeee;
    }

    .name-title {
        font-size: 48px;
        font-weight: 800;
        color: var(--kvs-navy);
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    .sub-title {
        color: var(--kvs-gold);
        font-size: 20px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-top: -5px;
    }

    /* Service-Style Content Blocks */
    .kvs-card {
        border: 1px solid #e5e7eb;
        padding: 35px;
        background-color: var(--kvs-light-bg);
        border-top: 6px solid var(--kvs-navy);
        height: 100%;
        transition: all 0.3s ease;
    }

    .kvs-card:hover {
        border-top: 6px solid var(--kvs-gold);
        box-shadow: 0 15px 30px rgba(0,0,0,0.08);
    }

    .card-header {
        color: var(--kvs-navy);
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 20px;
        text-transform: uppercase;
    }

    /* Typography Polish */
    p, li { color: #4b5563; line-height: 1.8; font-size: 1.05rem; }
    h2 { color: var(--kvs-navy) !important; font-weight: 800 !important; border-left: 5px solid var(--kvs-gold); padding-left: 15px; }

    /* Buttons */
    .stButton>button {
        background-color: var(--kvs-navy) !important;
        color: white !important;
        border-radius: 0px !important;
        border: none !important;
        padding: 15px 40px !important;
        font-weight: 700 !important;
    }
    
    .stButton>button:hover {
        background-color: var(--kvs-gold) !important;
    }

    /* Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- TOP CONTACT BAR ---
st.markdown("""
    <div class="top-nav">
        <div>📞 +91 95501 16685</div>
        <div>📧 yashraisharma01@gmail.com</div>
        <div style="letter-spacing: 1px;">GITHUB • LINKEDIN</div>
    </div>
    """, unsafe_allow_html=True)

# --- CORPORATE BRANDING ---
st.markdown("""
    <div class="header-section">
        <div class="name-title">YASH RAI SHARMA</div>
        <div class="sub-title">Technocrat & Software Engineer</div>
    </div>
    """, unsafe_allow_html=True)

# --- PROFESSIONAL SUMMARY ---
with st.container():
    col_a, col_b = st.columns([2.5, 1], gap="large")
    with col_a:
        st.header("Executive Summary")
        st.write("""
            Technocrat with deep technical bases in **Software Development, Quantum Computing, Augmented/Virtual Reality, and Cyber Security**. 
            I am a B.Tech Computer Science graduate from **SRM Institute of Science and Technology** with a 8.5 CGPA.
        """)
        st.write("""
            With leadership experience as a **Director at VechTech Consulting** and as a **Core-Quantum Lead**, I am driven to deliver 
            impactful technological solutions[cite: 1].
        """)
    with col_b:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("DOWNLOAD CV")
        st.button("REQUEST CALLBACK")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- CORE EXPERTISE GRID (KVS STYLE) ---
st.header("Expertise & Specializations")
g1, g2, g3 = st.columns(3)

with g1:
    st.markdown("""
        <div class="kvs-card">
            <div class="card-header">SOFTWARE ENG.</div>
            <p>Specialized in <b>Python3, C++, React JS, and JavaScript</b>[cite: 1]. Experienced in developing speech recognition software and ERP solutions[cite: 1].</p>
        </div>
    """, unsafe_allow_html=True)

with g2:
    st.markdown("""
        <div class="kvs-card">
            <div class="card-header">CYBER SECURITY</div>
            <p>Hands-on experience in <b>Offensive Security</b> and handling government tenders for <b>Security Operations Centers (SOCs)</b>[cite: 1].</p>
        </div>
    """, unsafe_allow_html=True)

with g3:
    st.markdown("""
        <div class="kvs-card">
            <div class="card-header">EMERGING TECH</div>
            <p>Pioneering research in <b>Quantum Computing</b> and developing <b>VR/AR Navigation Systems</b> using Unity and Blender[cite: 1].</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- WORK HISTORY SECTION ---
st.header("Professional Experience")
tab1, tab2, tab3 = st.tabs(["Leadership", "Engineering", "Research"])

with tab1:
    st.subheader("Director | VechTech Consulting Private Limited")
    st.caption("Apr 2023 - Present[cite: 1]")
    st.write("""
    - Managed company operations and organizational dynamics[cite: 1].
    - Led technical projects involving speech recognition and ERP implementation[cite: 1].
    - Managed a freelance team to successfully deliver over 6 web development projects[cite: 1].
    """)

with tab2:
    st.subheader("Application Development Intern | HappiApps")
    st.write("- Focused on **UI/UX and Front-end Engineering** in a collaborative environment[cite: 1].")
    st.subheader("Cyber Security Intern | Allvy Software Solutions")
    st.write("- Involved in establishing **Cyber Network Operations Centers (C-NOCs)**[cite: 1].")

with tab3:
    st.subheader("Core-Quantum Lead | Quantum Computing Lab SRM")
    st.write("- Led a dynamic team of 50+ members driving innovative research and strategic partnerships[cite: 1].")

# --- ACHIEVEMENTS & AWARDS ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.header("Recognition")
st.success("**Excellence Award for Entrepreneurship, Management, and Startups** (SRM, May 2024)[cite: 1]")

# --- FOOTER ---
st.markdown("""
    <div style="background-color: #1a365d; color: white; padding: 60px; text-align: center; margin-top: 100px;">
        <h2 style="color: white !important; border:none;">Let's Build the Future Together</h2>
        <p style="color: #cbd5e1;">Available for global opportunities in Emerging Tech & Leadership.</p>
        <div style="margin-top:20px;">
            <span style="margin: 0 15px;">GITHUB</span> | <span style="margin: 0 15px;">LINKEDIN</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
