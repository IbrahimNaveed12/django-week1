# django-week1: Personal Portfolio Website

This is my Week 1 project for the Django Remote Internship at Jamwah Studios (10 to 16 November 2026, instructor Jamshed Ali). It is a small portfolio website with four pages, built with Django.

## Pages

- **Home:** a short introduction and three featured projects
- **About:** my education, skills, certification and internship
- **Projects:** my repositories and projects
- **Contact:** email and links

## Built with

- Python 3.15.2
- Django 6.1.3
- HTML and CSS

## How to run it

1. Clone the repository and open the folder:
   ```
   git clone https://github.com/IbrahimNaveed12/django-week1.git
   cd django-week1
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate          (Windows)
   source venv/bin/activate       (Mac or Linux)
   ```
3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
4. Start the server:
   ```
   python manage.py runserver
   ```
5. Open http://127.0.0.1:8000/ in the browser.

## Folder structure

```
django-week1/
├── manage.py
├── requirements.txt
├── lab0-writeup.md
├── python-lab/          Lab 1: the Book class (library.py and main.py)
├── portfolio/           the Django project (settings and main urls)
└── pages/               the Django app
    ├── views.py         one view for each page
    ├── urls.py          the urls of the app
    ├── templates/       base.html and the four page templates
    └── static/          css and images
```

## How it works

When I open a page, the browser sends a request. `portfolio/urls.py` passes it to `pages/urls.py`, which finds the right function in `pages/views.py`. The view renders a template, and every template extends `base.html`, so the navbar and footer are written only once. The CSS file and the image are served as static files.

## What I learned this week

- How a request moves in Django: the URL finds the view, the view picks the data, and the template shows the page.
- The difference between a project (`portfolio`) and an app (`pages`), and why the app must be added to `INSTALLED_APPS`.
- How to use `base.html` with `{% extends %}` and `{% block %}` so the navbar and footer are written only once.
- How to use static files (CSS and images) with `{% load static %}` and `{% static %}`.
- How to use a virtual environment, `requirements.txt` and Git commits to keep my work organised and push it to GitHub.

## Note

I used an AI assistant as an helper while building this project so its self and ai both based. I reviewed the code and I can explain how it works.

## Author

Muhammad Ibrahim Naveed (Ibraheem), BS Software Engineering student at COMSATS Lahore.
GitHub: https://github.com/IbrahimNaveed12
