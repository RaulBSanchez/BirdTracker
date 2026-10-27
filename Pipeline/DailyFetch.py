import requests
import json
from dotenv import load_dotenv, dotenv_values
import os
import pandas as pd
import datetime
from time import sleep
load_dotenv()
import time
from pathlib import Path
import calendar
from config import LOCATIONS

# from datetime import date


def daily_fetch():
    client_api = os.getenv("API_KEY")

    headers = {
        "X-eBirdApiToken": client_api
    }

    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    year = yesterday.year
    month = yesterday.month
    day = yesterday.day
    df = pd.DataFrame()

    for location in LOCATIONS:
        url = (
            f"https://api.ebird.org/v2/data/obs/"
            f"{location}/historic/{year}/{month}/{day}"
        )

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            if data:
                day_df = pd.DataFrame(data)
                df = pd.concat([df, day_df], ignore_index=True)

            else:
                print(f"No data for {LOCATIONS[location]} on {month} {day}")

        else:
            print("An error occured")

    return df, yesterday


if __name__ == "__main__":
    daily_fetch()
