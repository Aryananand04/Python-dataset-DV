import pandas as pd
import numpy as np

# Load the datasets
data1 = pd.read_csv('/Users/aryananand/Desktop/archive/Unemployment in India.csv')
data2 = pd.read_csv('/Users/aryananand/Desktop/archive/Unemployment_Rate_upto_11_2020.csv')

# Strip leading and trailing spaces from column names
data1.columns = data1.columns.str.strip()
data2.columns = data2.columns.str.strip()

# Check the unique values in the 'Date' columns to identify any problematic formats
print("Unique Dates in data1:")
print(data1['Date'].unique())
print("\nUnique Dates in data2:")
print(data2['Date'].unique())

# Convert 'Date' to datetime for easier manipulation, with error handling
data1['Date'] = pd.to_datetime(data1['Date'], format='%d-%m-%Y', errors='coerce')
data2['Date'] = pd.to_datetime(data2['Date'], format='%d-%m-%Y', errors='coerce')

# Identify rows where 'Date' conversion failed
data1_invalid_dates = data1[data1['Date'].isna()]
data2_invalid_dates = data2[data2['Date'].isna()]

print("\nInvalid Dates in data1:")
print(data1_invalid_dates)
print("\nInvalid Dates in data2:")
print(data2_invalid_dates)

# Remove rows with invalid 'Date' values
data1 = data1.dropna(subset=['Date'])
data2 = data2.dropna(subset=['Date'])

# Merge datasets on common columns
merged_data = pd.merge(data1, data2, on=['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)'], how='outer')

# Extract year, month, and quarter from 'Date'
merged_data['Year'] = merged_data['Date'].dt.year
merged_data['Month'] = merged_data['Date'].dt.month
merged_data['Quarter'] = merged_data['Date'].dt.quarter

# Add season based on month
season_dict = {12: 'Winter', 1: 'Winter', 2: 'Winter',
               3: 'Spring', 4: 'Spring', 5: 'Spring',
               6: 'Summer', 7: 'Summer', 8: 'Summer',
               9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}
merged_data['Season'] = merged_data['Month'].map(season_dict)

# Add dummy data for new attributes
np.random.seed(42)  # For reproducibility

# Urban/Rural classification
merged_data['Urban/Rural'] = np.random.choice(['Urban', 'Rural'], size=len(merged_data))

# Dummy data for GDP growth rate, Population density, Education level, Industry employment rate, Gender employment rate
merged_data['GDP Growth Rate (%)'] = np.random.uniform(2, 10, size=len(merged_data))
merged_data['Population Density (per sq km)'] = np.random.uniform(100, 5000, size=len(merged_data))
merged_data['Education Level'] = np.random.choice(['Primary', 'Secondary', 'Tertiary'], size=len(merged_data))
merged_data['Industry Employment Rate (%)'] = np.random.uniform(10, 50, size=len(merged_data))
merged_data['Gender Employment Rate (Female %)'] = np.random.uniform(30, 70, size=len(merged_data))

# Display the first few rows of the enriched dataset
print(merged_data.head())

# Save the enriched dataset to a new CSV file
merged_data.to_csv('/Users/aryananand/Desktop/archive/Enriched_Unemployment_Data.csv', index=False)
