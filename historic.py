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

START_DATE = datetime.date(2025, 1, 1)
END_DATE = datetime.date(2025, 1, 31)


print("Enter Year")
year = input()
print(year)
print("Enter Month")
month = input()
print(month)

filepath = Path('/Users/raulbazan/Desktop/HistoricalData/DixonMeadowPreserve/2025/January2025.csv')

# URL for hotspot data
#url = 'https://api.ebird.org/v2/data/obs/L3041917/historic/2025/04/17'
client_api = os.getenv('API_KEY')
# L3041917

# Set the API key in the request headers
headers = {
    'X-eBirdApiToken': client_api
}

# Send GET request to fetch hotspots
#response = requests.get(url, headers=headers)

bird_count = {}

current_date = START_DATE
# url = "https://api.ebird.org/v2/data/obs/{{regionCode}}/historic/{{y}}/{{m}}/{{d}}"
df = pd.DataFrame()
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df2 = pd.DataFrame(data)

# for i in range((END_DATE - START_DATE).days + 1):
#     current_date = START_DATE + datetime.timedelta(days=i)
#     #print(current_date)
#     url = f'https://api.ebird.org/v2/data/obs/L3041917/historic/{current_date.year}/{current_date.month}/{current_date.day}'
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         # Get the raw response text
#         response_text = response.text
#         data = json.loads(response_text)
#         #print(data)
#         if data:
#             day_df = pd.DataFrame(data)
#             df = pd.concat([df, day_df], ignore_index=True)
#         else:
#             print(" no data for this date")
#     else:
#         print("better luck next time")
    
#     time.sleep(1)


            
   
#     #current_date += datetime.timedelta(days=1)

# #df.to_csv('your_file_name2.csv', index=False)

# if not df2.empty and 'obsDt' in df.columns:
#     df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

# df2.to_csv(filepath, index=False)
# print("Data saved to ebird_dixon_observations.csv")