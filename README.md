
---

# 🏥 Patient Management System API (FastAPI + SQLite)

A **RESTful API** built with **FastAPI** for managing patient records using **SQLite** as the database and **SQLAlchemy ORM**.
This project demonstrates clean API design, data validation, and CRUD operations using modern Python tools.

---

## 🚀 Features

* Create, read, update, and delete patient records
* Store data in **SQLite database**
* Sort patients by height or weight
* Automatic data validation using Pydantic
* Interactive API documentation (Swagger UI)
* Clean project structure with ORM support

---

## 🛠️ Tech Stack

* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**
* **Uvicorn**

---

## 📂 Project Structure

```
.
├── main.py
├── database.py
├── models.py
├── schemas.py
├── patients.db
├── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

---

### 4️⃣ Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive docs:

* **Swagger UI**

```
http://127.0.0.1:8000/docs
```

* **ReDoc**

```
http://127.0.0.1:8000/redoc
```

---

## 🌐 API Endpoints

| Method | Endpoint                | Description                       |
| ------ | ----------------------- | --------------------------------- |
| GET    | `/`                     | Welcome message                   |
| GET    | `/about`                | About the API                     |
| GET    | `/view`                 | View all patients                 |
| GET    | `/patient/{patient_id}` | View patient by ID                |
| POST   | `/create`               | Create a new patient              |
| PUT    | `/edit/{patient_id}`    | Update patient details            |
| DELETE | `/delete/{patient_id}`  | Delete a patient                  |
| GET    | `/sort`                 | Sort patients by height or weight |

---

## 🗃️ Database

* Uses **SQLite**
* Database file: `patients.db`
* Tables are created automatically on application startup

---

## 📌 Notes

* Patient ID must be unique
* All inputs are validated using Pydantic
* Designed for learning, practice, and small projects
* Can be easily extended to PostgreSQL or MySQL

---

## 🚀 Future Improvements

* Add authentication & authorization
* Add pagination and filtering
* Add BMI calculation as computed field
* Add Alembic migrations
* Deploy using Docker

---
