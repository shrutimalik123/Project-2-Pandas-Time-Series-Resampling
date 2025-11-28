import pandas as pd
import numpy as np

# Create a date range for 90 days (daily data)
dates = pd.date_range(start='2025-01-01', periods=90, freq='D')

# Create a corresponding array of simulated temperature readings
# (e.g., daily average temperatures with some noise)
np.random.seed(42) # for reproducible results
data = np.random.normal(loc=15, scale=5, size=90)

# Create the DataFrame
df = pd.DataFrame({'Temperature_C': data}, index=dates)

print("--- Original Daily Data (First 5 Rows) ---")
print(df.head())

# Verify that the index is a DatetimeIndex
print("\n--- Index Check ---")
print(f"Index type: {type(df.index)}")
print(f"Index dtype: {df.index.dtype}")

# Resample to Weekly Average Temperature
weekly_avg = df['Temperature_C'].resample('W').mean()

# Resample to Monthly Average Temperature
monthly_avg = df['Temperature_C'].resample('M').mean()

print("\n--- Weekly Average Temperature ---")
print(weekly_avg)

print("\n--- Monthly Average Temperature ---")
print(monthly_avg)

# Calculate the 7-day (weekly) rolling mean
df['7D_Rolling_Mean'] = df['Temperature_C'].rolling(window=7).mean()

print("\n--- Daily Data with 7-Day Rolling Mean (Last 5 Rows) ---")
# The first 6 rows will be NaN because 7 data points are needed to start the average
print(df.tail())
