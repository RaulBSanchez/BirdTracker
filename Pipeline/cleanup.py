import pandas as pd
import os
from pathlib import Path

# def getCsvFiles(path):
#     try:
#         directory = Path(path)
#         for file in directory.iterdir():
#             if file.is_file() and file.suffix == ".csv":
#             	print(f"from getviles {file}")
#             	dataFrameCreator(file)
#             	#dataframes[df_name] = pd.read_csv(file)
#     except FileNotFoundError:
#         print("No files found.")
#     except Exception as e:
#         print(f"Error: {e}")
    
#     #return dataframes

# def dataFrameCreator(file):
# 	df = pd.read_csv(file)
# 	string_path = str(file)
# 	csv_name = string_path.split("/")[-1]
# 	print(f" csv name  {csv_name}")

	
# 	df['birdCount'] = df['howMany'].astype('Int64')
# 	df = df.drop(['obsValid', 'obsReviewed', 'locationPrivate', 'exoticCategory', 'subId', 'howMany'], axis=1)
# 	df['obsDt'] = pd.to_datetime(df['obsDt'], format='%Y-%m-%d %H:%M:%S') 
# 	df = df.dropna()
# 	df = df[df['birdCount'] <= 75]
# 	df = df.reset_index(drop=True)



# 	sql_order = ['speciesCode', 'comName', 'sciName', 'locId', 'locName', 'obsDt','birdCount', 'lat',
#        'lng']
      

# 	df = df[sql_order]
# 	#print("removed parameters")
# 	print(df)

	
# 	target_path = '/Users/raulbazan/Desktop/BirdData/CleanData/NewData/'  + csv_name
# 	print(target_path)
# 	cleandatapath = Path(target_path)
# 	print(f"cleandatapath: {cleandatapath}")
# 	#print(target_path)
# 	try: 
# 		df.to_csv(cleandatapath, index=False)
# 		print("Moved to clean data")
# 	except Exception as e:
# 		print("save failed", e)
# 		print("this didnt work", cleandatapath)


# directory_path = "/Users/raulbazan/Desktop/BirdData/HistoricalData/NewData/"
# #target_path = "/Users/raulbazan/Desktop/CleanData/DixonMeadowPreserve/2024"
# dfs = getCsvFiles(directory_path)

# Example: view one
#print(dfs['April2025'].head())

def testCleanUp():
	print("hello from cleanup")



if __name__ == "__main__":
    testCleanUp()
