import pandas as pd
import os
from pathlib import Path


# csv_files = list(Path("/Users/raulbazan/Desktop/HistoricalData/DixonMeadowPreserve/2025").glob("*.csv"))

# for x in csv_files:
# 	print(x)



from pathlib import Path
import pandas as pd

def getCsvFiles(path):
    try:
        directory = Path(path)
        for file in directory.iterdir():
            if file.is_file() and file.suffix == ".csv":
                dataFrameCreator(file, directory)  # filename without .csv
                #dataframes[df_name] = pd.read_csv(file)
    except FileNotFoundError:
        print("No files found.")
    except Exception as e:
        print(f"Error: {e}")
    
    #return dataframes

def dataFrameCreator(file, directory):
	df = pd.read_csv(file)
	df['birdCount'] = df['howMany'].astype('Int64')
	df = df.drop(['obsValid', 'obsReviewed', 'locationPrivate', 'exoticCategory', 'subId', 'howMany'], axis=1)
	df['obsDt'] = pd.to_datetime(df['obsDt'], format='%Y-%m-%d %H:%M:%S') 
	df = df.dropna(axis=0, subset=['birdCount'])
	df = df.reset_index(drop=True)
	print(df)

	



directory_path = "/Users/raulbazan/Desktop/HistoricalData/DixonMeadowPreserve/2025/"
dfs = getCsvFiles(directory_path)

# Example: view one
#print(dfs['April2025'].head())
