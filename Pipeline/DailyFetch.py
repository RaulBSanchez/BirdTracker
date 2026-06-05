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


def daily_fetch(location_tag, year):


    locations = {
	"L1025768":	"FDR",
	"L1069194":	"PhiladelphiaNavalYard",
	"L1145863":	"WissahickonValley",
	"L3041917":	"DixonMeadowPreserve",
	"L504403":	"JohnHeinz"
	}
    client_api = os.getenv("API_KEY")

    headers = {
        "X-eBirdApiToken": client_api
    }

    today = datetime.date.today()
    print(today)
    df = pd.DataFrame()
    url = (
        f"https://api.ebird.org/v2/data/obs/"
        f"L504403/historic/2026/06/04")
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data:
            day_df = pd.DataFrame(data)
            df = pd.concat([df, day_df], ignore_index=True)

        else:
            print(f"Failed for today")

    print(df)

location = "Hello"
year = 2026
daily_fetch(location, year)




