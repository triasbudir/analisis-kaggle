import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load & preprocessing
df = pd.read_csv('powerconsumption.csv')
df['Datetime'] = pd.to_datetime(df['Datetime'])
df['jam'] = df['Datetime'].dt.hour
df['bulan'] = df['Datetime'].dt.month
df['hari'] = df['Datetime'].dt.dayofweek
df['total_power'] = df['PowerConsumption_Zone1'] + df['PowerConsumption_Zone2'] + df['PowerConsumption_Zone3']

print("=== ANALISIS POWER CONSUMPTION MOROCCO ===")
print(f"Periode: {df['Datetime'].min()} s/d {df['Datetime'].max()}")
print(f"Total data: {len(df):,} records")
print(f"\nRata-rata suhu: {df['Temperature'].mean():.1f}°C")
print(f"Rata-rata kelembaban: {df['Humidity'].mean():.1f}%")
print(f"\nTotal konsumsi rata-rata: {df['total_power'].mean():,.0f} kWh")
print(f"Zone 1 rata-rata: {df['PowerConsumption_Zone1'].mean():,.0f} kWh")
print(f"Zone 2 rata-rata: {df['PowerConsumption_Zone2'].mean():,.0f} kWh")
print(f"Zone 3 rata-rata: {df['PowerConsumption_Zone3'].mean():,.0f} kWh")

# Korelasi suhu vs konsumsi
korelasi = df['Temperature'].corr(df['total_power'])
print(f"\nKorelasi Suhu vs Total Konsumsi: {korelasi:.3f}")
print("(1.0 = korelasi sempurna, 0 = tidak ada korelasi)")

# Buat grafik
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Analisis Power Consumption Morocco 2017', fontsize=14, fontweight='bold')

# Grafik 1: Konsumsi per zona
zona_avg = [df['PowerConsumption_Zone1'].mean(), 
            df['PowerConsumption_Zone2'].mean(),
            df['PowerConsumption_Zone3'].mean()]
axes[0,0].bar(['Zone 1', 'Zone 2', 'Zone 3'], zona_avg, color=['steelblue','orange','green'])
axes[0,0].set_title('Rata-rata Konsumsi per Zona')
axes[0,0].set_ylabel('kWh')

# Grafik 2: Pola per jam
jam_df = df.groupby('jam')['total_power'].mean()
axes[0,1].plot(jam_df.index, jam_df.values, color='red', marker='o', linewidth=2)
axes[0,1].fill_between(jam_df.index, jam_df.values, alpha=0.3, color='red')
axes[0,1].set_title('Pola Konsumsi per Jam')
axes[0,1].set_xlabel('Jam')
axes[0,1].set_ylabel('kWh')
axes[0,1].set_xticks(range(0, 24))

# Grafik 3: Korelasi suhu vs konsumsi
axes[0,2].scatter(df['Temperature'], df['total_power'], alpha=0.05, color='purple', s=1)
axes[0,2].set_title(f'Korelasi Suhu vs Konsumsi\n(r={korelasi:.3f})')
axes[0,2].set_xlabel('Suhu (°C)')
axes[0,2].set_ylabel('Total Konsumsi (kWh)')

# Grafik 4: Konsumsi per bulan
bulan_df = df.groupby('bulan')['total_power'].mean()
nama_bulan = ['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agu','Sep','Okt','Nov','Des']
axes[1,0].bar(nama_bulan, bulan_df.values, color='steelblue')
axes[1,0].set_title('Rata-rata Konsumsi per Bulan')
axes[1,0].set_ylabel('kWh')
axes[1,0].tick_params(axis='x', rotation=45)

# Grafik 5: Suhu per bulan
suhu_df = df.groupby('bulan')['Temperature'].mean()
axes[1,1].plot(nama_bulan, suhu_df.values, color='orange', marker='o', linewidth=2)
axes[1,1].fill_between(range(12), suhu_df.values, alpha=0.3, color='orange')
axes[1,1].set_title('Rata-rata Suhu per Bulan')
axes[1,1].set_ylabel('°C')
axes[1,1].tick_params(axis='x', rotation=45)

# Grafik 6: Konsumsi per hari
hari_df = df.groupby('hari')['total_power'].mean()
nama_hari = ['Sen','Sel','Rab','Kam','Jum','Sab','Min']
colors = ['steelblue']*5 + ['coral']*2
axes[1,2].bar(nama_hari, hari_df.values, color=colors)
axes[1,2].set_title('Rata-rata Konsumsi per Hari')
axes[1,2].set_ylabel('kWh')

plt.tight_layout()
plt.savefig('analisis_power.png', dpi=150)
print("\nGrafik tersimpan sebagai analisis_power.png")
