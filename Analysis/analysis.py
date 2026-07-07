import pandas as pd
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from database.connection import get_connection
from pathlib import Path

# previous_day_observations = """
# SELECT DISTINCT
#     common_name,
#     location_name
# FROM public.phillybirds
# WHERE observation_datetime::date = CURRENT_DATE - INTERVAL '1 day'
# ORDER BY common_name, location_name;
# """



# try:
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute(previous_day_observations)
#     results = cursor.fetchall()

#     for row in results:
#         print(row)

#     cursor.close()
#     conn.close()


# finally:
#     if conn:
#         conn.close()




def run_query(filename):
    conn = None
    try:
        sql_path = Path(__file__).parent / filename
        
        with open(sql_path, "r") as file:
            query = file.read()
            print(query)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            #print(results)
            # print(results)
            #df = pd.read_sql(query, conn)
            columns = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(results, columns=columns)
            cursor.close()
            return df


    except:
        print("didnt work")

    finally: 
        if conn:
            conn.close()

location_birds = run_query("unique_location.sql")
print(location_birds)
