📚 Book Store Management System

An advanced Django-based E-Commerce web application for managing and purchasing books online.

---

## 🚀 Project Overview

Book Store Management System is a full-stack Django web application that allows users to:

- Browse available books
- Search books by title or author
- Add books to cart
- Proceed to checkout
- Place orders (Cash on Delivery)
- Admin manage books, categories, and orders

This project demonstrates full-stack web development using Django framework.

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML5, CSS3, Bootstrap 5
- Database: SQLite3
- Authentication: Django Built-in Auth System

---

## ✨ Features

### 👤 User Side
- View all books
- Search functionality
- Add to cart
- Remove from cart
- Checkout system
- Order confirmation page

### 🛠️ Admin Side
- Add / Update / Delete Books
- Manage Categories
- View Cart Data
- Manage Orders
- Secure Admin Login

---

## 📂 Project Structure


bookstore/
│
├── store/ # Book & Category management
├── cart/ # Cart functionality
├── orders/ # Order & checkout system
├── templates/ # HTML templates
├── manage.py
└── db.sqlite3


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/yourusername/bookstore-project.git
cd bookstore-project
2️⃣ Install Dependencies
pip install django
3️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
4️⃣ Create Superuser
python manage.py createsuperuser
5️⃣ Run Server
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/
Admin Panel:
http://127.0.0.1:8000/admin/

🧪 Demo Flow

Admin adds Categories and Books
User browses books
Adds books to cart
Proceeds to checkout
Places order

Order is stored in database

🎯 Learning Outcomes

Django MVC Architecture
Database Relationships (Foreign Keys)
Authentication System
Cart & Order Management
Full-stack E-Commerce Workflow

📌 Future Enhancements

Online Payment Integration (Razorpay / Stripe)
User Order History
Product Images Upload
REST API Integration
Deployment on AWS / Heroku

👩‍💻 Developed By

Jade Akhila
B.Tech – Artificial Intelligence & Machine Learning
