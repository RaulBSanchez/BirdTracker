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
#from datetime import date






def fetch_historic_data(location_tag, year):
    client_api = os.getenv("API_KEY")

    headers = {
        "X-eBirdApiToken": client_api
    }

    today = datetime.date.today()

    monthly_data = {}

    for month in range(1, 13):
        if year == today.year and month > today.month:
            break

        month_name = calendar.month_name[month]
        num_days = calendar.monthrange(year, month)[1]

        df = pd.DataFrame()

        print(f"Starting {month_name}")

        for day in range(1, num_days + 1):
            historic_date = datetime.date(year, month, day)

            if historic_date >= today:
                break

            url = (
                f"https://api.ebird.org/v2/data/obs/"
                f"{location_tag}/historic/{year}/{month}/{day}"
            )

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()

                if data:
                    day_df = pd.DataFrame(data)
                    df = pd.concat([df, day_df], ignore_index=True)

            else:
                print(f"Failed for {historic_date}")

            time.sleep(1)

        

        if not df.empty:
            df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

        key = f"{year}-{month:02d}"
        monthly_data[key] = df

        print(f"Done with {month}, {year}")

    
    return monthly_data


    

if __name__ == "__main__":
    main()
  


