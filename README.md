# 📘 Study Guide System

A **personal productivity and learning web application** built with **Django**.  
The 'Study Guide System' is a Django-based web application designed to assist students in managing their studies efficiently through a suite of productivity tools. It provides a backend-only API-driven platform for authenticated users to organize notes, tasks, unit conversions, and search YouTube videos without leaving the system. The project prioritizes modularity, security, and beginner-friendly implementation, making it extensible for future frontend integration.
---

## 🚀 Key Features

- 📝 **Notepad:** CRUD operations for user-specific notes (title, content, archive status).  
- ✅ **To-Do List:** Manage study tasks and deadlines with progress tracking.  
- 📚 **Unit Converter:** Convert length (yard ↔ foot) and mass (pound ↔ kilogram), with history tracking.  
- 🎥 **YouTube Search:** Search YouTube videos (title, video ID, channel, thumbnail, URL) using youtube-search-python library, with history tracking.  
- 🔐 **Users App:** User authentication (register, login, logout, profile) using Django REST Framework (DRF) TokenAuthentication.  
---

## 🧩 Project Structure

| App | Description |
|------|--------------|
| `users` | Handles registration, login, and profile management |
| `notes` | Notepad for creating and managing study notes |
| `To do list` | To-do list for managing tasks and goals |
| `unit converter` | Convert units from one to other |
| `YouTube Search` | YouTube API integration for study content |

---

## 🗄️ Database Overview

| Model | Key Fields |
|--------|-------------|
| **CustomUser** | username, email, first_name, last_name |
| **Note** | user, title, content, is_archived, created_at, updated_at |
| **ToDo** | user, title, description, is_completed, created_at, updated_at |
| **Conversion** | user, value, from_unit, to_unit, result, created_at |
| **YouTubeSearchHistory** | user, query, created_at |


---


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kbz-21/Study_Guide_System.git
cd Study_Guide_System

2️⃣ Create and Activate Virtual Environment

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


3️⃣ Install Dependencies
- pip install -r requirements.txt

4️⃣ Apply Migrations
- python manage.py migrate

5️⃣ Run the Development Server
- python manage.py runserver

6️⃣ Access the App

Open your browser and go to:
http://127.0.0.1:8000/


🛠️ Technologies Used

# Backend: Django (Python)
# Framework: Django, Django REST Framework for APIs.
# Authentication: DRF TokenAuthentication, ensuring user-specific data access.
# Libraries:
  - youtube-search-python for YouTube video search (scraping-based, no API key).
  - django.contrib.auth for user management.
# Tools: Postman for API testing, Django Admin for data inspection.
# Environment: Python 3.x, virtual environment, requirements.txt for dependencies.
# Database: SQLite

📧 API Used:

# Internal APIs: All apps expose RESTful endpoints under /api/v1/ for CRUD and specific actions
# External Integration: youtube-search-python for YouTube search (no official YouTube Data API v3
# Hosting (planned): pythonAnwhere

🛡️ Security & Design Notes

* Uses DRF TokenAuthentication with IsAuthenticated for all API endpoints.
* User-specific querysets (e.g., user=self.request.user) ensure data isolation.
* Serializers validate inputs; passwords hashed with Django’s PBKDF2.
* youtube-search-python avoids API key exposure; consider HTTPS for production.

👨‍💻 Author

Kaleab Zewdie
📧 kaleabzewdie972@gmail.com
💻 junior Back-end developer | Capstone Project Contributor
