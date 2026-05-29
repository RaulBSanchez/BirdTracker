import pandas as pd
from database import get_connection


query = """
SELECT
    location_name,
    COUNT(DISTINCT common_name) AS unique_species
FROM public.dixon_meadow_preserve
GROUP BY location_name
ORDER BY unique_species DESC;
"""


conn = None

try:
    conn = get_connection()

    df = pd.read_sql_query(query, conn)

    print("\nSpecies Diversity by Location:")
    print(df)

finally:
    if conn:
        conn.close()