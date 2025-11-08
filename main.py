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