import pandas as pd

df = pd.read_csv("dataset/traffic.csv")

print(df.head())

print(df.info())

print(df.describe())