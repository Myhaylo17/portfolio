from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Myhaylo Koltun Portfolio")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Skill(BaseModel):
    name: str
    level: str
    experience: str

class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]

class ContactInfo(BaseModel):
    phone: str
    email: str
    github: str
    linkedin: str


PROFILE = {
    "name": "Myhaylo Koltun",
    "title": "Python Developer",
    "bio": "Computer Science student at National University 'Lviv Polytechnic' with strong passion for Python development and web technologies.",
    "location": "Lviv, Ukraine"
}

HARD_SKILLS = [
    {"name": "Python", "level": "Intermediate", "experience": "1+ year"},
    {"name": "Django", "level": "Beginner-Intermediate", "experience": "6 months"},
    {"name": "MySQL/SQL", "level": "Intermediate", "experience": "6 months"},
    {"name": "JavaScript", "level": "Beginner-Intermediate", "experience": "1 year"},
    {"name": "HTML/CSS", "level": "Intermediate", "experience": "1 year"},
    {"name": "FastAPI", "level": "Beginner", "experience": "Learning"},
    {"name": "OOP & Design Patterns", "level": "Intermediate", "experience": "1 year"},
    {"name": "Git/GitHub", "level": "Intermediate", "experience": "1+ year"}
]

SOFT_SKILLS = [
    "Effective Communication",
    "Hardworking & Responsible",
    "Quick Learning & Adaptability",
    "Strong Motivation",
    "Problem-Solving",
    "Team Collaboration"
]

PROJECTS = [
    {
        "title": "AutoGalaxy: Rental Cars Website",
        "description": "Full-stack Django application for car reservations with user authentication, profile management",
        "technologies": ["Django", "Python", "MySQL", "HTML", "CSS", "JavaScript"]
    },
    {
        "title": "Data Analysis Projects",
        "description": "Academic projects focusing on Big Data concepts including data preprocessing, analysis, and visualization",
        "technologies": ["Python", "Pandas", "NumPy", "Matplotlib", "Data Visualization"]
    },
    {
        "title": "API Integration Projects",
        "description": "Various projects implementing OOP principles, design patterns, file handling, and external API integration",
        "technologies": ["Python", "OOP", "REST APIs", "JSON/CSV"]
    },
    {
        "title": "Personal Portfolio",
        "description": "Modern portfolio website built with FastAPI backend and responsive frontend",
        "technologies": ["FastAPI", "Python", "HTML", "CSS", "JavaScript"]
    }
]

CONTACT = {
    "phone": "+380 98 250 45 76",
    "email": "myhaylo.koltun@gmail.com",
    "github": "https://github.com/Myhaylo17",
    "linkedin": "https://www.linkedin.com/in/михайло-колтун-049ba1362/"
}

EDUCATION = {
    "institution": "National University 'Lviv Polytechnic'",
    "specialization": "Computer Science",
    "period": "2023 - Present",
    "status": "Current Student"
}


@app.get("/api/profile")
async def get_profile():
    return PROFILE

@app.get("/api/skills/hard", response_model=List[Skill])
async def get_hard_skills():
    return HARD_SKILLS

@app.get("/api/skills/soft")
async def get_soft_skills():
    return {"skills": SOFT_SKILLS}

@app.get("/api/projects", response_model=List[Project])
async def get_projects():
    return PROJECTS

@app.get("/api/contact", response_model=ContactInfo)
async def get_contact():
    return CONTACT

@app.get("/api/education")
async def get_education():
    return EDUCATION

@app.get("/api/all")
async def get_all_data():
    return {
        "profile": PROFILE,
        "hard_skills": HARD_SKILLS,
        "soft_skills": SOFT_SKILLS,
        "projects": PROJECTS,
        "contact": CONTACT,
        "education": EDUCATION
    }

@app.get("/", response_class=HTMLResponse)
async def portfolio_page(request: Request):
    context = {"request": request, "profile": PROFILE}
    return templates.TemplateResponse("index.html", context)
