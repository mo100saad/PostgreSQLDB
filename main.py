"""
MOHAMMAD SAAD 101306472
main.py
COMP3005 Assignment Q1
Performs CRUD operations on the 'students' table in PostgreSQL. 
"""
import os  # for retrieving env variables
import psycopg2  # communicating with postgres server
from dotenv import load_dotenv  # to load in env variables


# Load environment variables
load_dotenv()  # user names, pass etc.

# declare expected hidden variables to connect to server
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Use the vars to connect to postgres
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


# read all student rows from the table
def getAllStudents():
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM students;")  # simple query to get all
        rows = cur.fetchall()
        print("\n--- All Students ---")  # text header

        # pretty-print each row with a clean date string
        for row in rows:
            student_id, first_name, last_name, email, enrollment_date = row
            # convert date object to YYYY-MM-DD string (more readable)
            formatted_date = enrollment_date.strftime("%Y-%m-%d") if enrollment_date else "N/A"
            print(f"{student_id} | {first_name} {last_name} | {email} | {formatted_date}")

        print("--------------------\n")
    except Exception as err:
        print(f"Error in getAllStudents: {err}")
    finally:
        cur.close()
        con.close()


# add a new student record
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s);
        """, (first_name, last_name, email, enrollment_date))  # insert values
        con.commit()  # save changes
        print(f"Added student {first_name} {last_name}")
    except Exception as err:
        print(f"Error in addStudent: {err}")
    finally:
        cur.close()
        con.close()


# update an existing student's email using their id
def updateStudentEmail(student_id, new_email):
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("""
            UPDATE students
            SET email = %s
            WHERE student_id = %s;
        """, (new_email, student_id))  # updates one student by id
        con.commit()
        print(f"Updated email for student ID {student_id}")
    except Exception as e:
        print(f"Error in updateStudentEmail: {e}")
    finally:
        cur.close()
        con.close()


# delete a student record by id
def deleteStudent(student_id):
    try:
        con = get_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))  # remove by id
        con.commit()
        print(f"Deleted student with ID {student_id}")
    except Exception as e:
        print(f"Error in deleteStudent: {e}")
    finally:
        cur.close()
        con.close()


# simple menu for user interaction to test CRUD
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
            getAllStudents()  # view all
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
            print("Goodbye!")  # end program
            break
        else:
            print("Invalid option\n")


if __name__ == "__main__":
    main()
