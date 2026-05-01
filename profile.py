import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Yash Rai Sharma | Technocrat", layout="wide")

# --- CINEMATIC CSS INJECTION ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Inter:wght@300;400;600&display=swap');

    /* Background: Ancient Jagged Rock Texture */
    .stApp {
        background: radial-gradient(circle at center, rgba(20, 20, 20, 0.8) 0%, rgba(0, 0, 0, 1) 100%),
                    url('https://www.transparenttextures.com/patterns/dark-stone.png'),
                    #050505;
        background-attachment: fixed;
        color: #e0e0e0;
    }

    /* Animated Liquid Gold Flow effect */
    @keyframes goldFlow {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 100%; }
    }

    .gold-header {
        font-family: 'Cinzel', serif;
        background: linear-gradient(90deg, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: goldFlow 5s linear infinite;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 5px;
    }

    /* 3D "Rock Crevice" Section Design */
    .crevice-section {
        background: rgba(10, 10, 10, 0.6);
        border-left: 3px solid #b38728;
        padding: 40px;
        margin-bottom: 50px;
        border-radius: 0 30px 30px 0;
        box-shadow: -10px 0px 20px rgba(0,0,0,0.5);
        transition: transform 0.6s cubic-bezier(0.22, 1, 0.36, 1);
        perspective: 1000px;
    }

    .crevice-section:hover {
        transform: perspective(1000px) rotateY(-3deg) translateX(10px);
        background: rgba(179, 135, 40, 0.03);
        border-left: 3px solid #fcf6ba;
    }

    .section-label {
        font-family: 'Cinzel', serif;
        color: #bf953f;
        font-size: 1.2rem;
        letter-spacing: 3px;
        margin-bottom: 15px;
    }

    /* Verbatim Text Styling */
    p, li {
        font-family: 'Inter', sans-serif;
        line-height: 1.8;
        color: #c0c0c0;
        text-align: justify;
    }

    b, strong { color: #fcf6ba; }

    /* Hide standard Streamlit UI */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 🌊 AMBIENT WAVES AUDIO ---
st.markdown("""
    <audio autoplay loop>
        <source src="https://www.soundjay.com/nature/ocean-wave-1.mp3" type="audio/mpeg">
    </audio>
    <div style="text-align:right; font-size:10px; color:#444;">Ambient Audio Enabled</div>
    """, unsafe_allow_html=True)

# --- RESUME CONTENT ---
with st.container():
    # HERO
    st.markdown('<h1 class="gold-header" style="font-size: 75px; margin-bottom:0;">YASH RAI SHARMA</h1>', unsafe_allow_html=True)
    st.markdown('<p style="letter-spacing:8px; color:#bf953f; font-weight:bold;">TECHNOCRAT | SOFTWARE ENGINEER</p>', unsafe_allow_html=True)
    st.write(f"**+91 95501 16685 | yashraisharma01@gmail.com | github.com/yashraisharma**")
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # SUMMARY
    st.markdown('<div class="crevice-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">SUMMARY</div>', unsafe_allow_html=True)
    st.write("Technocrat, with bases in Software development, Quantum Computing, Augmented/Virtual Reality and Cyber Security.[cite: 1]")
    st.write("Aspiring to lead and learn, with experience in Project management, Human-Resource management, strategic partnerships and Innovation.[cite: 1]")
    st.write("Seeking opportunities to deliver impactful solutions, grasp and further technological advancements.[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

    # EDUCATION
    st.markdown('<div class="crevice-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">EDUCATION</div>', unsafe_allow_html=True)
    st.write("**SRM Institute of Science and Technology, Chennai, TN**[cite: 1]")
    st.write("B.Tech, Computer Science Engineering w/s Software Engineering | May 2024 | CGPA: 8.5[cite: 1]")
    st.write("Relevant coursework: AI, OOPS, Operating Systems, Data Structures and Algorithms, Design and Analysis of Algorithms, DBMS[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

    # WORK EXPERIENCE
    st.markdown('<div class="crevice-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">WORK EXPERIENCE</div>', unsafe_allow_html=True)
    
    st.write("**VechTech Consulting Private Limited, Hyderabad, TS: Director (Apr 2023)**[cite: 1]")
    st.write("Actively served as Director at \"VechTech Consulting Private Limited\", Hyderabad, TS, Since April 2023, contributed to the company's operations and working processes. My experience within my father's company, has equipped me with essential management and critical thinking skills. This involvement has allowed me to hone my skills in decision-making, furthering the company's direction and success. With my role as a partaker in the company endeavors, I've gained valuable insights into effective running of a company, enhancing my understanding of organizational dynamics and leadership principles.[cite: 1]")
    st.write("Having been an instrument to the ongoing technical projects at VechTech Consulting Private Limited, I have specifically been conducive in the development of speech recognition software and the implementation of business ERP solutions. In these roles, I've facilitated communication among team members, ensured project milestones were met, and provided input to enhance the overall progress and efficiency of these projects. Additionally, separate from these initiatives, I've managed a freelance team to complete over 6 web development projects. From work procurement to client dealings and team coordination, I've overseen the entire process, ensuring successful project delivery and client satisfaction. These experiences have provided me, a diverse skill set and strengthened my abilities to manage multifaceted projects effectively.[cite: 1]")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**HappiApps, Chennai, TN: Application Development Engineer Intern (Aug 2022-Jan 2023)**[cite: 1]")
    st.write("Learned and synchronized within a team environment, gained valuable practical software development experience across multiple projects. Specializing as a UI/UX and front-end engineer, I acquired essential insights into effective collaboration and project execution methodologies. Working alongside my peers, I honed my skills in communication, problem-solving, and adaptability, fostering a deep understanding of the nuances involved in successful team dynamics and project delivery..[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

    # OTHER EXPERIENCES & PROJECTS
    st.markdown('<div class="crevice-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">OTHER EXPERIENCES</div>', unsafe_allow_html=True)
    st.write("**Quantum Computing Lab SRM, Chennai, TN: Core-Quantum Lead**[cite: 1]")
    st.write("Engaged in quantum computing research and development LAB as Core Quantum Lead with a dynamic team of over 50 members, I actively contributed to driving innovative ideas and fostering strategic partnerships to enhance the potential of our college club.[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

    # AWARDS
    st.markdown('<div class="crevice-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">AWARDS AND RECOGNITION</div>', unsafe_allow_html=True)
    st.write("**Excellence award SRM (MAY 2024)**[cite: 1]")
    st.write("Recipient of the Excellence Award for Entrepreneurship, Management, and Startups from the School of Computing, SRM, This award underscores my commitment to fostering entrepreneurial spirit and effective management practices within the academic community and beyond.[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center; padding: 50px; border-top: 1px solid #333;">
        <p class="gold-header" style="font-size:20px;">Available for High-Impact Initiatives</p>
    </div>
""", unsafe_allow_html=True)
