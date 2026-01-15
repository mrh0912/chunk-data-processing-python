import pandas as pd
from config import RAW_DATA_PATH

df = pd.read_csv(RAW_DATA_PATH, nrows=5)
print(df.head())
print(df.columns)
