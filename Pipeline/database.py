import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
from config import CLEAN_DATA_DIR, ARCHIVE_LOADED_DIR





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

    # SQL upsert query: one row per species, per location, per day.
    # Re-loading the same data updates the existing row instead of duplicating it.
    insert_query = """
    INSERT INTO PhillyBirds (
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
    ON CONFLICT (species_code, location_id, observation_date) DO UPDATE SET
        common_name = EXCLUDED.common_name,
        scientific_name = EXCLUDED.scientific_name,
        location_name = EXCLUDED.location_name,
        observation_datetime = EXCLUDED.observation_datetime,
        bird_count = EXCLUDED.bird_count,
        latitude = EXCLUDED.latitude,
        longitude = EXCLUDED.longitude
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

    # Postgres can't upsert the same key twice in one statement, so keep the
    # latest row per species/location/day
    df = df.assign(observation_date=pd.to_datetime(df["observation_datetime"]).dt.date)
    df = df.sort_values("observation_datetime").drop_duplicates(
        subset=["species_code", "location_id", "observation_date"], keep="last"
    )

    # Convert dataframe rows into tuples
    records = list(df[columns].itertuples(index=False, name=None))

    try:
        if records:
            execute_values(cursor, insert_query, records)

        conn.commit()

        print(f"Successfully uploaded: {file.name} ({len(records)} rows)")
        return True

    except Exception as e:

        conn.rollback()

        print(f"Failed to upload: {file.name}")
        print("Error:", e)
        return False

    finally:
        cursor.close()
        conn.close()


# Parse CSV files and send them to PostgreSQL
def getCsvFiles(path):

    try:
        directory = Path(path)
        print(directory)
        for file in directory.iterdir():

            if file.is_file() and file.suffix == ".csv":

                print(f"Processing: {file.name}")

                df = pd.read_csv(file)

                # Archive only on success; failed files stay put for a retry
                if insertSql(df, file):
                    ARCHIVE_LOADED_DIR.mkdir(parents=True, exist_ok=True)
                    file.replace(ARCHIVE_LOADED_DIR / file.name)

    except FileNotFoundError:
        print("No files found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    getCsvFiles(CLEAN_DATA_DIR)



