from flask import Flask, render_template_string, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Portfolio | Riko</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root {
    --accent: #00ffd5;
    --glass-bg: rgba(255,255,255,0.12);
    --glass-border: rgba(255,255,255,0.25);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: "Segoe UI", sans-serif;
    background: linear-gradient(120deg,#0f2027,#203a43,#2c5364);
    color: white;
    scroll-behavior: smooth;
}

/* SCROLL PROGRESS */
#progress {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    width: 0%;
    background: var(--accent);
    z-index: 2000;
}

/* NAVBAR */
nav {
    position: fixed;
    top: 0;
    width: 100%;
    padding: 14px 40px;
    backdrop-filter: blur(10px);
    background: rgba(0,0,0,0.35);
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
}

nav a {
    color: white;
    margin-left: 20px;
    text-decoration: none;
    font-size: 14px;
}

nav a:hover {
    color: var(--accent);
}

/* SECTION – DIPERAPAT */
section {
    padding: 50px 40px;
    margin-bottom: 10px;
    opacity: 0;
    transform: translateY(35px);
    transition: 0.7s ease;
}

section.show {
    opacity: 1;
    transform: translateY(0);
}

/* HERO – TIDAK TERLALU TINGGI */
.hero {
    display: flex;
    align-items: center;
    padding-top: 90px;     /* aman untuk navbar fixed */
    padding-bottom: 35px;
}

/* Trik agar About Me dekat dengan Hero */
.hero + section {
    margin-top: -10px;
}

/* GLASS CARD */
.glass {
    width: 100%;
    max-width: 880px;
    margin: 0 auto;
    background: var(--glass-bg);
    backdrop-filter: blur(16px);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 26px;
}
                                  
#skills .glass {
    min-height: 160px;
}

/* DIVIDER */
.divider {
    height: 1px;
    background: rgba(255,255,255,0.25);
    margin: 30px 0;
}

/* SKILLS */
.skills span {
    display: inline-block;
    margin: 6px;
    padding: 7px 15px;
    border-radius: 20px;
    background: rgba(255,255,255,0.18);
    font-size: 14px;
}

/* PROJECT CARD */
.project {
    margin-top: 16px;
    padding: 16px;
    border-radius: 14px;
    background: rgba(255,255,255,0.12);
    transition: 0.3s ease;
}

.project:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.2);
}

/* BUTTON */
button {
    padding: 9px 18px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-weight: bold;
}

.btn-cv {
    background: var(--accent);
    color: black;
    margin-top: 14px;
}

/* CTA */
.cta {
    text-align: center;
}

/* MOBILE */
@media (max-width: 768px) {
    nav {
        padding: 12px 20px;
    }

    section {
        padding: 45px 20px;
    }

    .glass {
        padding: 22px;
    }
}
</style>
</head>

<body>

<div id="progress"></div>

<nav>
    <b>Portfolio Riko Panggiano</b>
    <div>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#project">Project</a>
        <a href="#education">Education</a>
        <a href="#contact">Contact</a>
    </div>
</nav>

<section class="hero show">
    <div class="glass">
        <h1>Hi, I'm Riko</h1>
        <p id="typing"></p>
        <a href="/download-cv"><button class="btn-cv">Download CV</button></a>
    </div>
</section>

<section id="about">
    <div class="glass">
        <h2>About Me</h2>
        <p>
            Saya adalah seorang IT / Web Developer yang memiliki minat kuat
            dalam pengembangan aplikasi berbasis web, khususnya backend
            menggunakan Python Flask dan Laravel.
        </p>
        <p>
            Berpengalaman mengembangkan sistem manajemen UMKM, sistem cafe,
            serta website e-commerce dengan fokus pada performa dan kemudahan penggunaan.
        </p>
    </div>
</section>

<section id="skills">
    <div class="glass">
        <h2>Skills</h2>
        <div class="skills">
            <span>Python</span>
            <span>Flask</span>
            <span>Laravel</span>
            <span>HTML</span>
            <span>CSS</span>
            <span>JavaScript</span>
            <span>MySQL</span>
        </div>
    </div>
</section>

<section id="project">
    <div class="glass">
        <h2>Projects</h2>

        <div class="project">
            <h3>Management System UMKM</h3>
            <p>Sistem untuk mengelola produk, transaksi, dan laporan penjualan UMKM.</p>
            <p><b>Tech:</b> Python, Flask</p>
        </div>

        <div class="project">
            <h3>Management System Cafe</h3>
            <p>Aplikasi manajemen menu, pesanan, dan transaksi cafe.</p>
            <p><b>Tech:</b> Laravel, MySQL</p>
        </div>

        <div class="project">
            <h3>E-Commerce Website</h3>
            <p>Website e-commerce dengan fitur katalog, cart, dan pemesanan.</p>
            <p><b>Tech:</b> Python, Flask</p>
        </div>
    </div>
</section>

<section id="education">
    <div class="glass">
        <h2>Education</h2>

        <p>
            <b>Universitas Buddhi Dharma</b><br>
            S1 Informatika (2021 – 2025)
        </p>

        <p style="margin-top: 15px;">
            <b>SMA Dharma Putra</b><br>
            Ilmu Pengetahuan Umum (2019 – 2021)
        </p>

        <div class="divider"></div>

        <h2>Interests</h2>
        <ul>
            <li>Pengembangan project web berbasis sistem</li>
            <li>Mempelajari teknologi backend & framework baru</li>
            <li>Problem solving dan optimasi sistem</li>
        </ul>
    </div>
</section>

<section id="contact">
    <div class="glass">
        <h2>Contact</h2>
        <p>Email: rikopanggiano24@email.com</p>
        <p>GitHub: github.com/RikoPanggiano</p>

        <div class="divider"></div>

        <div class="cta">
            <h3>Tertarik bekerja sama?</h3>
            <p>Silakan hubungi saya untuk diskusi lebih lanjut.</p>
            <a href="mailto:rikopanggiano24@email.com">
                <button class="btn-cv">Contact Me</button>
            </a>
        </div>
    </div>
</section>

<script>
// Typing Effect
const text = "IT / Web Developer | Flask | Laravel";
let i = 0;
function typing() {
    if (i < text.length) {
        document.getElementById("typing").innerHTML += text.charAt(i);
        i++;
        setTimeout(typing, 60);
    }
}
typing();

// Scroll animation & progress bar
const sections = document.querySelectorAll("section");
window.addEventListener("scroll", () => {
    sections.forEach(sec => {
        const top = sec.getBoundingClientRect().top;
        if (top < window.innerHeight - 120) {
            sec.classList.add("show");
        }
    });

    const scroll = document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    document.getElementById("progress").style.width = (scroll / height * 100) + "%";
});
</script>

</body>
</html>
""")

@app.route("/download-cv")
def download_cv():
    return send_file("CV.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
