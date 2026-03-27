# 🎓 Student Management System - Backend (Flask API)

## 📌 Overview
This project is a RESTful backend API for a Student Management System built using Flask and SQLAlchemy.  
It supports full CRUD operations (Create, Read, Update, Delete) to manage student records efficiently.

---

## 🚀 Tech Stack
- Python
- Flask
- SQLAlchemy (ORM)
- SQLite
- REST API
- Git & GitHub

---

## ⚙️ Features
- ➕ Add new student
- 📄 View all students
- ✏️ Update student details
- ❌ Delete student
- ✅ Input validation
- 🚫 Duplicate email handling
- 📦 Proper HTTP status codes (200, 201, 400, 404, 500)

---

## 📂 Project Structure

```
student-management-backend/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
└── .gitignore
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| POST   | /add-student | Add a new student |
| GET    | /students | Retrieve all students |
| PUT    | /update-student/<id> | Update student details |
| DELETE | /delete-student/<id> | Delete a student |

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/soujanya1007/student-management-backend.git
```

2. Navigate to project folder:

```bash
cd student-management-backend
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000/
```

---

## 🧠 Concepts Demonstrated
- RESTful API design
- Database modeling using ORM
- CRUD operations
- Error handling & validation
- Git version control

---

## 👩‍💻 Author
**Soujanya H Patil**
