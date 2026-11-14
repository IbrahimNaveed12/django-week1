# Django Week 1 Portfolio

A personal portfolio website built with Django for Week 1 of the Jamwah Studios Django Internship.

## Pages
- **Home (`/`)**: Brief introduction, profile image, and featured projects.
- **About (`/about/`)**: Bio, education background, technical skills, certification, and internship details.
- **Projects (`/projects/`)**: Complete list of projects (coursework, practice, and GenAI-assisted).
- **Contact (`/contact/`)**: Personal contact email and social profile links.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/IbrahimNaveed12/django-week1.git
   cd django-week1
   ```

2. Create and activate a virtual environment:
   - **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

## Folder Structure

```
django-week1/
├── manage.py            # Django command-line utility
├── requirements.txt     # Python package dependencies
├── lab0-writeup.md      # Lab 0 short write-up
├── python-lab/          # OOP Book class exercise
├── portfolio/           # Project settings and root URL configuration
└── pages/               # Main portfolio app (views, URLs, templates, static CSS/images)
```

## What I Learned This Week

<!-- TODO: The student writes 4 or 5 bullets in their own words -->
- [TODO] Setting up a virtual environment and installing Django
- [TODO] Understanding Django projects versus apps
- [TODO] Routing URLs to views and rendering HTML templates
- [TODO] Template inheritance with base.html and serving static files

*Note: I used an AI assistant while building this and I reviewed and understood the code.*
