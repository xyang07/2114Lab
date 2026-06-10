import pandas as pd
import numpy as np
from scipy.signal import find_peaks

df = pd.read_csv("data.csv", skiprows=9, skipinitialspace=True)
df.columns = df.columns.str.strip()

print("Columns found:", df.columns.tolist())

time_col    = df.columns[0]
voltage_col = df.columns[1]

df = df[df[time_col] >= 0].reset_index(drop=True)

time = df[time_col].values
voltage = df[voltage_col].values

peaks, _ = find_peaks(voltage, prominence=0.1)

print(f"{'#':<6} {'Time (s)':<18} {'Voltage (V)'}")
for i, p in enumerate(peaks):
    print(f"{i:<6} {time[p]:<18.6e} {voltage[p]:.4f}")
