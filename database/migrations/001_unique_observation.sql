-- One row per species, per location, per day (eBird's historic endpoint
-- returns a single observation per species per day). Enables upserts so
-- re-running a load never duplicates rows.
--
-- Revert:
--   ALTER TABLE public.phillybirds DROP CONSTRAINT phillybirds_species_location_date_key;
--   ALTER TABLE public.phillybirds DROP COLUMN observation_date;

ALTER TABLE public.phillybirds
    ADD COLUMN IF NOT EXISTS observation_date DATE
    GENERATED ALWAYS AS (observation_datetime::date) STORED;

ALTER TABLE public.phillybirds
    ADD CONSTRAINT phillybirds_species_location_date_key
    UNIQUE (species_code, location_id, observation_date);
