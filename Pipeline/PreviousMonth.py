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









def dataFetcher(last_month, previous_days, current_year):

	locations = {
	"L1025768":	"FDR",
	"L1069194":	"PhiladelphiaNavalYard",
	"L1145863":	"WissahickonValley",
	"L3041917":	"DixonMeadowPreserve",
	"L504403":	"JohnHeinz"
	}


	string_month = str(last_month)
	string_year = str(current_year)
	csv_file_name =  f"{string_month}{string_year}.csv"
	# path = '/Users/raulbazan/Desktop/BirdData/HistoricalData/NewData' + '/' + csv_file_name + '.csv'
	#print(path)
	output_dir = Path('/Users/raulbazan/Projects/BirdTracker/Data/UncleanedData')

	filepath = output_dir / csv_file_name
	
	df = pd.DataFrame()
	
	client_api = os.getenv('API_KEY')

	print(previous_days)

	# Set the API key in the request headers
	headers = {
        'X-eBirdApiToken': client_api
    }
    # For loop to iterate through the days of the previous month and create a csv file with the historic data
	for location in locations:
		for i in range(1, previous_days + 1):
			url = f"https://api.ebird.org/v2/data/obs/{location}/historic/{current_year}/{last_month}/{i}"
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
					print(" no data for this date" , " ", location , " " , i)
			else:
				print("better luck next time ", location, response.status_code)
	    
			time.sleep(1)



	if not df.empty and 'obsDt' in df.columns:
		df['obsDt'] = pd.to_datetime(df['obsDt'], errors='coerce')

	#output_dir = Path('/Users/raulbazan/Projects/BirdTracker/Data/UncleanedData')
	#filepath = output_dir + csv_file_name
	#df.to_csv(filepath, index=False)
	df.to_csv(filepath, index=False)
#Get previous month and days to get data from previous month. 
# for locationId,locationName  in locations.items():







if __name__ == "__main__":
	today = datetime.date.today()
	first = today.replace(day=1)
	last_month = first - datetime.timedelta(days=1)
	previous_month = last_month.month
	previous_days = last_month.day
	current_year = last_month.year
	dataFetcher(previous_month, previous_days, current_year)

