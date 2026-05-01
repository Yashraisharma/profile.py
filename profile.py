import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Nandeep Rai Sharma | Portfolio", page_icon="👤", layout="centered")

# --- UI STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0f172a; }
    h1 { color: #38bdf8; font-weight: 700; }
    h2 { color: #818cf8; border-bottom: 1px solid #334155; padding-bottom: 10px; }
    .stMarkdown { line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER / BIO ---
st.title("Nandeep Rai Sharma")
st.write("### Senior Growth Content Engineer & Software Professional")
st.write("📍 Hyderabad, India")

st.info("""
Highly analytical Growth Engineer with a background in Software Engineering. 
I specialize in bridging the gap between complex technical infrastructure and 
high-velocity marketing growth.
""")

# --- EXPERIENCE SHOT ---
st.header("Professional Profile")
st.write("""
Currently serving as an **Assistant Growth Manager at Apollo 247**, I lead 
marketing automation experiments and technical integrations that scale. 
My work focuses on optimizing user lifecycles through precise data synchronization 
and AI-driven content strategies.
""")

# --- SKILL MATRIX ---
st.header("Core Competencies")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Technical Stack")
    st.write("- **Languages:** Python, SQL, Google Apps Script")
    st.write("- **Platforms:** CleverTap, Segment, GitHub")
    st.write("- **AI/ML:** Flash 3 Implementation, LLM Prompt Engineering")

with col2:
    st.subheader("Growth Strategy")
    st.write("- **Channels:** WhatsApp, SMS, Push Notification Triggers")
    st.write("- **Analytics:** Funnel Optimization, User Segmentation")
    st.write("- **Execution:** Automated Lifecycle Workflows")

# --- ACHIEVEMENTS ---
st.header("Key Highlights")
st.success("**Infrastructure:** Developed a Python ecosystem managing real-time data sync for 48,000+ users.")
st.success("**Automation:** Built custom scripts to streamline growth experiments, reducing manual overhead by 70%.")

# --- FOOTER ---
st.divider()
st.write("Connect with me to discuss growth engineering, marketing automation, or technical strategy.")

# Social Buttons
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/YOUR_PROFILE") # Update this
with c2:
    st.link_button("GitHub", "https://github.com/YOUR_USERNAME") # Update this
with c3:
    st.link_button("Contact via Email", "mailto:your.email@example.com")
