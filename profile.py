import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Yash Rai Sharma | Profile", layout="wide")

# --- KVS CORPORATE UI/UX STYLING ---
st.markdown("""
    <style>
    :root {
        --kvs-navy: #1a365d;
        --kvs-gold: #c0a062;
    }
    .stApp { background-color: #ffffff; }
    .top-nav {
        background-color: var(--kvs-navy);
        padding: 10px 60px;
        color: white;
        display: flex;
        justify-content: space-between;
        border-bottom: 5px solid var(--kvs-gold);
        font-size: 0.9rem;
    }
    .resume-header {
        padding: 40px 10%;
        border-bottom: 1px solid #eeeeee;
    }
    .name-title {
        font-size: 44px;
        font-weight: 800;
        color: var(--kvs-navy);
        margin: 0;
    }
    .section-head {
        color: var(--kvs-navy);
        border-bottom: 2px solid var(--kvs-gold);
        padding-bottom: 5px;
        margin-top: 40px;
        margin-bottom: 20px;
        text-transform: uppercase;
        font-weight: 700;
        font-size: 1.4rem;
    }
    .job-title { font-weight: 700; color: #333; font-size: 1.1rem; }
    .date-loc { color: #666; font-style: italic; font-size: 0.95rem; }
    p, li { color: #333; line-height: 1.6; text-align: justify; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- TOP CONTACT BAR ---
st.markdown("""
    <div class="top-nav">
        <div>+91 95501 16685 | yashraisharma01@gmail.com</div>
        <div>github.com/yashraisharma | linkedin.com/in/yashraisharma</div>
    </div>
    """, unsafe_allow_html=True)

# --- RESUME CONTENT ---
with st.container():
    st.markdown('<div class="resume-header"><div class="name-title">YASH RAI SHARMA</div></div>', unsafe_allow_html=True)

    # SUMMARY
    st.markdown('<div class="section-head">SUMMARY</div>', unsafe_allow_html=True)
    st.write("Technocrat, with bases in Software development, Quantum Computing, Augmented/Virtual Reality and Cyber Security.")
    st.write("Aspiring to lead and learn, with experience in Project management, Human-Resource management, strategic partnerships and Innovation.")
    st.write("Seeking opportunities to deliver impactful solutions, grasp and further technological advancements.")

    # EDUCATION
    st.markdown('<div class="section-head">EDUCATION</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("**SRM Institute of Science and Technology, Chennai, TN**")
        st.write("B.Tech, Computer Science Engineering w/s Software Engineering")
        st.write("Relevant coursework: AI, OOPS, Operating Systems, Data Structures and Algorithms, Design and Analysis of Algorithms, DBMS")
    with col2:
        st.write("May 2024")
        st.write("CGPA: 8.5")
    
    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4 = st.columns([3, 1])
    with col3:
        st.markdown("**Fiitjee Junior College, Saifabad**")
        st.write("Intermediate(+1 & +2)")
    with col4:
        st.write("Jun 2020")
        st.write("Percentage: 71%")

    # TECHNICAL SKILLS
    st.markdown('<div class="section-head">TECHNICAL SKILLS</div>', unsafe_allow_html=True)
    st.write("**Programming:** Python3, C, C++, HTML CSS+, JavaScript, React JS, Offensive Security")
    st.write("**Design and Modeling Tools:** AutoCAD, Figma, MATLAB, Microsoft Office, Blender, Unity3")
    st.write("**Certifications:** Google-Data Analytics, Google-Foundations of Project Management, IBM Introduction to Cloud Computing, Erasmus University Rotterdam-Serious Gaming")

    # WORK EXPERIENCE
    st.markdown('<div class="section-head">WORK EXPERIENCE</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="job-title">VechTech Consulting Private Limited, Hyderabad, TS: Director</div>', unsafe_allow_html=True)
    st.markdown('<div class="date-loc">Apr 2023</div>', unsafe_allow_html=True)
    st.write("Actively served as Director at \"VechTech Consulting Private Limited\", Hyderabad, TS, Since April 2023, contributed to the company's operations and working processes. My experience within my father's company, has equipped me with essential management and critical thinking skills. This involvement has allowed me to hone my skills in decision-making, furthering the company's direction and success. With my role as a partaker in the company endeavors, I've gained valuable insights into effective running of a company, enhancing my understanding of organizational dynamics and leadership principles.")
    st.write("Having been an instrument to the ongoing technical projects at VechTech Consulting Private Limited, I have specifically been conducive in the development of speech recognition software and the implementation of business ERP solutions. In these roles, I've facilitated communication among team members, ensured project milestones were met, and provided input to enhance the overall progress and efficiency of these projects. Additionally, separate from these initiatives, I've managed a freelance team to complete over 6 web development projects. From work procurement to client dealings and team coordination, I've overseen the entire process, ensuring successful project delivery and client satisfaction. These experiences have provided me, a diverse skill set and strengthened my abilities to manage multifaceted projects effectively.")

    st.markdown('<br><div class="job-title">HappiApps, Chennai, TN: Application Development Engineer Intern</div>', unsafe_allow_html=True)
    st.markdown('<div class="date-loc">Aug 2022 - Jan 2023</div>', unsafe_allow_html=True)
    st.write("Learned and synchronized within a team environment, gained valuable practical software development experience across multiple projects. Specializing as a UI/UX and front-end engineer, I acquired essential insights into effective collaboration and project execution methodologies. Working alongside my peers, I honed my skills in communication, problem-solving, and adaptability, fostering a deep understanding of the nuances involved in successful team dynamics and project delivery..")

    st.markdown('<br><div class="job-title">Allvy Software Solutions: Cyber Security Intern</div>', unsafe_allow_html=True)
    st.markdown('<div class="date-loc">Feb 2024</div>', unsafe_allow_html=True)
    st.write("Employed as a cybersecurity intern at Allvy Software Solutions, I had the opportunity to immerse myself in various facets of the field, driven by a passion for continuous learning and exploration. During my internship, I was actively involved in handling government tenders focused on establishing Security Operations Centers (SOCs) and Cyber Network Operations Centers (C-NOCs). This hands-on experience provided me with valuable insights into the intricacies of cybersecurity, allowing me to grasp not only the foundational principles but also the practical considerations involved in tender processes and the establishment of critical cybersecurity infrastructure. Working closely with experienced professionals, I gained an understanding of the technical and operational aspects of SOC and C-NOC setups.")

    # OTHER EXPERIENCES
    st.markdown('<div class="section-head">OTHER EXPERIENCES</div>', unsafe_allow_html=True)
    st.write("**Quantum Computing Lab SRM, Chennai, TN: Core-Quantum Lead** (Mar 2023 - Oct 2023)")
    st.write("Engaged in quantum computing research and development LAB as Core Quantum Lead with a dynamic team of over 50 members, I actively contributed to driving innovative ideas and fostering strategic partnerships to enhance the potential of our college club. Through collaborative efforts, we sought to secure sponsorships for events and procure professors to enrich the learning experiences of club members. This immersive experience provided me with a deep understanding of quantum computing principles and methodologies, while also honing my skills in teamwork, leadership, and relationship building. Working alongside a diverse group of individuals, I gained practical insights into research, development, and community engagement, further igniting my passion for exploring cutting-edge technologies and driving impactful initiatives.")

    # PROJECTS
    st.markdown('<div class="section-head">PROJECTS COMPLETED</div>', unsafe_allow_html=True)
    st.markdown("**Heart Attack Prediction**")
    st.write("- **Objective:** The probability of the heart attack occurring or not occurring can be predicted before-hand using A.l, this in turn gives doctors indicators to take precaution or make the patience go through necessary treatments to prevent it from happening. The A.I can effectively predict this for multiple patients without taking much time, with only the expense of entering and feeding the program data.")
    st.write("- **Solution:** The project uses the Cleveland dataset to learn, analyze and predict the probability of a heart attack through various Models of machine learning. Different Models are compared with each other in order to find out a Model which gives the best prediction accuracy for said dataset.")

    st.markdown("<br>**Pneumonia Detection System**")
    st.write("- **Objective:** To detect pneumonia using Al via developing an accurate and reliable algorithm that can effectively analyze medical images and accurately identify cases of pneumonia. This algorithm must be able to distinguish between several types of pneumonia, such as bacterial and viral pneumonia, and accurately diagnose the condition in patients with varying degrees of severity.")
    st.write("- **Solution:** The approach involves collecting and preparing a large dataset of chest X-ray images, developing a deep learning model to detect pneumonia in the images, integrating the model into pneumonia detection software, and evaluating the software's effectiveness in assisting medical professionals in diagnosing the disease.")

    # AWARDS
    st.markdown('<div class="section-head">AWARDS AND RECOGNITION</div>', unsafe_allow_html=True)
    st.write("**Excellence award SRM (MAY 2024):** Recipient of the Excellence Award for Entrepreneurship, Management, and Startups from the School of Computing, SRM. This award underscores my commitment to fostering entrepreneurial spirit and effective management practices within the academic community and beyond.")
