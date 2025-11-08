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