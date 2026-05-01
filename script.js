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
                        TECHNOCRAT | ENGINEER
                    </p>
                    <p style={{ marginTop: '20px', opacity: 0.6 }}>
                        +91 95501 16685 | yashraisharma01@gmail.com
                    </p>
                </header>

                <section className="crevice">
                    <div className="label">SUMMARY</div>
                    <div className="resume-text">
                        Technocrat, with bases in <span className="highlight">Software development, Quantum Computing, Augmented/Virtual Reality and Cyber Security</span>. 
                        Aspiring to lead and learn, with experience in Project management, Human-Resource management, strategic partnerships and Innovation. 
                        Seeking opportunities to deliver impactful solutions, grasp and further technological advancements[cite: 1].
                    </div>
                </section>

                <section className="crevice">
                    <div className="label">WORK EXPERIENCE</div>
                    <div className="resume-text">
                        <h3 style={{ color: '#fcf6ba', fontFamily: 'Cinzel', marginBottom: '10px' }}>
                            VechTech Consulting Private Limited | Director
                        </h3>
                        <p style={{ fontStyle: 'italic', opacity: 0.7, marginBottom: '25px' }}>
                            Hyderabad, TS | Apr 2023 - Present[cite: 1]
                        </p>
                        Actively served as Director at "VechTech Consulting Private Limited", Hyderabad, TS, Since April 2023, contributed to the company's operations and working processes[cite: 1]. 
                        My experience within my father's company, has equipped me with essential management and critical thinking skills[cite: 1]. 
                        This involvement has allowed me to hone my skills in decision-making, furthering the company's direction and success[cite: 1]. 
                        With my role as a partaker in the company endeavors, I've gained valuable insights into effective running of a company, enhancing my understanding of organizational dynamics and leadership principles[cite: 1].
                        <br/><br/>
                        Having been an instrument to the ongoing technical projects at VechTech Consulting Private Limited, I have specifically been conducive in the development of speech recognition software and the implementation of business ERP solutions[cite: 1].
                    </div>
                </section>

                <section className="crevice">
                    <div className="label">RECOGNITION</div>
                    <div className="resume-text">
                        <span className="highlight" style={{ fontSize: '1.3rem' }}>Excellence award SRM | MAY 2024</span>[cite: 1]<br/><br/>
                        Recipient of the Excellence Award for Entrepreneurship, Management, and Startups from the School of Computing, SRM[cite: 1]. 
                        This award underscores my commitment to fostering entrepreneurial spirit and effective management practices within the academic community and beyond[cite: 1].
                    </div>
                </section>
            </div>
        </div>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Portfolio />);
