# Advanced Library Management System

## 📌 Project Overview
The Advanced Library Management System is a console-based application developed using **Python** and **SQLite**.  
It follows an **industry-standard layered architecture** to manage library operations efficiently such as adding, viewing, searching, and deleting books.

---

## 🛠️ Technologies Used
- Programming Language: Python 3
- Database: SQLite
- IDE: Visual Studio Code
- OS: Windows

---

## 🏗️ Project Architecture
The project follows a **3-Tier Architecture**:

1. **Controller Layer** – Handles user interaction and input
2. **Service Layer** – Contains business logic and validation
3. **DAO (Data Access Object) Layer** – Handles database operations
4. **Database Layer** – SQLite database

---
library_mgmt/
│
├── controller/
│ └── book_controller.py
│
├── service/
│ └── book_service.py
│
├── dao/
│ └── book_dao.py
│
├── db/
│ └── connection.py
│
├── models/
│ └── book.py
│
├── database.sql
├── insert_data.sql
├── setup_db.py
├── library.db
└── main.py


---

## ✨ Features
- Add new books to the library
- View all available books
- Search books by title, author, or ISBN
- Delete books from the system
- SQLite database integration
- Console-based dashboard (menu-driven)

---

## ⚙️ Database Setup Instructions
The database is created automatically using a Python script.

### Step 1: Create Database
```bash
python setup_db.py


This will create the library.db file and required tables.

▶️ How to Run the Project

Open the project folder in VS Code

Open terminal

Run the following command:

python main.py

🧪 Testing

All CRUD operations were tested successfully

Database constraints and validations are working as expected

Sample data insertion verified

📊 Sample Output
====== Library Management System ======
1. Add Book
2. View Books
3. Search Book
4. Delete Book
5. Exit

🎯 Conclusion

This project demonstrates the use of Python with SQLite using a clean and modular architecture.
It is suitable for academic submission and helps understand real-world backend development concepts.

👤 Developed By

Name: Shaik Abdul Razak
Course: B.Tech (CSE)
Project Type: Internship-Vaultofcodes


