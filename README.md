# 🚀 Company Career Portal

Welcome to the **Company Career Portal**, a web-based job application platform where job seekers can browse job openings and apply seamlessly. Recruiters can manage applications efficiently through an intuitive admin dashboard.

---

## 📌 Features

✅ **Job Listings** – Browse the available job positions.
✅ **Apply Online** – Submit applications with resume upload.
✅ **Admin Dashboard** – Manage job postings & applications.
✅ **User-friendly UI** – Responsive & clean Bootstrap-based design.

---

## 🛠 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/company-career-portal.git
cd company-career-portal
```

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** to access the job portal.

---

## 📁 Project Structure
```
company-career-page/        # Root project folder
│── jobs/                   # Main application
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files (CSS, JS, images)
│   │   ├── css/            # Custom stylesheets
│   │   ├── js/             # Custom JavaScript files
│   │   ├── images/         # Company logo and other images
│   ├── templates/          # HTML Templates
│   │   ├── base.html       # Base template (includes navbar, footer, etc.)
│   │   ├── job_list.html   # List of job openings
│   │   ├── job_detail.html # Job details with apply button
│   │   ├── apply_success.html # Application success page
│   ├── __init__.py         
│   ├── admin.py            # Django Admin configurations
│   ├── apps.py             # App configuration
│   ├── forms.py            # Django forms (JobApplicationForm, etc.)
│   ├── models.py           # Database models (Job, JobApplication)
│   ├── tests.py            # Test cases
│   ├── urls.py             # URL routing
│   ├── views.py            # Views (Job list, job details, apply job)
│
│── media/                  # Uploaded resumes and files (ensure it's in .gitignore)
│── static/                 # Global static files
│── templates/              # Global templates (if needed)
│── company_career/         # Main Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│
│── venv/                   # Virtual environment (should be in .gitignore)
│── db.sqlite3              # SQLite database (or use PostgreSQL/MySQL)
│── manage.py               # Django command-line tool
│── requirements.txt        # Dependencies (Django, ASGIRef, etc.)
│── .gitignore              # Ignore unnecessary files like venv, __pycache__, media, etc.
│── README.md               # Project documentation

```

---

## 🔐 Admin Panel
Access the admin panel at:
**http://127.0.0.1:8000/admin/**

### 📜 Default Admin Credentials:
- **Username:** (your created superuser)
- **Password:** (your set password)

---

## 📢 Contributing
Want to contribute? Feel free to create pull requests! 🚀


Happy Coding! 😊✨

