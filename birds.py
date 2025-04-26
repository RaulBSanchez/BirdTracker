import requests
import json
from dotenv import load_dotenv, dotenv_values 
import os
load_dotenv()

# URL for hotspot data
url = 'https://api.ebird.org/v2/ref/hotspot/US-PA-101'
client_api = os.getenv('API_KEY')


# Set the API key in the request headers
headers = {
    'X-eBirdApiToken': client_api
}

# Send GET request to fetch hotspots
response = requests.get(url, headers=headers)

# Ensure the response is successful before proceeding
if response.status_code == 200:
    # Get the raw response text
    response_text = response.text
    
    # Initialize an empty list to store the parsed locations
    locations = []
    
    # Split the response text by newlines to get individual lines
    lines = response_text.strip().split("\n")

    # Iterate over each line
    for line in lines:
        # Split the line by commas to get individual components
        parts = line.split(",")
        
        # Extract the location ID and location name (assuming they're at specific positions)
        loc_id = parts[0]  # The first element is the location ID
        loc_name = parts[6]  # The seventh element is the location name
        
        # Store the result in the list as a dictionary
        locations.append({"Location ID": loc_id, "Location Name": loc_name})

    # Print the extracted locations
    for location in locations:
        print(location)
else:
    print(f"Failed to fetch hotspots. Status code: {response.status_code}")
