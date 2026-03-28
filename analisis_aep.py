import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
print("Loading data...")
df = pd.read_csv('AEP_hourly.csv')
print(f"Total data: {len(df):,} baris")
print(f"Kolom: {df.columns.tolist()}")
print(f"\n5 data pertama:")
print(df.head())
print(f"\nInfo dataset:")
print(df.info())
print(f"\nStatistik dasar:")
print(df.describe())
