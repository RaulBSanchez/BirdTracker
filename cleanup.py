import pandas as pd
import os

#file_path = Path("/Users/raulbazan/Desktop/HistoricalData/DixonMeadowPreserve/2025/April2025.csv")

df = pd.read_csv("/Users/raulbazan/Desktop/HistoricalData/DixonMeadowPreserve/2025/April2025.csv")
print(df)


print(df.dtypes)

git config user.email "Raul.BazanSanchez@gmail.com"

2025-04-30 08:33:00

df['Mycol'] = pd.to_datetime(df['Mycol'], format='%Y%m%d:%H:%M:%S')

'%Y%d%d:%H:%M:%S'