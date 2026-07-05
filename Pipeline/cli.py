#from cleanup import testCleanUp
# from database import testDataBase
# from previousMonth import testPrevious
# from historic import testHistory
import datetime
from historic import fetch_historic_data
from pathlib import Path
from config import CLEAN_DATA_DIR, UNCLEAN_DATA_DIR
from DailyFetch import daily_fetch
from previousMonth import dataFetcher

def locationSelector():
    locations = {
    1: ["L1025768", "FDR"],
    2: ["L1069194" ,"Philadelphia Naval Yard"],
    3: ["L1145863", "Wissahickon Valley"],
    4: ["L3041917", "Dixon Meadow Preserve"],
    5: ["L504403",  "John Heinz"]
    }
    

    print("Please select a location to the historical data for")

    for key, val in locations.items():
        print(f" {key} : {val[1]}")
    
    while True:    
        try:
            locationValue = int(input("Enter number: "))        
            #print(locationTag, "from selector")
            if locationValue in locations:
                locationTag = locations[locationValue][0]
                locationName = locations[locationValue][1]
                break
            else:
                print(f"{locationValue}, was not a valid choice")

        except ValueError:
            print("Pleaes select a number")

    return locationTag, locationName

def selectYear():
    years = (2020, 2021, 2022, 2023, 2024, 2025, 2026)
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

    return year


def dateRange(year):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    return start_date, end_date

def save_monthly_csvs(monthly_data, location_tag, year, locationName):
    output_dir = Path('/Users/raulbazan/Projects/BirdTracker/Data/UncleanedData')
    name = locationName.replace(" " , "")
    for month_key, df in monthly_data.items():
        if not df.empty:
            filename = f"{name}_{month_key}.csv"
            filepath = output_dir / filename

            df.to_csv(filepath, index=False)

def save_prev_month(df, month, year):
    output_dir = Path('/Users/raulbazan/Projects/BirdTracker/Data/UncleanedData')
    if not df.empty:
        filename = f"{month}_{year}.csv"
        filepath = output_dir / filename

        df.to_csv(filepath, index=False)



def save_daily_csvs(df, month, day):
    if not df.empty:
        filename = f"{month}_{day}.csv"
        filepath = output_dir / filename

        df.to_csv(filepath, index=False)

def historic_save(df, locationName, year):
    output_dir = Path('/Users/raulbazan/Projects/BirdTracker/Data/UncleanedData')

    if not df.empty:
        filename = f"{locationName}_{year}.csv"
        filepath = output_dir / filename

        df.to_csv(filepath, index=False)

def main():


    options = {
        1: "Daily Fetch",
        2: "Monthly Fetch",
        3: "Historical Fetch"
    }

    for key, val in options.items():
        print(f" {key} : {val}")


    

    while True:
        try:
            selection = int(input("Enter a number"))
            #print(selection)
            if selection == 1:
                print("option 1")
                daily_df, month, day = daily_fetch()
                save_daily_csvs(daily_df, month, day)
                break
            elif selection == 2:
                print("option two")
                #return df, previous_month, current_year
                df, month, year = dataFetcher()
                save_prev_month(df, month, year)

               
                break
            elif selection == 3:
                print("Historical Fetcher")
                locationTag, locationName = locationSelector()
                year = selectYear()
                monthly_data = fetch_historic_data(locationTag, year)
                historic_save(monthly_data, locationName, year)
                break
            else: 
                print("please enter a valid selection")
            
        except ValueError:
            print("Enter Valid Option")


    

main()
    