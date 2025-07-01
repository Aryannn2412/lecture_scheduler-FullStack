# 📚 Online Lecture Scheduling System

A full-stack role-based web application where **Admins** can create courses and assign lectures, and **Instructors** can view their personalized lecture schedule.

---

## 🚀 Tech Stack

- 🧠 Python + Flask
- 🧱 SQLite (via SQLAlchemy ORM)
- 🖥️ HTML5, Bootstrap 5, Jinja2
- 🔐 Flask-Login, Flask-WTF, Email Validator

---

## ✨ Key Features

### 👩‍💼 Admin Functionality
- Register and login as **Admin**
- Add new courses with:
  - Course Name
  - Level (Beginner, Intermediate, Advanced)
  - Description
  - (Optional) Image URL
- Assign lectures to instructors on specific dates
- ✅ **Date collision check**: Instructor cannot be double-booked on the same date
- View list of instructors while scheduling

### 👨‍🏫 Instructor Functionality
- Register and login as **Instructor**
- View all upcoming lectures assigned to you
- See course name and scheduled date
- Sorted in chronological order

---

## 👤 User Roles

Users can register as:
- ✅ **Admin**
- ✅ **Instructor**

Signup includes a dropdown to select your role, handled securely via Flask backend.

---

## 🔑 Demo Credentials (For Testing)

> Replace with your created users

### Admin:
- Email: `admin@demo.com`
- Password: `admin123`

### Instructor:
- Email: `instructor@demo.com`
- Password: `instructor123`

---
## Demo Video Drive link

https://drive.google.com/file/d/1ykPM9G7Vrvm-QI9sGZTE9rPrIGLQ-QTk/view?usp=sharing


## 🧪 How to Run Locally

bash:
git clone <your-repo-url>
cd lecture_scheduler
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt

flask --app app.py create-db  # Initializes the database
python app.py                 # Runs the server

# Visit: http://127.0.0.1:5000
