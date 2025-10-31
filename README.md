# 📝 SimpleBlog — A Developer’s Journey Journal

> A personal blogging platform built with **Django** to document my **real-time project learnings, achievements, and failures** while exploring new technologies.

---

## 🚀 About the Project

**SimpleBlog** is not just another blog website — it’s a **self-documentation platform** I created to record my **daily development journey**.  
Whenever I build new projects or face technical challenges, I log everything here — from success milestones to debugging struggles.  

This project also marks my **first hands-on experience with Django**, where I learned:
- Django models, views, and URL routing  
- Template rendering and static files management  
- Admin panel customization  
- Deployment with Render and PostgreSQL  

---

## 🎯 Purpose & Motivation

While learning full-stack development, I realized that developers often forget to document their process.  
So, I decided to build a place where:
- I could **record my learning journey** in real-time.  
- Reflect on **what went wrong** and **how I solved it**.  
- Improve my Django and backend deployment skills.

This project became both a **learning companion** and a **digital dev diary**. 🧠

---

## 🏗️ Tech Stack

- **Backend:** Django (Python Framework)  
- **Database:** PostgreSQL (via Render)  
- **Frontend:** HTML, CSS, Django Templates  
- **Deployment:** Render (Cloud Hosting)  
- **Version Control:** Git & GitHub  

---

## ⚙️ Key Features

✅ Create, Edit, and Delete blog posts  
✅ Responsive blog listing and detail pages  
✅ Django Admin panel for managing posts  
✅ PostgreSQL database integration  
✅ Deployed live on Render  

---

## 🔗 Live Demo

🌍 **Live Site:** [Visit SimpleBlog on Render](https://simpleblog-2.onrender.com/)  

---

## 🧩 Folder Structure

simpleblog/
│
├── blog/ # Core app handling posts
├── simpleblog/ # Project settings & configurations
├── static/ # CSS, JS, and static assets
├── templates/ # HTML templates
├── manage.py # Django management script
└── requirements.txt # Python dependencies


---

## 👨‍💻 Author

**Bimochan Jena**  
MCA Student | Aspiring Full Stack Developer  
🌐 [GitHub Profile](https://github.com/BimoJena)

---

## 💡 Future Plans

- Add user authentication (login/signup)  
- Integrate a markdown editor for posts  
- Add categories/tags and search feature  
- Enable image upload in posts  
- Create a personal portfolio section linked to blog

---

## 🧠 Lessons Learned

- Setting up Django project from scratch  
- Handling migrations and models  
- Configuring static/media files  
- Using environment variables securely  
- Deploying Django apps on Render  
- Debugging live database issues

---

## 🛠️ Installation Guide (for local setup)

If anyone wants to run this locally 👇

```bash
git clone https://github.com/BimoJena/simpleblog.git
cd simpleblog
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
