const { useState, useEffect } = React;

function Portfolio() {
    const [entered, setEntered] = useState(false);
    const [timeLeft, setTimeLeft] = useState({ d: 0, h: 0, m: 0, s: 0 });

    // Target: UPSC Syllabus Deadline / May 2026 Cycle
    const targetDate = new Date("May 20, 2026 00:00:00").getTime();

    useEffect(() => {
        const timer = setInterval(() => {
            const now = new Date().getTime();
            const distance = targetDate - now;

            setTimeLeft({
                d: Math.floor(distance / (1000 * 60 * 60 * 24)),
                h: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
                m: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
                s: Math.floor((distance % (1000 * 60)) / 1000)
            });
        }, 1000);
        return () => clearInterval(timer);
    }, []);

    const handleEntry = () => {
        setEntered(true);
        const audio = new Audio('[https://www.soundjay.com/nature/ocean-wave-1.mp3](https://www.soundjay.com/nature/ocean-wave-1.mp3)');
        audio.loop = true;
        audio.play();
    };

    return (
        <div>
            {!entered && (
                <div className="gate" onClick={handleEntry}>
                    <h2 style={{letterSpacing: '10px', animation: 'pulse 2s infinite'}}>INITIALIZE DESCEND</h2>
                </div>
            )}

            <div style={{ opacity: entered ? 1 : 0, transition: 'opacity 2s ease' }}>
                <section className="countdown-section">
                    <div className="timer-digits">
                        {timeLeft.d}:{timeLeft.h}:{timeLeft.m}:{timeLeft.s}
                    </div>
                    <div className="timer-label">DAYS : HOURS : MIN : SEC</div>
                    <h1 style={{marginTop: '50px', fontSize: '3rem'}}>YASH RAI SHARMA</h1>
                    <p style={{opacity: 0.5}}>UPSC CIVIL SERVICES 2026 ASPIRANT | TECHNOCRAT</p>
                </section>

                <section className="crevice">
                    <div className="label">SYSTEM SUMMARY</div>
                    <p>Technocrat, with bases in Software development, Quantum Computing, AR/VR and Cyber Security. Experience in Project management and strategic partnerships at VechTech Consulting. Seeking to further technological advancements.</p>
                </section>

                <section className="crevice">
                    <div className="label">ACTIVE DEPLOYMENT: VECHTECH</div>
                    <p><b>Director | Apr 2023 - Present</b></p>
                    <p>Facilitated development of speech recognition software and ERP solutions. Managed freelance teams for 6+ web development projects.</p>
                </section>

                <section className="crevice">
                    <div className="label">ACADEMIC LOG</div>
                    <p><b>SRM Institute of Science and Technology</b></p>
                    <p>B.Tech, CSE (Software Engineering) | May 2024 | CGPA: 8.5</p>
                </section>
            </div>
        </div>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Portfolio />);
