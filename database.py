import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path


#Location of the data to be moved to the database
clean_data = "/Users/raulbazan/Desktop/CleanData/NewData/"




def insertSql (df, file):
    
    # Get the credentials to connect to the database
    load_dotenv()

    conn = psycopg2.connect(
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")
    )
      

    cursor = conn.cursor()

    #Query to insert data into the table. 
    insert_query = """
    INSERT INTO dixon_meadow_preserve (
        species_code, common_name, scientific_name,
        location_id, location_name, observation_datetime,
        bird_count, latitude, longitude
    ) VALUES %s
    """

    #Convert dataframe into a list of tuples to insert into PostGresSql
    records = list(df.itertuples(index=False, name=None))

    try:
        execute_values(cursor, insert_query, records)
        print("success")

    except: 
        print("This csv failed to upload: ", file)
    conn.commit()
    cursor.close()
    conn.close()
    




# Parsing the csv file to another dataframe and sending the file name as well in case the upload fails.
def getCsvFiles(path):
    try:
        directory = Path(path)
        for file in directory.iterdir():
            if file.is_file() and file.suffix == ".csv":
                df = pd.read_csv(file)
                insertSql(df, file)
    except FileNotFoundError:
        print("No files found.")
    except Exception as e:
        print(f"Error: {e}")


getCsvFiles(clean_data)



