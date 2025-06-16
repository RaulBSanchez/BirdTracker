import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path



clean_data = "/Users/raulbazan/Desktop/CleanData/DixonMeadowPreserve/2021"



def insertSql (df, file):
    load_dotenv()

    conn = psycopg2.connect(
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")
    )
      

    #df = pd.read_csv('January2025.csv')

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO dixon_meadow_preserve (
        species_code, common_name, scientific_name,
        location_id, location_name, observation_datetime,
        bird_count, latitude, longitude
    ) VALUES %s
    """

    records = list(df.itertuples(index=False, name=None))


    try:
        execute_values(cursor, insert_query, records)
        print("success")

    except: 
        print("didnt work")
        print(file)
    conn.commit()

    cursor.close()
    conn.close()
    


#print(df)

def getCsvFiles(path):
    try:
        directory = Path(path)
        for file in directory.iterdir():
            if file.is_file() and file.suffix == ".csv":
                #print(file)
                df = pd.read_csv(file)
                insertSql(df, file)
                  # filename without .csv
                #dataframes[df_name] = pd.read_csv(file)
    except FileNotFoundError:
        print("No files found.")
    except Exception as e:
        print(f"Error: {e}")




getCsvFiles(clean_data)



