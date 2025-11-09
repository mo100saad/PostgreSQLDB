COMP3005 Assignment Q1
PostgreSQL CRUD Application — Mohammad Saad (101306472)

This project connects a Python application to a PostgreSQL database to perform CRUD (Create, Read, Update, Delete) operations on a students table.

Overview

The app connects to a PostgreSQL database and provides a simple menu that lets users:

View all students (getAllStudents)

Add a new student (addStudent)

Update a student’s email (updateStudentEmail)

Delete a student (deleteStudent)

Each function communicates directly with the PostgreSQL database using the psycopg2 library.

Database Setup

Step 1. Open psql and create the database:
CREATE DATABASE students_db;
\c students_db

Step 2. Create the students table:
CREATE TABLE students (
student_id SERIAL PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
enrollment_date DATE
);

Step 3. Insert initial data:
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com
', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com
', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com
', '2023-09-02');

Project Setup

Step 1. Clone the repository:
git clone https://github.com/mo100saad/PostgreSQLDB
cd Comp3005

Step 2. Create a virtual environment (recommended):
python -m venv venv
venv\Scripts\activate (on Windows)
or
source venv/bin/activate (on Mac/Linux)

Step 3. Install dependencies:
pip install -r requirements.txt

Step 4. Create a .env file in the project directory:
DB_HOST=localhost
DB_NAME=students_db
DB_USER=postgres
DB_PASSWORD=yourpassword

Running the Application

Run the program with:
python main.py

You will see:
=== Student Menu ===

Get all students

Add student

Update student email

Delete student

Exit

Follow the prompts to test each CRUD operation.

Expected Behavior

1 - Lists all current students.
2 - Inserts a new student record.
3 - Updates a student’s email (prints “No student found” if invalid ID).
4 - Deletes a student record (prints “No student found” if invalid ID).
5 - Exits the program.

Demonstration Video

A short demo that shows:

Database setup in pgAdmin or psql

Initial data insertion

Each CRUD operation being executed and verified in pgAdmin

Video link: https://youtu.be/LhWrd1eYNNU

File Structure

Comp3005/
│
├── main.py - Main Python application
├── requirements.txt - Required Python packages
├── .env - Database credentials (not pushed to GitHub) these are local to your system
├── .gitignore - Ignores .env and venv files
└── README.txt - Setup guide and documentation