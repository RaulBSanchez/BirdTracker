import requests
from dotenv import load_dotenv
import os
import pandas as pd
import datetime
import time
load_dotenv()
from config import LOCATIONS


def fetch_date_range(start_date, end_date):
    client_api = os.getenv("API_KEY")

    headers = {
        "X-eBirdApiToken": client_api
    }

    df = pd.DataFrame()
    current = start_date

    # For loop to iterate through every location for each day in the range
    while current <= end_date:
        print(f"Fetching {current.isoformat()}")

        for location in LOCATIONS:
            url = (
                f"https://api.ebird.org/v2/data/obs/"
                f"{location}/historic/{current.year}/{current.month}/{current.day}"
            )

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()

                if data:
                    day_df = pd.DataFrame(data)
                    df = pd.concat([df, day_df], ignore_index=True)

                else:
                    print(f"No data for {LOCATIONS[location]} on {current.isoformat()}")

            else:
                print(f"Failed for {LOCATIONS[location]} on {current.isoformat()} ({response.status_code})")

            time.sleep(1)

        current += datetime.timedelta(days=1)

    return df
