# 🐦 BirdTracker

BirdTracker pulls bird sightings from the [eBird API](https://documenter.getpostman.com/view/664302/S1ENwy59) for five hotspots around Philadelphia. It cleans the data, loads it into PostgreSQL, and serves it through a small FastAPI service.

## Tracked hotspots

| eBird ID   | Name                    |
|------------|-------------------------|
| `L1025768` | FDR Park                |
| `L1069194` | Philadelphia Naval Yard |
| `L1145863` | Wissahickon Valley      |
| `L3041917` | Dixon Meadow Preserve   |
| `L504403`  | John Heinz NWR          |

To add or remove hotspots, edit `LOCATIONS` in [Pipeline/config.py](Pipeline/config.py).

## How it works

```
eBird API ──► Data/UncleanedData/*.csv ──► cleanup.py ──► Data/CleanData/*.csv ──► database.py ──► PostgreSQL ──► FastAPI
                       │                                        │
                       ▼                                        ▼
               Data/Archive/Raw/                       Data/Archive/Loaded/
```

1. **Fetch.** [Pipeline/cli.py](Pipeline/cli.py) calls eBird's `historic` endpoint (`/v2/data/obs/{locId}/historic/{y}/{m}/{d}`) and saves the raw CSV to `Data/UncleanedData/`.
2. **Clean.** [Pipeline/cleanup.py](Pipeline/cleanup.py) renames columns to snake_case, parses dates, and drops rows that are missing fields or have a non-numeric count. It also drops counts over 75. The raw file then moves to `Data/Archive/Raw/`.
3. **Load.** [Pipeline/database.py](Pipeline/database.py) upserts the clean rows into `public.phillybirds`, keyed on species, location and day, so re-running a load never creates duplicates. A file moves to `Data/Archive/Loaded/` only when its load succeeds. If a load fails, the file stays where it is so you can retry.

## Setup

**Requirements:** Python 3.10+, PostgreSQL, and an [eBird API key](https://ebird.org/api/keygen).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```dotenv
API_KEY=your_ebird_api_key
DB_NAME=birdtracker
DB_USER=postgres
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
```

Create the table:

```bash
psql -d birdtracker -f database/schema.sql
```

If your database is older and doesn't have the unique key yet, run the migration instead:

```bash
psql -d birdtracker -f database/migrations/001_unique_observation.sql
```

## Running the pipeline

The pipeline modules import each other by bare name, so run them from inside `Pipeline/`:

```bash
cd Pipeline
python cli.py
```

Choose a mode:

| # | Mode             | What it fetches                                        | Raw file name                       |
|---|------------------|--------------------------------------------------------|-------------------------------------|
| 1 | Daily Fetch      | Yesterday, all hotspots                                | `daily_YYYY-MM-DD.csv`              |
| 2 | Monthly Fetch    | Every day of the previous month, all hotspots          | `monthly_YYYY-MM.csv`               |
| 3 | Historical Fetch | A full year (2020 onward) for one hotspot you choose   | `<Hotspot>_<YYYY>.csv`              |
| 4 | Date Range Fetch | Any start and end date up to yesterday, all hotspots   | `range_<start>_to_<end>.csv`        |

After fetching, the CLI cleans the data and loads it automatically. To re-run only the clean and load steps (for example, to retry a failed load):

```bash
cd Pipeline
python pipeline.py
```

## API

Run the API from the project root:

```bash
uvicorn api.app:app --reload
```

Interactive docs are at http://127.0.0.1:8000/docs.

| Endpoint                       | Description                                                                                       |
|--------------------------------|---------------------------------------------------------------------------------------------------|
| `GET /health`                  | Checks the database connection                                                                    |
| `GET /observations`            | Sightings, newest first. Optional filters: `observation_date`, `location_id`, `species_code`, `limit` (1–1000, default 100) |
| `GET /species/top`             | Most frequently observed species (`limit` 1–100, default 10)                                      |
| `GET /YesterdaysObservations/` | Distinct species and locations seen yesterday                                                     |
| `GET /LifeList/`               | Personal life list from the `bird_cards` and `bird_card_media` tables (not created by `schema.sql`) |

## Database schema

`public.phillybirds` ([database/schema.sql](database/schema.sql)):

| Column                 | Type             | Notes                                     |
|------------------------|------------------|-------------------------------------------|
| `observation_id`       | `SERIAL`         | Primary key                               |
| `species_code`         | `VARCHAR`        | eBird species code, e.g. `amerob`         |
| `common_name`          | `VARCHAR`        |                                           |
| `scientific_name`      | `VARCHAR`        |                                           |
| `location_id`          | `VARCHAR`        | eBird hotspot ID                          |
| `location_name`        | `VARCHAR`        |                                           |
| `observation_datetime` | `TIMESTAMP`      |                                           |
| `bird_count`           | `INTEGER`        |                                           |
| `latitude`             | `DOUBLE PRECISION` |                                         |
| `longitude`            | `DOUBLE PRECISION` |                                         |
| `observation_date`     | `DATE`           | Generated from `observation_datetime`     |

The table is unique on `(species_code, location_id, observation_date)`.

## Analysis

[Analysis/](Analysis/) holds SQL queries and a small runner script:

- `yesterdays_birds.sql`: every species and location reported yesterday
- `unique_location.sql`: species seen yesterday at only one hotspot

```bash
python Analysis/analysis.py
```

## Known limitations

- eBird's `historic` endpoint returns one observation per species per location per day, not every checklist. `bird_count` therefore comes from a single checklist and is not a daily total.
- Counts above 75, and counts recorded as "X" (present but not counted), are dropped during cleaning.
- The daily fetch only covers yesterday, so it misses checklists submitted late. Use the Date Range Fetch to backfill.

See [TODO.md](TODO.md) for planned work.

## Project structure

```
BirdTracker/
├── Pipeline/        # CLI, eBird fetchers, cleaning, loading
├── api/             # FastAPI service
├── database/        # Connection helper, schema, migrations
├── Analysis/        # SQL queries and analysis script
├── Data/            # Raw, clean and archived CSVs (git-ignored)
└── requirements.txt
```

---

*Made with 🐦 and 📊 by Raul Bazan*
