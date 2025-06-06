import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        database = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")

        #print(database, user, password, host, port)  # For debugging (optional)

    
    except Exception as e:
        print("Error:", e)
        return False

conn = get_connection()
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered an error.")
