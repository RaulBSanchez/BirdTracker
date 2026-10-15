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
    years = tuple(range(2020, datetime.date.today().year + 1))
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





def save_csv(df, filename):
    if not df.empty:
        UNCLEAN_DATA_DIR.mkdir(parents=True, exist_ok=True)
        filepath = UNCLEAN_DATA_DIR / filename

        df.to_csv(filepath, index=False)
        print(f"Saved: {filepath}")

def save_prev_month(df, month, year):
    save_csv(df, f"monthly_{year}-{month:02d}.csv")


def save_daily_csvs(df, date):
    save_csv(df, f"daily_{date.isoformat()}.csv")

def historic_save(df, locationName, year):
    name = locationName.replace(" ", "")
    save_csv(df, f"{name}_{year}.csv")

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
            selection = int(input("Enter a number: "))
            #print(selection)
            if selection == 1:
                print("Running the daily run for all bird sightings around Philly")
                daily_df, date = daily_fetch()
                save_daily_csvs(daily_df, date)
                break
            elif selection == 2:
                print("Running the previous month run for all locations")
                df, month, year = dataFetcher()
                save_prev_month(df, month, year)

               
                break
            elif selection == 3:
                print("Running the historical fetcher, please select the location and year")
                locationTag, locationName = locationSelector()
                year = selectYear()
                historic_df = fetch_historic_data(locationTag, year)
                historic_save(historic_df, locationName, year)
                break
            else: 
                print("please enter a valid selection")
            
        except ValueError:
            print("Enter Valid Option")


    
if __name__ == "__main__":
    main()
    