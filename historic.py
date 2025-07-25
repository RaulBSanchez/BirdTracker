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



def dataFetcher(month_name, num_days, year, month):

    string_year = str(year)
    csv_file_name = 'NavalYard' + month_name + string_year
    path = '/Users/raulbazan/Desktop/HistoricalData/NewData/' + '/' + csv_file_name + '.csv'
    filepath = Path(path)
    #month = month_name
    #year = year
    df = pd.DataFrame()

    client_api = os.getenv('API_KEY')

   

# Set the API key in the request headers
    headers = {
        'X-eBirdApiToken': client_api
    }
    #print(headers, client_api)

    for i in range(1, num_days + 1):
        #current_date = START_DATE + datetime.timedelta(days=i)
        #print(current_date)
        url = f"https://api.ebird.org/v2/data/obs/L1069194/historic/{year}/{month}/{i}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Get the raw response text
            response_text = response.text
            data = json.loads(response_text)
            #print(data)
            if data:
                day_df = pd.DataFrame(data)
                df = pd.concat([df, day_df], ignore_index=True)
            else:
                print(" no data for this date" , " ", month , " " , i)
        else:
            print("better luck next time")
        
        time.sleep(1)



    if not df.empty and 'obsDt' in df.columns:
        df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

    df.to_csv(filepath, index=False)
    

def month():
    # This method will iterate over the months and call the data fetcher in order to 
    # get all the birds from the given month of the eBird Api
    print("Enter Year")
    year = int(input())
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        num_days = calendar.monthrange(year, month)[1]
        dataFetcher(month_name, num_days, year, month)


month()





