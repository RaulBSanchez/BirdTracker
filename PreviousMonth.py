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
today = datetime.date.today()
first = today.replace(day=1)
last_month = first - datetime.timedelta(days=1)
previous_month = last_month.month
#print(today, first, last_month)



locations = {
	"L1025768":	"Franklin Delano Roosevelt (FDR) Park"
	"L1069194":	"Philadelphia Naval Yard (restricted access)"
	"L1145863":	"Wissahickon Valley Park--Houston Meadow"
	"L3041917":	"Dixon Meadow Preserve"
	"L504403":	"John Heinz NWR--impoundment (Philadelphia Co.)"
}