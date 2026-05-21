import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path


#Location of the data to be moved to the database
# clean_data = "/Users/raulbazan/Desktop/BirdData/CleanData/NewData/"
# Location of the cleaned CSV files
clean_data = "/Users/raulbazan/Projects/BirdTracker/Data/CleanData"


def insertSql(df, file):

    # Load environment variables
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

    # SQL insert query
    insert_query = """
    INSERT INTO dixon_meadow_preserve (
        species_code,
        common_name,
        scientific_name,
        location_id,
        location_name,
        observation_datetime,
        bird_count,
        latitude,
        longitude
    ) VALUES %s
    """

    # Explicitly match dataframe columns to SQL column order
    columns = [
        "species_code",
        "common_name",
        "scientific_name",
        "location_id",
        "location_name",
        "observation_datetime",
        "bird_count",
        "latitude",
        "longitude"
    ]

    # Convert dataframe rows into tuples
    records = list(df[columns].itertuples(index=False, name=None))

    try:
        execute_values(cursor, insert_query, records)

        conn.commit()

        print(f"Successfully uploaded: {file.name}")

    except Exception as e:

        conn.rollback()

        print(f"Failed to upload: {file.name}")
        print("Error:", e)

    finally:
        cursor.close()
        conn.close()


# Parse CSV files and send them to PostgreSQL
def getCsvFiles(path):

    try:
        directory = Path(path)

        for file in directory.iterdir():

            if file.is_file() and file.suffix == ".csv":

                print(f"Processing: {file.name}")

                df = pd.read_csv(file)

                insertSql(df, file)

    except FileNotFoundError:
        print("No files found.")

    except Exception as e:
        print(f"Error: {e}")


def testDataBase():
    print("hello from database")


if __name__ == "__main__":

    getCsvFiles(clean_data)



