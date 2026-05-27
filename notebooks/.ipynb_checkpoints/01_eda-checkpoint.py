import pandas as pd
import numpy as np

df = pd.read_csv("/Users/aniketsawant/FraudDetection/fraud-detection-algorithm/data/raw/creditcard.csv")

print(df.shape)
print(df.columns)
print(df.head())
print(df.describe())
print(df.isna().sum())

