import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path



def main():
    load_dotenv()

    # Connect to PostgreSQL
    conn = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
    )

    cursor = conn.cursor()

    query = """
    SELECT 
        common_name,
        COUNT(*) AS total_observations
    FROM PhillyBirds
    GROUP BY common_name
    ORDER BY total_observations DESC
    LIMIT 10;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()


if __name__ == "main":
    main()