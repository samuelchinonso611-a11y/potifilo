from flask import Flask, render_template

app = Flask(__name__)

# ==========================================================
#  EDIT EVERYTHING BELOW — this is your entire site
# ==========================================================

PROFILE = {
    "name":      "Winter",
    "title":     "Python Developer & Problem Solver",
    "tagline":   "I design and build clean, reliable web applications that people actually enjoy using.",
    "location":  "Port Harcourt, Nigeria",
    "available": True,   # shows "Available for work" badge
    "email":     "samuelchinonso611@gmail.com",
    "github":    "https://github.com/yourusername",
    "linkedin":  "https://linkedin.com/in/yourusername",
    "twitter":   "https://twitter.com/yourusername",
    "resume":    "",     # optional: "resume.pdf" if you add one to static/
}

ABOUT = {
    "paragraphs": [
        "I'm a self-taught developer who fell in love with Python for its clarity and power. "
        "I build web apps end-to-end — from the database to the interface — with a strong bias "
        "toward simplicity and maintainability.",

        "When I'm not coding, you'll find me exploring open-source projects, writing notes on "
        "what I'm learning, or helping others get started with Flask.",
    ],
    "skills": [
        {"name": "Python",       "level": 90},
        {"name": "Flask",        "level": 88},
        {"name": "JavaScript",   "level": 80},
        {"name": "HTML & CSS",   "level": 85},
        {"name": "SQL / SQLite", "level": 75},
        {"name": "Git",          "level": 82},
    ],
    "currently_learning": ["FastAPI", "Docker", "TypeScript"],
}

STATS = [
    {"number": "10+",  "label": "Projects Built"},
    {"number": "3",    "label": "Years Coding"},
    {"number": "15+",  "label": "Happy Clients"},
    {"number": "∞",    "label": "Cups of Coffee"},
]

SERVICES = [
    {
        "icon":  "⌘",
        "title": "Web Applications",
        "body":  "Custom Flask and Python apps built from scratch — clean architecture, "
                 "reliable performance, and interfaces people actually enjoy using.",
    },
    {
        "icon":  "⚡",
        "title": "REST APIs",
        "body":  "Well-documented APIs with authentication, validation, and sensible error handling. "
                 "Designed for developers who will actually use them.",
    },
    {
        "icon":  "◐",
        "title": "Frontend Interfaces",
        "body":  "Responsive, accessible UIs in HTML, CSS, and JavaScript. "
                 "Simple, fast, and consistent across every screen size.",
    },
    {
        "icon":  "⟳",
        "title": "Automation & Scripts",
        "body":  "Python scripts that save hours of manual work — data processing, "
                 "file management, integrations, and scheduled jobs.",
    },
]

EXPERIENCE = [
    {
        "role":    "Freelance Python Developer",
        "company": "Self-employed",
        "period":  "2023 — Present",
        "summary": "Building custom web apps for small businesses and startups. "
                   "Specializing in Flask backends, REST APIs, and clean frontends.",
    },
    {
        "role":    "Junior Developer",
        "company": "Tech Company",
        "period":  "2022 — 2023",
        "summary": "Worked on internal tools, wrote Python scripts for data processing, "
                   "and maintained a legacy Flask application.",
    },
]

# ==========================================================
#  That's it. Everything below is the "engine".
# ==========================================================

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        about=ABOUT,
        stats=STATS,
        services=SERVICES,
        experience=EXPERIENCE,
        year=2025,
    )


if __name__ == "__main__":
    app.run(debug=True)