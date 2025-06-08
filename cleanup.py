import pandas as pd
import os

#file_path = Path("/Users/raulbazan/Desktop/HistoricalData/DixonMeadowPreserve/2025/April2025.csv")

df = pd.read_csv("/Users/raulbazan/Desktop/HistoricalData/DixonMeadowPreserve/2025/April2025.csv")
print(df)


print(df.dtypes)