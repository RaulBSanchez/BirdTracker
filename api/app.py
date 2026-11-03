from datetime import date
from typing import Optional

from fastapi import FastAPI, Query
from psycopg2.extras import RealDictCursor

from database.connection import get_connection


app = FastAPI(title="BirdTracker API")


def run_query(query, params=None):
    # Run a read-only query and return rows as a list of dicts
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        conn.close()


@app.get("/health")
def health():
    run_query("SELECT 1")
    return {"status": "ok"}


@app.get("/observations")
def get_observations(
    observation_date: Optional[date] = None,
    location_id: Optional[str] = None,
    species_code: Optional[str] = None,
    limit: int = Query(100, ge=1, le=1000),
):
    # Every filter is optional; a NULL parameter matches all rows
    query = """
    SELECT
        observation_id,
        species_code,
        common_name,
        scientific_name,
        location_id,
        location_name,
        observation_datetime,
        bird_count,
        latitude,
        longitude
    FROM public.phillybirds
    WHERE (%(observation_date)s::date IS NULL OR observation_date = %(observation_date)s)
      AND (%(location_id)s::text IS NULL OR location_id = %(location_id)s)
      AND (%(species_code)s::text IS NULL OR species_code = %(species_code)s)
    ORDER BY observation_datetime DESC
    LIMIT %(limit)s
    """
    params = {
        "observation_date": observation_date,
        "location_id": location_id,
        "species_code": species_code,
        "limit": limit,
    }
    return run_query(query, params)


@app.get("/species/top")
def get_top_species(limit: int = Query(10, ge=1, le=100)):
    query = """
    SELECT
        common_name,
        COUNT(*) AS total_observations
    FROM public.phillybirds
    GROUP BY common_name
    ORDER BY total_observations DESC
    LIMIT %(limit)s
    """
    return run_query(query, {"limit": limit})


@app.get("/LifeList/")
def get_life_list(limit: int = Query(10, ge=1, le=100)):
    query = """
    SELECT
        bc.card_id,
        bc.common_name,
        bcm.sex,
        bcm.macaulay_asset_id,
        bcm.contributor,
        bcm.source_url
    FROM bird_cards bc
    LEFT JOIN bird_card_media bcm
        ON bc.card_id = bcm.card_id
    ORDER BY bc.card_number, bcm.sex;
    """
    return run_query(query, {"limit": limit})

@app.get("/YesterdaysObservations/")
def get_life_list(limit: int = Query(10, ge=1, le=100)):
    query = """
    SELECT DISTINCT common_name, location_name, observation_date
    FROM public.phillybirds
    WHERE observation_date = CURRENT_DATE - 1
    ORDER BY common_name;
    """
    return run_query(query, {"limit": limit})