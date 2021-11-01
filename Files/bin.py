import pandas as pd

df=pd.read_csv('.\Files\Chennai.csv')

print(df.columns)

print(len(df.columns))

for i in df.columns:
    print(i)