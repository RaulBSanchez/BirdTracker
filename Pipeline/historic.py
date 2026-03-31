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
    print("this is from data fetcher")
    print(month_name, num_days, year, month)

#     string_year = str(year)
#     csv_file_name = 'NavalYard' + month_name + string_year
#     path = '/Users/raulbazan/Desktop/HistoricalData/NewData/' + '/' + csv_file_name + '.csv'
#     filepath = Path(path)
#     #month = month_name
#     #year = year
#     df = pd.DataFrame()

#     client_api = os.getenv('API_KEY')

   

# # Set the API key in the request headers
#     headers = {
#         'X-eBirdApiToken': client_api
#     }
#     #print(headers, client_api)

#     for i in range(1, num_days + 1):
#         #current_date = START_DATE + datetime.timedelta(days=i)
#         #print(current_date)
#         url = f"https://api.ebird.org/v2/data/obs/L1069194/historic/{year}/{month}/{i}"
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             # Get the raw response text
#             response_text = response.text
#             data = json.loads(response_text)
#             #print(data)
#             if data:
#                 day_df = pd.DataFrame(data)
#                 df = pd.concat([df, day_df], ignore_index=True)
#             else:
#                 print(" no data for this date" , " ", month , " " , i)
#         else:
#             print("better luck next time")
        
#         time.sleep(1)



#     if not df.empty and 'obsDt' in df.columns:
#         df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

#     df.to_csv(filepath, index=False)
    

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
    years = (2020, 2021, 2022, 2023, 2024, 2025)
    

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
        dataFetcher(month_name, num_days, year, month)
    

if __name__ == "__main__":
    main()





