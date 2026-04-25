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


def dataFetcher(month_name, num_days, year, month, locationTag):
    print("this is from data fetcher")
    #print(month_name, num_days, year, month)


    string_year = str(year)
    string_month = str(month)
    csv_file_name = 'NavalYard' + month_name + string_year
    path = '/Users/raulbazan/Projects/BirdTracker/Data' + '/' + csv_file_name + '.csv'
    filepath = Path(path)
    #month = month_name
    #year = year
    df = pd.DataFrame()

    print(locationTag, "from data fetcher")
    

    client_api = os.getenv('API_KEY')
    
    today = datetime.date.today()


    #print(f"{today}, todays date, current date {current_date}")

# Set the API key in the request headers
    headers = {

        'X-eBirdApiToken': client_api
    }
    #print(headers, client_api)
    for i in range(1, num_days + 1):
        print(i)
        # print("this is from the looooop")
        current_date = datetime.date(year, month, i)
        print(f"{current_date}, current date, {today}, today")
        
        if current_date >= today:
            break

        
        
        print(today, "todays data")
        print(current_date, "this is current date for loop")
        url = f"https://api.ebird.org/v2/data/obs/{locationTag}/historic/{year}/{month}/{i}"
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
                print(f"No data available for {i}, {month}, {year}")
        else:
            print("Failed to get a response from eBird")
                
        time.sleep(1)

        current_date += datetime.timedelta(days=1)


        if not df.empty and 'obsDt' in df.columns:
            df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

                # #df.to_csv(filepath, index=False)

    df.to_csv(filepath, index=False)



def fetch_historic_data(location_tag, year):
    client_api = os.getenv("API_KEY")

    headers = {
        "X-eBirdApiToken": client_api
    }

    today = datetime.date.today()

    for month in range(1, 13):
        if year == today.year and month > today.month:
            break

        month_name = calendar.month_name[month]
        num_days = calendar.monthrange(year, month)[1]

        df = pd.DataFrame()

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
                print(f"Failed for {current_date}")

            time.sleep(1)

        print(f"Finished with {month_name}")

        if not df.empty:
            df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

    
    return df


    

if __name__ == "__main__":
    main()
  


