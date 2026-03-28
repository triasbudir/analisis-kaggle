import pandas as pd
import matplotlib.pyplot as plt

# Load data
print("Loading data...")
df = pd.read_csv('powerconsumption.csv')
print(f"Total data: {len(df):,} baris")
print(f"Kolom: {df.columns.tolist()}")
print(f"\n5 data pertama:")
print(df.head())
print(f"\nStatistik dasar:")
print(df.describe())
