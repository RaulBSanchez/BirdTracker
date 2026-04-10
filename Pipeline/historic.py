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


def dataFetcher(month_name, num_days, year, month):
    print("this is from data fetcher")
    #print(month_name, num_days, year, month)

    string_year = str(year)
    string_month = str(month)
    csv_file_name = 'NavalYard' + month_name + string_year
    path = '/Users/raulbazan/Desktop/HistoricalData/NewData/' + '/' + csv_file_name + '.csv'
    filepath = Path(path)
    #month = month_name
    #year = year
    df = pd.DataFrame()

    

    client_api = os.getenv('API_KEY')
    current_date = datetime.date(year, month, 1)
    today = datetime.date.today()


    print(f"{today}, todays date, current date {current_date}")

# Set the API key in the request headers
    headers = {
        'X-eBirdApiToken': client_api
    }
    #print(headers, client_api)
    # while current_date < today:
    #     for i in range(1, num_days + 1):
            
    #         print(today, "todays data")
    #         print(current_date, "this is current date for loop")
    #         url = f"https://api.ebird.org/v2/data/obs/L1069194/historic/{year}/{month}/{i}"
    #         response = requests.get(url, headers=headers)
    #         if response.status_code == 200:
    #                 # Get the raw response text
    #             response_text = response.text
    #             data = json.loads(response_text)
    #                 #print(data)
    #             if data:
    #                 day_df = pd.DataFrame(data)
    #                 df = pd.concat([df, day_df], ignore_index=True)
    #             else:
    #                 print(f"No data available for {i}, {month}, {year}")
    #         else:
    #             print("Failed to get a response from eBird")
                
    #         time.sleep(1)

    #         current_date += datetime.timedelta(days=1)


    #     if not df.empty and 'obsDt' in df.columns:
    #         df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

    #             # #df.to_csv(filepath, index=False)
    #         print(df)

def main():
    # This method will iterate over the months and call the data fetcher in order to 
    # get all the birds from the given month of the eBird Api
    locations = {
    1: ["L1025768", "FDR"],
    2: ["L1069194" ,"Philadelphia Naval Yard"],
    3: ["L1145863", "Wissahickon Valley"],
    4: ["L3041917", "Dixon Meadow Preserve"],
    5: ["L504403",  "John Heinz"]
    }
    years = (2020, 2021, 2022, 2023, 2024, 2025, 2026)
    

    print("Please select a location to the historical data for")


    #Display the selection of locations
    for key, val in locations.items():
        print(f" {key} : {val[1]}")

    
    while True:    
        try:
            locationValue = int(input("Enter number: "))
            if locationValue not in locations:
                print("Please enter valid choice")
                continue
            break
                
        except ValueError:
            print("Pleaes select a number")

    print("Choose one of the following years")
    for year in years:
        print(year)


    while True:
        
        try:
            year = int(input("Enter number: "))
            if year not in years:
                print("Choose Valid Year")
                continue
            break

        except ValueError:
            print("Enter A valid choice")

            


    for month in range(1, 13):
        month_name = calendar.month_name[month]
        num_days = calendar.monthrange(year, month)[1]

        today = datetime.date.today()
        print(today.year, today.month)
        print(today, " todays month comparison")
        if year == today.year and month > today.month:
            break
        
        dataFetcher(month_name, num_days, year, month)
    


def testHistory():
    print("hello from history")

if __name__ == "__main__":
    main()
  


