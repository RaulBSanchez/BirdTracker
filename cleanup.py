import pandas as pd
import os
from pathlib import Path

def getCsvFiles(path):
    try:
        directory = Path(path)
        for file in directory.iterdir():
            if file.is_file() and file.suffix == ".csv":
                dataFrameCreator(file)  # filename without .csv
                #dataframes[df_name] = pd.read_csv(file)
    except FileNotFoundError:
        print("No files found.")
    except Exception as e:
        print(f"Error: {e}")
    
    #return dataframes

def dataFrameCreator(file):
	df = pd.read_csv(file)
	string_path = str(file)
	csv_name = string_path.split("/")[-1]
	

	
	df['birdCount'] = df['howMany'].astype('Int64')
	df = df.drop(['obsValid', 'obsReviewed', 'locationPrivate', 'exoticCategory', 'subId', 'howMany'], axis=1)
	df['obsDt'] = pd.to_datetime(df['obsDt'], format='%Y-%m-%d %H:%M:%S') 
	df = df.dropna()
	df = df[df['birdCount'] <= 75]
	df = df.reset_index(drop=True)



	sql_order = ['speciesCode', 'comName', 'sciName', 'locId', 'locName', 'obsDt','birdCount', 'lat',
       'lng']
      

	df = df[sql_order]
	#print("removed parameters")
	#print(df)

	
	target_path = '/Users/raulbazan/Desktop/CleanData/DixonMeadowPreserve/2023/' + csv_name
	cleandatapath = Path(target_path)
	#print(target_path)
	try: 
		df.to_csv(cleandatapath, index=False)
		print("Moved to clean data")
	except:
		print("didnt work")
		#print(target_path)


directory_path = "/Users/raulbazan/Desktop/HistoricalData/DixonMeadowPreserve/2023/"
#target_path = "/Users/raulbazan/Desktop/CleanData/DixonMeadowPreserve/2024"
dfs = getCsvFiles(directory_path)

# Example: view one
#print(dfs['April2025'].head())
