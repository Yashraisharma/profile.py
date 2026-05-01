import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Yash Rai Sharma | Technocrat", layout="wide")

# --- ADVANCED CINEMATIC ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&display=swap');

    /* Global Reset & Stone Background */
    .stApp {
        background: #050505;
        color: #d4d4d4;
    }

    /* The "Crevice" Background Effect */
    body {
        background-image: 
            linear-gradient(to right, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.2) 50%, rgba(0,0,0,0.9) 100%),
            url('https://www.transparenttextures.com/patterns/asfalt-dark.png');
        background-attachment: fixed;
    }

    /* Flowing Gold Vein Animation */
    @keyframes veinFlow {
        0% { filter: drop-shadow(0 0 5px #bf953f) brightness(1); }
        50% { filter: drop-shadow(0 0 20px #fcf6ba) brightness(1.5); }
        100% { filter: drop-shadow(0 0 5px #bf953f) brightness(1); }
    }

    /* Professional Title Branding */
    .hero-name {
        font-family: 'Cinzel', serif;
        font-size: clamp(40px, 8vw, 90px);
        font-weight: 900;
        text-align: center;
        background: linear-gradient(180deg, #fcf6ba 0%, #bf953f 50%, #8a6d3b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 12px;
        margin-bottom: 0px;
        filter: drop-shadow(0 5px 15px rgba(0,0,0,0.8));
    }

    /* Verbatim Section Containers (The "Rock Crevice") */
    .stone-block {
        background: rgba(15, 15, 15, 0.8);
        border: 1px solid rgba(191, 149, 63, 0.2);
        padding: 60px;
        margin: 80px auto;
        max-width: 900px;
        border-radius: 4px;
        position: relative;
        box-shadow: 0 30px 60px rgba(0,0,0,0.7);
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* The "Liquid Gold" vein flowing beside the section */
    .stone-block::before {
        content: "";
        position: absolute;
        top: 0; left: -10px; width: 4px; height: 100%;
        background: linear-gradient(to bottom, #bf953f, #fcf6ba, #bf953f);
        animation: veinFlow 3s infinite ease-in-out;
    }

    .stone-block:hover {
        transform: scale(1.02) translateY(-10px);
        border-color: rgba(252, 246, 186, 0.5);
        background: rgba(20, 20, 20, 0.9);
    }

    .section-title {
        font-family: 'Cinzel', serif;
        color: #c0a062;
        font-size: 1.2rem;
        letter-spacing: 5px;
        margin-bottom: 30px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(191, 149, 63, 0.3);
        display: inline-block;
        padding-bottom: 5px;
    }

    /* Resume Typography */
    .resume-text {
        font-family: 'Montserrat', sans-serif;
        line-height: 1.9;
        font-size: 1.05rem;
        color: #b0b0b0;
        text-align: justify;
    }

    .highlight { color: #fcf6ba; font-weight: 600; }

    /* Audio Trigger UI */
    #audio-overlay {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 10000;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(0,0,0,0.9);
        cursor: pointer;
        transition: opacity 1s ease;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>

    <div id="audio-overlay" onclick="startExperience()">
        <div style="text-align:center;">
            <p style="font-family:'Cinzel'; color:#bf953f; letter-spacing:5px;">CLICK TO ENTER THE ABYSS</p>
            <div style="width:50px; height:2px; background:#bf953f; margin: 20px auto; animation: veinFlow 2s infinite;"></div>
        </div>
    </div>

    <audio id="ambient-waves" loop>
        <source src="https://www.soundjay.com/nature/ocean-wave-1.mp3" type="audio/mpeg">
    </audio>

    <script>
    function startExperience() {
        const audio = document.getElementById('ambient-waves');
        audio.volume = 0.4;
        audio.play();
        document.getElementById('audio-overlay').style.opacity = '0';
        setTimeout(() => {
            document.getElementById('audio-overlay').style.display = 'none';
        }, 1000);
    }
    </script>
    """, unsafe_allow_html=True)

# --- VERBATIM CONTENT ---
st.markdown('<h1 class="hero-name">YASH RAI SHARMA</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; letter-spacing:10px; color:#c0a062; font-family:Cinzel; margin-top:-20px;">TECHNOCRAT | ENGINEER</p>', unsafe_allow_html=True)

# Contact Info
st.markdown(f"""
<div style="text-align:center; font-family:Montserrat; font-size:0.9rem; opacity:0.7; margin-bottom:100px;">
    +91 95501 16685 &nbsp; | &nbsp; yashraisharma01@gmail.com &nbsp; | &nbsp; github.com/yashraisharma
</div>
""", unsafe_allow_html=True)

# Summary
st.markdown(f"""
<div class="stone-block">
    <div class="section-title">Summary</div>
    <div class="resume-text">
        Technocrat, with bases in <span class="highlight">Software development, Quantum Computing, Augmented/Virtual Reality and Cyber Security</span>. 
        Aspiring to lead and learn, with experience in Project management, Human-Resource management, strategic partnerships and Innovation. 
        Seeking opportunities to deliver impactful solutions, grasp and further technological advancements[cite: 1].
    </div>
</div>
""", unsafe_allow_html=True)

# Experience: VechTech
st.markdown(f"""
<div class="stone-block">
    <div class="section-title">Work Experience</div>
    <div class="resume-text">
        <p><b>VechTech Consulting Private Limited, Hyderabad, TS: Director | Apr 2023</b>[cite: 1]</p>
        Actively served as Director at "VechTech Consulting Private Limited", Hyderabad, TS, Since April 2023, contributed to the company's operations and working processes[cite: 1]. 
        My experience within my father's company, has equipped me with essential management and critical thinking skills[cite: 1]. 
        This involvement has allowed me to hone my skills in decision-making, furthering the company's direction and success[cite: 1].
        <br><br>
        Having been an instrument to the ongoing technical projects at VechTech Consulting Private Limited, I have specifically been conducive in the 
        development of speech recognition software and the implementation of business ERP solutions[cite: 1].
    </div>
</div>
""", unsafe_allow_html=True)

# Awards
st.markdown(f"""
<div class="stone-block">
    <div class="section-title">Recognition</div>
    <div class="resume-text">
        <b>Excellence award SRM | MAY 2024</b>[cite: 1]<br>
        Recipient of the Excellence Award for Entrepreneurship, Management, and Startups from the School of Computing, SRM[cite: 1]. 
        This award underscores my commitment to fostering entrepreneurial spirit and effective management practices within the academic community and beyond[cite: 1].
    </div>
</div>
""", unsafe_allow_html=True)
