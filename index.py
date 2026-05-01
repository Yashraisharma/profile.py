<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yash Rai Sharma | Technocrat</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: linear-gradient(180deg, #fcf6ba 0%, #bf953f 50%, #8a6d3b 100%);
            --rock: #050505;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background-color: var(--rock);
            color: #d1d1d1;
            font-family: 'Montserrat', sans-serif;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at center, rgba(0,0,0,0) 0%, rgba(0,0,0,0.9) 100%),
                url('https://www.transparenttextures.com/patterns/dark-stone.png');
            background-attachment: fixed;
        }

        /* Entry Overlay */
        #entry-gate {
            position: fixed;
            inset: 0;
            background: #000;
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: opacity 1.2s ease-out;
        }

        .pulse-text {
            font-family: 'Cinzel', serif;
            color: #bf953f;
            letter-spacing: 10px;
            font-size: 1.2rem;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.4; text-shadow: 0 0 0px #bf953f; }
            50% { opacity: 1; text-shadow: 0 0 20px #fcf6ba; }
        }

        /* Hero Section */
        .hero {
            height: 80vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
        }

        .gold-title {
            font-family: 'Cinzel', serif;
            font-size: clamp(3.5rem, 15vw, 9rem);
            background: var(--gold);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 15px;
            margin: 0;
            filter: drop-shadow(0 10px 30px rgba(0,0,0,1));
        }

        .subtitle {
            font-family: 'Cinzel', serif;
            color: #c0a062;
            letter-spacing: 8px;
            font-size: 1.4rem;
            margin-top: 10px;
        }

        /* Cinematic Crevice Sections */
        .crevice {
            max-width: 900px;
            margin: 100px auto;
            padding: 80px;
            background: rgba(10, 10, 10, 0.95);
            border-left: 3px solid #bf953f;
            box-shadow: -30px 40px 80px rgba(0,0,0,0.9);
            position: relative;
            transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            perspective: 1500px;
        }

        .crevice:hover {
            transform: perspective(1500px) rotateY(-5deg) translateX(20px);
            border-left-color: #fcf6ba;
            background: rgba(15, 15, 15, 1);
        }

        .label {
            font-family: 'Cinzel', serif;
            color: #bf953f;
            letter-spacing: 5px;
            font-size: 1.3rem;
            margin-bottom: 35px;
            border-bottom: 1px solid rgba(191,149,63,0.3);
            display: inline-block;
            padding-bottom: 5px;
        }

        .resume-text {
            line-height: 2.1;
            text-align: justify;
            font-size: 1.15rem;
            color: #b8b8b8;
        }

        .highlight { color: #fcf6ba; font-weight: 600; }

        /* Flowing Gold Vein (CSS Animation) */
        .crevice::before {
            content: "";
            position: absolute;
            top: 0; left: -3px; width: 3px; height: 100%;
            background: linear-gradient(to bottom, transparent, #fcf6ba, transparent);
            background-size: 100% 200%;
            animation: flow 4s linear infinite;
        }

        @keyframes flow {
            0% { background-position: 0% 0%; }
            100% { background-position: 0% -200%; }
        }
    </style>
</head>
<body>

    <div id="entry-gate" onclick="unlock()">
        <div class="pulse-text">DESCEND INTO THE GOLDEN ABYSS</div>
    </div>

    <audio id="waves" loop preload="auto">
        <source src="https://www.soundjay.com/nature/ocean-wave-1.mp3" type="audio/mpeg">
    </audio>

    <div class="hero">
        <h1 class="gold-title">YASH RAI SHARMA</h1>
        <p class="subtitle">TECHNOCRAT | ENGINEER</p>
        <p style="margin-top: 30px; opacity: 0.6; font-size: 0.9rem; letter-spacing: 2px;">
            +91 95501 16685 | yashraisharma01@gmail.com
        </p>
    </div>

    <section class="crevice">
        <div class="label">SUMMARY</div>
        <div class="resume-text">
            Technocrat, with bases in <span class="highlight">Software development, Quantum Computing, Augmented/Virtual Reality and Cyber Security</span>. 
            Aspiring to lead and learn, with experience in Project management, Human-Resource management, strategic partnerships and Innovation[cite: 1]. 
            Seeking opportunities to deliver impactful solutions, grasp and further technological advancements[cite: 1].
        </div>
    </section>

    <section class="crevice">
        <div class="label">WORK EXPERIENCE</div>
        <div class="resume-text">
            <h3 style="color:#fcf6ba; font-family:Cinzel; margin-bottom:10px;">VechTech Consulting Private Limited | Director</h3>
            <p style="font-style:italic; opacity:0.7; margin-bottom:25px;">Hyderabad, TS | Apr 2023 - Present[cite: 1]</p>
            Actively served as Director at "VechTech Consulting Private Limited", Hyderabad, TS, Since April 2023, contributed to the company's operations and working processes[cite: 1]. 
            My experience within my father's company, has equipped me with essential management and critical thinking skills[cite: 1]. 
            This involvement has allowed me to hone my skills in decision-making, furthering the company's direction and success[cite: 1].
            <br><br>
            Having been an instrument to the ongoing technical projects at VechTech Consulting Private Limited, I have specifically been conducive in the development of speech recognition software and the implementation of business ERP solutions[cite: 1].
        </div>
    </section>

    <section class="crevice">
        <div class="label">RECOGNITION</div>
        <div class="resume-text">
            <span class="highlight">Excellence award SRM | MAY 2024</span>[cite: 1]<br><br>
            Recipient of the Excellence Award for Entrepreneurship, Management, and Startups from the School of Computing, SRM[cite: 1]. 
            This award underscores my commitment to fostering entrepreneurial spirit and effective management practices within the academic community and beyond[cite: 1].
        </div>
    </section>

    <script>
        function unlock() {
            const audio = document.getElementById('waves');
            audio.play();
            const gate = document.getElementById('entry-gate');
            gate.style.opacity = '0';
            setTimeout(() => gate.remove(), 1200);
        }
    </script>
</body>
</html>
