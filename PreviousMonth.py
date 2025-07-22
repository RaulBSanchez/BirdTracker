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


# Get the last month in order to get previous months birding data
# today = datetime.date.today()
# first = today.replace(day=1)
# last_month = first - datetime.timedelta(days=1)
# previous_month = last_month.month
# previous_days = last_month.day
# current_year = last_month.year
# print(current_year)



locations = {
	"L1025768":	"Franklin Delano Roosevelt (FDR) Park",
	"L1069194":	"Philadelphia Naval Yard (restricted access)",
	"L1145863":	"Wissahickon Valley Park--Houston Meadow",
	"L3041917":	"Dixon Meadow Preserve",
	"L504403":	"John Heinz NWR--impoundment (Philadelphia Co.)"
}






def dataFetcher(last_month, previous_days, current_year, locationId, locationName):
	print("from data dataFetcher")
	print(last_month, previous_days, current_year, locationId, locationName)
	string_month = str(last_month)
	string_year = str(current_year)
	#print(string_year, string_month)
	csv_file_name = locationName + string_month + string_year
	path = '/Users/raulbazan/Desktop/testdata' + '/' + csv_file_name + '.csv'
	print(path)
	filepath = Path(path)
	# month = month_name
	# year = year
	df = pd.DataFrame()

	client_api = os.getenv('API_KEY')

   

# Set the API key in the request headers
	headers = {
        'X-eBirdApiToken': client_api
    }
    #print(headers, client_api)

	for i in range(1, previous_days + 1):
	    #current_date = START_DATE + datetime.timedelta(days=i)
	    #print(current_date)
	    url = f"https://api.ebird.org/v2/data/obs/{locationId}/historic/{current_year}/{last_month}/{i}"
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
	            print(" no data for this date" , " ", last_month , " " , i)
	    else:
	        print("better luck next time")
	    
	    time.sleep(1)



	if not df.empty and 'obsDt' in df.columns:
		df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

	df.to_csv(filepath, index=False)


for locationId,locationName  in locations.items():

	
	today = datetime.date.today()
	first = today.replace(day=1)
	last_month = first - datetime.timedelta(days=1)
	previous_month = last_month.month
	previous_days = last_month.day
	current_year = last_month.year
	locationName = ''.join(e for e in locationName if e.isalnum())
	dataFetcher(previous_month, previous_days, current_year, locationId, locationName)


