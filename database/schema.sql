-- Schema for the PhillyBirds table, matching the live database.
-- Run once against a fresh database: psql -d <DB_NAME> -f database/schema.sql

CREATE TABLE IF NOT EXISTS public.phillybirds (
    observation_id       SERIAL PRIMARY KEY,
    species_code         VARCHAR(255),
    common_name          VARCHAR(255),
    scientific_name      VARCHAR(255),
    location_id          VARCHAR(255),
    location_name        VARCHAR(255),
    observation_datetime TIMESTAMP,
    bird_count           INTEGER,
    latitude             DOUBLE PRECISION,
    longitude            DOUBLE PRECISION
);
