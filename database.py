import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        database = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "5432")

        conn = psycopg2.connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None

def insert_observation():
    conn = get_connection()
    if not conn:
        return

    try:
        cur = conn.cursor()

        insert_query = """
            INSERT INTO dixon_meadow_preserve (
                species_code, common_name, scientific_name,
                location_id, location_name, observation_datetime,
                bird_count, latitude, longitude
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        values = (
            'mallar3', 'Mallard', 'Anas platyrhynchos',
            'L3041917', 'Dixon Meadow Preserve', '2025-05-01 10:52:00',
            1, 40.1003152, -75.2402115
        )

        cur.execute(insert_query, values)
        conn.commit()
        print("Observation inserted successfully.")

    except Exception as e:
        print("Insert failed:", e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    insert_observation()