import requests
import json
from dotenv import load_dotenv, dotenv_values 
import os
load_dotenv()

# URL for hotspot data
url = 'https://api.ebird.org/v2/data/obs/L3041917/historic/2025/04/17'
client_api = os.getenv('API_KEY')


# Set the API key in the request headers
headers = {
    'X-eBirdApiToken': client_api
}

# Send GET request to fetch hotspots
response = requests.get(url, headers=headers)


# url = "https://api.ebird.org/v2/data/obs/{{regionCode}}/historic/{{y}}/{{m}}/{{d}}"

if response.status_code == 200:
    # Get the raw response text
    response_text = response.text
    data = json.loads(response_text)
    print(type(data))
    
    for x in data:

        #print("common name:",  x["comName"])
        #print("Count:", x["howMany"])
        print(x)
else:
    print("no good")