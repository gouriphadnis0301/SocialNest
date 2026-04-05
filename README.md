# 🚀 SocialNest - Social Media API (FastAPI)

SocialNest is a scalable backend REST API for a social media application built using FastAPI. It supports user authentication, post creation, and a voting system. The API is designed with clean architecture and follows modern backend development practices.

---

## 📌 Project Overview

This project simulates the backend of a social media platform where users can:

* Register and login securely
* Create and manage posts
* View posts created by others
* Vote (like/unlike) posts
* Access protected routes using JWT authentication

It is built to demonstrate backend development skills using FastAPI and PostgreSQL.

---

## ✨ Features

* 🔐 JWT-based Authentication (Login system)
* 👤 User Registration & Management
* 📝 CRUD Operations for Posts
* 👍 Voting System (Like/Unlike Posts)
* 🔒 Protected Routes (Authorization required)
* ⚡ Fast and high-performance API
* 📄 Interactive API Documentation (Swagger UI)

---

## 🛠 Tech Stack

* FastAPI
* Python
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn
* JWT Authentication

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/socialnest-fastapi.git
cd socialnest-fastapi

---

### 🔹 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate

---

### 🔹 3. Install Dependencies

pip install -r requirements.txt

---

### 🔹 4. Setup Environment Variables

Create a `.env` file in the root directory:

DATABASE_NAME=fastapi
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=yourpassword

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

---

### 🔹 5. Run the Server

uvicorn app.main:app --reload

---

## 🌐 API Documentation

Once the server is running:

http://127.0.0.1:8000/docs

---

## 🔑 Authentication Flow

1. Create User → /users/
2. Login → /login
3. Copy Access Token
4. Click **Authorize** in Swagger UI
5. Use protected endpoints like /posts/

---

## 📂 Project Structure

app/
┣ routers/
┃ ┣ auth.py
┃ ┣ post.py
┃ ┣ user.py
┃ ┣ vote.py
┣ models.py
┣ database.py
┣ config.py
┣ main.py

---

## 🧪 Example API Endpoints

### 🔹 User

POST /users/ → Create User
GET /users/{id} → Get User

### 🔹 Authentication

POST /login → Login User

### 🔹 Posts

GET /posts/ → Get All Posts
POST /posts/ → Create Post
PUT /posts/{id} → Update Post
DELETE /posts/{id} → Delete Post

### 🔹 Vote

POST /vote/ → Vote A Post

---

## 🚧 Future Improvements

* Add comments feature
* Image upload support
* Pagination & filtering
* Deployment (AWS / Render / Docker)
* Notification system

---

## 👩‍💻 Author

Gouri Phadnis

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 📌 Note

Do not upload `.env` file or database credentials to GitHub.
