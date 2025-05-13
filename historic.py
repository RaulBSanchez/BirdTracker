import requests
import json
from dotenv import load_dotenv, dotenv_values 
import os
import pandas as pd
import datetime
from time import sleep
load_dotenv()

START_DATE = datetime.date(2025, 4, 23)
END_DATE = datetime.date(2025, 4, 26)



# URL for hotspot data
#url = 'https://api.ebird.org/v2/data/obs/L3041917/historic/2025/04/17'
client_api = os.getenv('API_KEY')


# Set the API key in the request headers
headers = {
    'X-eBirdApiToken': client_api
}

# Send GET request to fetch hotspots
#response = requests.get(url, headers=headers)

bird_count = {
    
}

current_date = START_DATE
# url = "https://api.ebird.org/v2/data/obs/{{regionCode}}/historic/{{y}}/{{m}}/{{d}}"

for i in range((END_DATE - START_DATE).days + 1):
    current_date = START_DATE + datetime.timedelta(days=i)
    print(current_date)
    url = f'https://api.ebird.org/v2/data/obs/L3041917/historic/{current_date.year}/{current_date.month}/{current_date.day}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Get the raw response text
        response_text = response.text
        data = json.loads(response_text)
        print(type(data))
    
        for x in data:
            # print(x["comName"])
            # print(x["howMany"])

            #if bird doesnt exist, create a key 

            # if x["comName"] not in bird_count.keys():
            #     bird_count[x["comName"]] = x.get("howMany", 0)
        

            # else: 
            #     bird_count[x["comName"]] += x.get("howMany", 0)
            print(x)


            
    else:
        print("no good")
    #current_date += datetime.timedelta(days=1)

