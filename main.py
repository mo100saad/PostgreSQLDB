"""
MOHAMMAD SAAD 101306472
main.py
COMP3005 Assignment Q1
Performs CRUD operations on the 'students' table in PostgreSQL. 
"""
import os #for retrieving env variables
import psycopg2 #communicating with postgress server
from dotenv import load_dotenv #to load in env variables


# Load environment variables
load_dotenv() #user names pass etc.

# declare expected hidden variables to connect to server
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#Use the vars to connect to postgress
def get_connection():
    return psycopg2.connect( 
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def getAllStudents():
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM students;")
        rows = cur.fetchall()
        print("\n--- All Students ---") #Text display before saying students
        for row in rows:
            print(row)
        print("--------------------\n")
    except Exception as err:
        print(f"Error in getAllStudents: {err}")
    finally:
        cur.close()
        con.close()

def addStudent(first_name, last_name, email, enrollment_date):
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s);
        """, (first_name, last_name, email, enrollment_date))
        con.commit()
        print(f"Added student {first_name} {last_name}")
    except Exception as err:
        print(f"Error in addStudent: {err}")
    finally:
        cur.close()
        con.close()

def updateStudentEmail(student_id, new_email):
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            UPDATE students
            SET email = %s
            WHERE student_id = %s;
        """, (new_email, student_id))
        con.commit()
        print(f"Updated email for student ID {student_id}")
    except Exception as e:
        print(f"Error in updateStudentEmail: {e}")
    finally:
        cur.close()
        con.close()

def deleteStudent(student_id):
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        con.commit()
        print(f"Deleted student with ID {student_id}")
    except Exception as e:
        print(f"Error in deleteStudent: {e}")
    finally:
        cur.close()
        con.close()

def main():
    while True:
        print("=== Student Menu ===")
        print("1. Get all students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            getAllStudents()
        elif choice == "2":
            f = input("First name: ")
            l = input("Last name: ")
            e = input("Email: ")
            d = input("Enrollment date (YYYY-MM-DD): ")
            addStudent(f, l, e, d)
        elif choice == "3":
            sid = input("Student ID: ")
            new = input("New email: ")
            updateStudentEmail(sid, new)
        elif choice == "4":
            sid = input("Student ID: ")
            deleteStudent(sid)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option\n")

if __name__ == "__main__":
    main()