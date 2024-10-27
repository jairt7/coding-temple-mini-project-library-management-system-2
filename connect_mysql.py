import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "library"
    user = "root"
    password = "password"
    host = "localhost"
    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        print("Connection successful.")
        return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None