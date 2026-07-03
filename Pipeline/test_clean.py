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
from previousMonth import dataFetcher

if __name__ == "__main__":


    today = datetime.date.today()
    first = today.replace(day = 1)
    last_month = first - datetime.timedelta(days=1)
    
    previous_month = last_month.month
    previous_days = last_month.day
    current_year = last_month.year

    df = dataFetcher(previous_month, previous_days, current_year)
    print(df)
