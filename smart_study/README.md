# 📘 Study Guide System

A **personal productivity and learning web application** built with **Django**.  
The Study Guide System helps students and lifelong learners organize their study activities by combining multiple essential tools—notes, tasks, homework, and study aids—into one unified platform.

---

## 🚀 Key Features

- 📝 **Notepad:** Create, edit, and organize personal study notes.  
- ✅ **To-Do List:** Manage study tasks and deadlines with progress tracking.  
- 📚 **Homework Writer:** Write and save assignments or study summaries.  
- 🎥 **YouTube Search:** Integrated **YouTube Data API v3** for finding educational videos.  
- 🔐 **User Authentication:** Secure login and registration for personalized access.  
---

## 🧩 Project Structure

| App | Description |
|------|--------------|
| `users` | Handles registration, login, and profile management |
| `notes` | Notepad for creating and managing study notes |
| `homework` | Writing and saving assignments |
| `tasks` | To-do list for managing tasks and goals |
| `videos` | YouTube API integration for study content |
| `tools` | Utility functions such as unit converter |

---

## 🗄️ Database Overview

| Model | Key Fields |
|--------|-------------|
| **User** | username, email, password |
| **Note** | title, content, created_at, updated_at |
| **Task** | description, is_completed, due_date |
| **Homework** | subject, content, created_at |

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
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Run the Development Server
python manage.py runserver

6️⃣ Access the App

Open your browser and go to:
http://127.0.0.1:8000/


🛠️ Technologies Used

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: SQLite 

API: YouTube Data API v3

Hosting (planned): Render / Heroku

🛡️ Security & Design Notes

Implements Django’s built-in CSRF protection and secure session handling

Modular architecture (separate apps for maintainability)

Prepared for deployment with HTTPS configuration


👨‍💻 Author

Kaleab Zewdie
📧 kaleabzewdie972@gmail.com
💻 Django Developer | Capstone Project Contributor