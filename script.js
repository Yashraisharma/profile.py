const { useState } = React;

function Portfolio() {
    const [entered, setEntered] = useState(false);

    const handleEntry = () => {
        setEntered(true);
        const audio = new Audio('https://www.soundjay.com/nature/ocean-wave-1.mp3');
        audio.loop = true;
        audio.play();
    };

    return (
        <div>
            <div className="abyss-bg"></div>
            
            {!entered && (
                <div className="entry-gate" onClick={handleEntry}>
                    <div className="pulse-gold">DESCEND INTO THE GOLDEN ABYSS</div>
                </div>
            )}

            <div style={{ opacity: entered ? 1 : 0, transition: 'opacity 2s ease' }}>
                <header className="hero">
                    <h1 className="gold-title">YASH RAI SHARMA</h1>
                    <p style={{ fontFamily: 'Cinzel', color: '#c0a062', letterSpacing: '8px', fontSize: '1.5rem' }}>
                        TECHNOCRAT | COMPUTER SCIENCE ENGINEER
                    </p>
                    <p style={{ marginTop: '20px', opacity: 0.6 }}>
                        +91 95501 16685 | yashraisharma01@gmail.com | Hyderabad, TS
                    </p>
                </header>

                {/* --- SUMMARY SECTION --- */}
                <section className="crevice">
                    <div className="label">SUMMARY</div>
                    <div className="resume-text">
                        Technocrat, with bases in <span className="highlight">Software development, Quantum Computing, Augmented/Virtual Reality and Cyber Security</span>. 
                        Aspiring to lead and learn, with experience in Project management, Human-Resource management, strategic partnerships and Innovation. 
                        Seeking opportunities to deliver impactful solutions, grasp and further technological advancements.
                    </div>
                </section>

                {/* --- EDUCATION SECTION --- */}
                <section className="crevice">
                    <div className="label">EDUCATION</div>
                    <div className="resume-text">
                        <h3 className="highlight">SRM Institute of Science and Technology, Chennai, TN</h3>
                        <p>B.Tech, Computer Science Engineering w/s Software Engineering | May 2024 | CGPA: 8.5</p>
                        <p style={{marginTop: '10px', fontSize: '0.95rem'}}>
                            <b>Relevant coursework:</b> AI, OOPS, Operating Systems, Data Structures and Algorithms, Design and Analysis of Algorithms, DBMS
                        </p>
                        <br/>
                        <h3 className="highlight">Fiitjee Junior College, Saifabad</h3>
                        <p>Intermediate (+1 & +2) | Jun 2020 | Percentage: 71%</p>
                    </div>
                </section>

                {/* --- TECHNICAL SKILLS --- */}
                <section className="crevice">
                    <div className="label">TECHNICAL SKILLS</div>
                    <div className="resume-text">
                        <p><b>Programming:</b> Python3, C, C++, HTML CSS+, JavaScript, React JS, Offensive Security</p>
                        <p><b>Design and Modeling:</b> AutoCAD, Figma, MATLAB, Microsoft Office, Blender, Unity3</p>
                        <p><b>Certifications:</b> Google-Data Analytics, Google-Foundations of Project Management, IBM Introduction to Cloud Computing, Erasmus University Rotterdam-Serious Gaming</p>
                    </div>
                </section>

                {/* --- WORK EXPERIENCE --- */}
                <section className="crevice">
                    <div className="label">WORK EXPERIENCE</div>
                    <div className="resume-text">
                        <h3 className="highlight">VechTech Consulting Private Limited, Hyderabad, TS: Director</h3>
                        <p style={{ fontStyle: 'italic', opacity: 0.7, marginBottom: '15px' }}>Apr 2023 - Present</p>
                        <p>
                            Actively served as Director at "VechTech Consulting Private Limited", Hyderabad, TS, Since April 2023, contributed to the company's operations and working processes. 
                            My experience within my father's company, has equipped me with essential management and critical thinking skills. 
                            This involvement has allowed me to hone my skills in decision-making, furthering the company's direction and success. 
                            With my role as a partaker in the company endeavors, I've gained valuable insights into effective running of a company, enhancing my understanding of organizational dynamics and leadership principles.
                        </p>
                        <br/>
                        <p>
                            Having been an instrument to the ongoing technical projects at VechTech Consulting Private Limited, I have specifically been conducive in the development of speech recognition software and the implementation of business ERP solutions. 
                            In these roles, I've facilitated communication among team members, ensured project milestones were met, and provided input to enhance the overall progress and efficiency of these projects. 
                            Additionally, separate from these initiatives, I've managed a freelance team to complete over 6 web development projects. 
                            From work procurement to client dealings and team coordination, I've overseen the entire process, ensuring successful project delivery and client satisfaction.
                        </p>

                        <br/><br/>

                        <h3 className="highlight">Allvy Software Solutions: Cyber Security Intern</h3>
                        <p style={{ fontStyle: 'italic', opacity: 0.7, marginBottom: '15px' }}>Feb 2024</p>
                        <p>
                            Employed as a cybersecurity intern at Allvy Software Solutions, I had the opportunity to immerse myself in various facets of the field, driven by a passion for continuous learning and exploration. 
                            During my internship, I was actively involved in handling government tenders focused on establishing Security Operations Centers (SOCs) and Cyber Network Operations Centers (C-NOCs). 
                            This hands-on experience provided me with valuable insights into the intricacies of cybersecurity, allowing me to grasp not only the foundational principles but also the practical considerations involved in tender processes and the establishment of critical cybersecurity infrastructure.
                        </p>

                        <br/><br/>

                        <h3 className="highlight">HappiApps, Chennai, TN: Application Development Engineer Intern</h3>
                        <p style={{ fontStyle: 'italic', opacity: 0.7, marginBottom: '15px' }}>Aug 2022 - Jan 2023</p>
                        <p>
                            Learned and synchronized within a team environment, gained valuable practical software development experience across multiple projects. 
                            Specializing as a UI/UX and front-end engineer, I acquired essential insights into effective collaboration and project execution methodologies. 
                            Working alongside my peers, I honed my skills in communication, problem-solving, and adaptability.
                        </p>
                    </div>
                </section>

                {/* --- LEADERSHIP & AWARDS --- */}
                <section className="crevice">
                    <div className="label">LEADERSHIP & AWARDS</div>
                    <div className="resume-text">
                        <p><b>Quantum Computing Lab SRM, Chennai, TN: Core-Quantum Lead</b></p>
                        <p>Engaged in quantum computing research and development LAB as Core Quantum Lead with a dynamic team of over 50 members, I actively contributed to driving innovative ideas and fostering strategic partnerships to enhance the potential of our college club.</p>
                        
                        <br/>

                        <h3 className="highlight">Excellence award SRM | MAY 2024</h3>
                        <p>
                            Recipient of the Excellence Award for Entrepreneurship, Management, and Startups from the School of Computing, SRM. 
                            This award underscores my commitment to fostering entrepreneurial spirit and effective management practices within the academic community and beyond.
                        </p>
                    </div>
                </section>
            </div>
        </div>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Portfolio />);
