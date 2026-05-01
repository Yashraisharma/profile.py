import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Yash Rai Sharma | Technocrat", layout="wide")

# --- CUSTOM CSS FOR THE ANCIENT GOLD AESTHETIC ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&display=swap');

    /* Background: Dark Rock */
    .stApp {
        background: #050505;
        background-image: radial-gradient(circle at center, rgba(20, 20, 20, 0.8) 0%, rgba(0, 0, 0, 1) 100%),
                          url('https://www.transparenttextures.com/patterns/dark-stone.png');
        background-attachment: fixed;
        color: #d4d4d4;
    }

    /* Animated Gold Flow for Headers */
    @keyframes goldFlow {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 100%; }
    }

    .hero-name {
        font-family: 'Cinzel', serif;
        font-size: clamp(40px, 8vw, 85px);
        font-weight: 900;
        text-align: center;
        background: linear-gradient(180deg, #fcf6ba 0%, #bf953f 50%, #8a6d3b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 12px;
        filter: drop-shadow(0 5px 15px rgba(0,0,0,0.8));
        margin-bottom: 0px;
    }

    /* Verbatim Section Containers */
    .stone-block {
        background: rgba(10, 10, 10, 0.85);
        border: 1px solid rgba(191, 149, 63, 0.2);
        padding: 50px;
        margin: 60px auto;
        max-width: 900px;
        border-radius: 2px;
        border-left: 4px solid #bf953f;
        box-shadow: -15px 20px 40px rgba(0,0,0,0.8);
        transition: all 0.5s ease;
    }

    .stone-block:hover {
        transform: perspective(1000px) rotateY(-2deg) translateX(10px);
        border-color: #fcf6ba;
        background: rgba(20, 20, 20, 0.95);
    }

    .section-title {
        font-family: 'Cinzel', serif;
        color: #c0a062;
        font-size: 1.3rem;
        letter-spacing: 6px;
        margin-bottom: 25px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(191, 149, 63, 0.4);
        padding-bottom: 8px;
    }

    .resume-text {
        font-family: 'Montserrat', sans-serif;
        line-height: 1.9;
        font-size: 1.05rem;
        color: #c0c0c0;
        text-align: justify;
    }

    /* Gold Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #bf953f 0%, #8a6d3b 100%) !important;
        color: white !important;
        border: none !important;
        padding: 15px 40px !important;
        font-family: 'Cinzel', serif !important;
        letter-spacing: 3px !important;
        font-weight: 700 !important;
        width: 100% !important;
        border-radius: 0px !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- AUDIO LOGIC ---
# Using a standard audio player that stays at the top
st.markdown('<p style="text-align:center; font-family:Cinzel; color:#bf953f; letter-spacing:2px;">AMBIENT SOUNDSCAPE</p>', unsafe_allow_html=True)
st.audio("https://www.soundjay.com/nature/ocean-wave-1.mp3", format="audio/mpeg", loop=True)

# --- VERBATIM RESUME CONTENT ---
st.markdown('<h1 class="hero-name">YASH RAI SHARMA</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; letter-spacing:10px; color:#c0a062; font-family:Cinzel; margin-top:-20px; font-weight:700;">TECHNOCRAT | ENGINEER</p>', unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center; font-family:Montserrat; font-size:0.9rem; opacity:0.8; margin-bottom:80px; color:#bf953f;">
    +91 95501 16685 &nbsp; | &nbsp; yashraisharma01@gmail.com &nbsp; | &nbsp; github.com/yashraisharma
</div>
""", unsafe_allow_html=True)

# SUMMARY Section
st.markdown(f"""
<div class="stone-block">
    <div class="section-title">Summary</div>
    <div class="resume-text">
        Technocrat, with bases in <b>Software development, Quantum Computing, Augmented/Virtual Reality and Cyber Security</b>. 
        Aspiring to lead and learn, with experience in Project management, Human-Resource management, strategic partnerships and Innovation[cite: 1]. 
        Seeking opportunities to deliver impactful solutions, grasp and further technological advancements[cite: 1].
    </div>
</div>
""", unsafe_allow_html=True)

# EDUCATION Section
st.markdown(f"""
<div class="stone-block">
    <div class="section-title">Education</div>
    <div class="resume-text">
        <b>SRM Institute of Science and Technology, Chennai, TN</b><br>
        B.Tech, Computer Science Engineering w/s Software Engineering | May 2024 | CGPA: 8.5[cite: 1]<br><br>
        Relevant coursework: AI, OOPS, Operating Systems, Data Structures and Algorithms, Design and Analysis of Algorithms, DBMS[cite: 1]<br><br>
        <b>Fiitjee Junior College, Saifabad</b><br>
        Intermediate(+1 & +2) | Jun 2020 | Percentage: 71%[cite: 1]
    </div>
</div>
""", unsafe_allow_html=True)

# WORK EXPERIENCE Section
st.markdown(f"""
<div class="stone-block">
    <div class="section-title">Work Experience</div>
    <div class="resume-text">
        <p style="color:#fcf6ba; font-weight:700;">VechTech Consulting Private Limited, Hyderabad, TS: Director | Apr 2023</p>
        Actively served as Director at "VechTech Consulting Private Limited", Hyderabad, TS, Since April 2023, contributed to the company's operations and working processes[cite: 1]. 
        My experience within my father's company, has equipped me with essential management and critical thinking skills[cite: 1]. 
        This involvement has allowed me to hone my skills in decision-making, furthering the company's direction and success[cite: 1]. 
        With my role as a partaker in the company endeavors, I've gained valuable insights into effective running of a company, 
        enhancing my understanding of organizational dynamics and leadership principles[cite: 1].
    </div>
</div>
""", unsafe_allow_html=True)

# AWARDS Section
st.markdown(f"""
<div class="stone-block">
    <div class="section-title">Awards and Recognition</div>
    <div class="resume-text">
        <b>Excellence award SRM | MAY 2024</b>[cite: 1]<br>
        Recipient of the Excellence Award for Entrepreneurship, Management, and Startups from the School of Computing, SRM[cite: 1]. 
        This award underscores my commitment to fostering entrepreneurial spirit and effective management practices within the academic community and beyond[cite: 1].
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("CONNECT WITH YASH RAI SHARMA"):
    st.balloons()
