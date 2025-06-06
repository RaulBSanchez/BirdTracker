-- Database: Birds

-- DROP DATABASE IF EXISTS "Birds";

CREATE DATABASE "Birds"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    ICU_LOCALE = 'en-US'
    LOCALE_PROVIDER = 'icu'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;




-- Create Dixon Table 

CREATE TABLE dixon_meadow_preserve (
    observation_id SERIAL PRIMARY KEY,
    species_code VARCHAR(255),
    common_name VARCHAR(255),
    scientific_name VARCHAR(255),
    location_id VARCHAR(255),
    location_name VARCHAR(255),
    observation_datetime TIMESTAMP,
    bird_count INT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);
