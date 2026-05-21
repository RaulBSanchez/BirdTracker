import pandas as pd
import os
from pathlib import Path



RAW_DATA = Path('/Users/raulbazan/Projects/BirdTracker/Data/UncleanedData/')
CLEAN_DATA_PATH = Path("/Users/raulbazan/Projects/BirdTracker/Data/CleanData")


def get_csv_files(path):
    directory = Path(path)

    if not directory.exists():
        print(f"No folder found: {directory}")
        return []

    return [file for file in directory.iterdir() if file.is_file() and file.suffix == ".csv"]


def clean_dataframe(file):
    df = pd.read_csv(file)

    df["birdCount"] = pd.to_numeric(df["howMany"], errors="coerce").astype("Int64")

    df["obsDt"] = pd.to_datetime(
        df["obsDt"],
        format="%Y-%m-%d %H:%M:%S",
        errors="coerce"
    )

    df = df.drop(
        columns=[
            "obsValid",
            "obsReviewed",
            "locationPrivate",
            "exoticCategory",
            "subId",
            "howMany"
        ],
        errors="ignore"
    )

    df = df.dropna(subset=["speciesCode", "comName", "sciName", "locId", "locName", "obsDt", "birdCount"])

    df = df[df["birdCount"] <= 75]
    
    df = df.rename(columns={
    "speciesCode": "species_code",
    "comName": "common_name",
    "sciName": "scientific_name",
    "locId": "location_id",
    "locName": "location_name",
    "obsDt": "observation_datetime",
    "birdCount": "bird_count",
    "lat": "latitude",
    "lng": "longitude"})

    sql_order =[
        "species_code",
        "common_name",
        "scientific_name",
        "location_id",
        "location_name",
        "observation_datetime",
        "bird_count",
        "latitude",
        "longitude"
    ]

    df = df[sql_order]

    return df.reset_index(drop=True)


def save_clean_file(df, original_file):
    CLEAN_DATA_PATH.mkdir(parents=True, exist_ok=True)

    target_file = CLEAN_DATA_PATH / original_file.name

    df.to_csv(target_file, index=False)

    print(f"Saved clean file: {target_file}")


def clean_all_files():
    csv_files = get_csv_files(RAW_DATA)

    cleaned_dfs = {}

    for file in csv_files:
        print(f"Cleaning: {file.name}")

        df = clean_dataframe(file)
        save_clean_file(df, file)

        key = file.stem
        cleaned_dfs[key] = df

    return cleaned_dfs




if __name__ == "__main__":
    dfs = clean_all_files()

