import pandas as pd

# Load data1 and data2
try:
    data1 = pd.read_csv('/Users/aryananand/Desktop/archive/Unemployment in India.csv', parse_dates=['Date'], dayfirst=True)
    data2 = pd.read_csv('/Users/aryananand/Desktop/archive/Unemployment_Rate_upto_11_2020.csv', parse_dates=['Date'], dayfirst=True)
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Displaying first few rows of each dataset to verify columns
print("\nFirst few rows of data1:")
print(data1.head())

print("\nFirst few rows of data2:")
print(data2.head())

# Cleaning data1
try:
    print("\nInvalid Dates in data1:")
    invalid_data1 = data1[data1['Date'].isnull()]
    print(invalid_data1)
except KeyError as e:
    print(f"Error cleaning data1: {e}")

# Cleaning data2
try:
    print("\nInvalid Dates in data2:")
    invalid_data2 = data2[data2['Date'].isnull()]
    print(invalid_data2)
except KeyError as e:
    print(f"Error cleaning data2: {e}")

# Drop rows with NaN dates (if any)
data1 = data1.dropna(subset=['Date']).reset_index(drop=True)
data2 = data2.dropna(subset=['Date']).reset_index(drop=True)

# Merge data1 and data2 on 'Region' and 'Date'
try:
    merged = pd.merge(data1, data2, on=['Region', 'Date'], how='inner')
    print("\nMerged data:")
    print(merged.head())
except Exception as e:
    print(f"Error merging data: {e}")

# Add dummy data in enriched (example)
try:
    enriched = merged.copy()
    enriched['Dummy_Column'] = '#####'
    print("\nEnriched data:")
    print(enriched.head())
except Exception as e:
    print(f"Error enriching data: {e}")

# Optionally, you can save enriched data to a CSV file for further inspection
try:
    enriched.to_csv('/Users/aryananand/Desktop/Python data set/enriched_data.csv', index=False)
    print("\nEnriched data saved successfully.")
except Exception as e:
    print(f"Error saving enriched data: {e}")
