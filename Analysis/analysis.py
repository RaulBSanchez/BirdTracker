import pandas as pd
import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from database.connection import get_connection


query = """
SELECT
    location_name,
    COUNT(DISTINCT common_name) AS unique_species
FROM PhillyBirds
GROUP BY location_name
ORDER BY unique_species DESC;
"""




try:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()


finally:
    if conn:
        conn.close()

