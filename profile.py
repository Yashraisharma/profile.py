import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Yash Rai Sharma | Technocrat", layout="wide")

# --- CINEMATIC CSS & JAVASCRIPT ---
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
        background: rgba(10, 10, 10, 0.7);
        border-left: 3px solid #b38728;
        padding: 45px;
        margin-bottom: 60px;
        border-radius: 0 40px 40px 0;
        box-shadow: -15px 0px 30px rgba(0,0,0,0.6);
        transition: transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
        perspective: 1500px;
    }

    .crevice-section:hover {
        transform: perspective(1500px) rotateY(-4deg) translateX(15px);
        background: rgba(179, 135, 40, 0.04);
        border-left: 3px solid #fcf6ba;
    }

    .section-label {
        font-family: 'Cinzel', serif;
        color: #bf953f;
        font-size: 1.4rem;
        letter-spacing: 4px;
        margin-bottom: 25px;
        font-weight: 700;
    }

    /* Verbatim Text Styling */
    p, li, div {
        font-family: 'Inter', sans-serif;
        line-height: 1.8;
        color: #d1d1d1;
        text-align: justify;
    }

    b, strong { color: #fcf6ba; font-weight: 600; }

    /* Invisible click-layer to trigger audio */
    #audio-trigger {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 99999;
        cursor: pointer;
        background: transparent;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>

    <!-- AUDIO ELEMENT -->
    <audio id="waves-audio" loop>
        <source src="https://www.soundjay.com/nature/ocean-wave-1.mp3" type="audio/mpeg">
    </audio>

    <!-- SCRIPT FOR INTERACTION-BASED AUDIO -->
    <script>
    const player = document.getElementById('waves-audio');
    const trigger = document.createElement('div');
    trigger.id = 'audio-trigger';
    document.body.appendChild(trigger);

    trigger.addEventListener('click', () => {
        player.play();
        trigger.remove(); // Remove layer so user can interact with content
    });
    </script>
    """, unsafe_allow_html=True)

# --- VERBATIM RESUME CONTENT ---
with st.container():
    # HERO SECTION
    st.markdown('<h1 class="gold-header" style="font-size: 80px; margin-bottom:0;">YASH RAI SHARMA</h1>', unsafe_allow_html=True)
    st.markdown('<p style="letter-spacing:10px; color:#bf953f; font-weight:bold; margin-top:-10px;">TECHNOCRAT | SOFTWARE ENGINEER</p>', unsafe_allow_html=True)
    st.write("+91 95501 16685 | yashraisharma01@gmail.com")
    st.write("github.com/yashraisharma | linkedin.com/in/yashraisharma[cite: 1]")
    
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
    st.write("<br>**Fiitjee Junior College, Saifabad**[cite: 1]", unsafe_allow_html=True)
    st.write("Intermediate(+1 & +2) | Jun 2020 | Percentage: 71%[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

    # TECHNICAL SKILLS
    st.markdown('<div class="crevice-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">TECHNICAL SKILLS</div>', unsafe_allow_html=True)
    st.write("**Programming:** Python3, C, C++, HTML CSS+, JavaScript, React JS, Offensive Security[cite: 1]")
    st.write("**Design and Modeling Tools:** AutoCAD, Figma, MATLAB, Microsoft Office, Blender, Unity3[cite: 1]")
    st.write("**Certifications:** Google-Data Analytics, Google-Foundations of Project Management, IBM Introduction to Cloud Computing, Erasmus University Rotterdam-Serious Gaming[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

    # WORK EXPERIENCE
    st.markdown('<div class="crevice-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">WORK EXPERIENCE</div>', unsafe_allow_html=True)
    
    st.write("**VechTech Consulting Private Limited, Hyderabad, TS: Director | Apr 2023**[cite: 1]")
    st.write("Actively served as Director at \"VechTech Consulting Private Limited\", Hyderabad, TS, Since April 2023, contributed to the company's operations and working processes. My experience within my father's company, has equipped me with essential management and critical thinking skills. This involvement has allowed me to hone my skills in decision-making, furthering the company's direction and success. With my role as a partaker in the company endeavors, I've gained valuable insights into effective running of a company, enhancing my understanding of organizational dynamics and leadership principles.[cite: 1]")
    st.write("Having been an instrument to the ongoing technical projects at VechTech Consulting Private Limited, I have specifically been conducive in the development of speech recognition software and the implementation of business ERP solutions. In these roles, I've facilitated communication among team members, ensured project milestones were met, and provided input to enhance the overall progress and efficiency of these projects. Additionally, separate from these initiatives, I've managed a freelance team to complete over 6 web development projects. From work procurement to client dealings and team coordination, I've overseen the entire process, ensuring successful project delivery and client satisfaction. These experiences have provided me, a diverse skill set and strengthened my abilities to manage multifaceted projects effectively.[cite: 1]")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**HappiApps, Chennai, TN: Application Development Engineer Intern | Aug 2022-Jan 2023**[cite: 1]")
    st.write("Learned and synchronized within a team environment, gained valuable practical software development experience across multiple projects. Specializing as a UI/UX and front-end engineer, I acquired essential insights into effective collaboration and project execution methodologies. Working alongside my peers, I honed my skills in communication, problem-solving, and adaptability, fostering a deep understanding of the nuances involved in successful team dynamics and project delivery..[cite: 1]")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("**Allvy Software Solutions: Cyber Security Intern | Feb 2024**[cite: 1]")
    st.write("Employed as a cybersecurity intern at Allvy Software Solutions, I had the opportunity to immerse myself in various facets of the field, driven by a passion for continuous learning and exploration. During my internship, I was actively involved in handling government tenders focused on establishing Security Operations Centers (SOCs) and Cyber Network Operations Centers (C-NOCs). This hands-on experience provided me with valuable insights into the intricacies of cybersecurity, allowing me to grasp not only the foundational principles but also the practical considerations involved in tender processes and the establishment of critical cybersecurity infrastructure. Working closely with experienced professionals, I gained an understanding of the technical and operational aspects of SOC and C-NOC setups.[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

    # RECOGNITION
    st.markdown('<div class="crevice-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">AWARDS AND RECOGNITION</div>', unsafe_allow_html=True)
    st.write("**Excellence award SRM | MAY 2024**[cite: 1]")
    st.write("Recipient of the Excellence Award for Entrepreneurship, Management, and Startups from the School of Computing, SRM, This award underscores my commitment to fostering entrepreneurial spirit and effective management practices within the academic community and beyond.[cite: 1]")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center; padding: 40px; opacity:0.6;">
        <p class="gold-header" style="font-size:18px; animation:none;">Yash Rai Sharma &copy; 2026</p>
    </div>
""", unsafe_allow_html=True)
