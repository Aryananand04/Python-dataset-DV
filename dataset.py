import pandas as pd

# Load the datasets
file1_path = '/Users/aryananand/Desktop/archive/Unemployment in India.csv'
file2_path = '/Users/aryananand/Desktop/archive/Unemployment_Rate_upto_11_2020.csv'

data1 = pd.read_csv(file1_path)
data2 = pd.read_csv(file2_path)

# Strip leading and trailing spaces from column names
data1.columns = data1.columns.str.strip()
data2.columns = data2.columns.str.strip()

# Display the cleaned columns
print("Columns of data1:")
print(data1.columns)
print("\nColumns of data2:")
print(data2.columns)


# Merge datasets on common columns
merged_data = pd.merge(data1, data2, on=['Region', 'Date', 'Frequency', 'Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)'], how='outer')

# Display the first few rows of the merged dataset to verify
print(merged_data.head())

# Save the merged dataset to a new CSV file
merged_data.to_csv('/Users/aryananand/Desktop/archive/Merged_Unemployment_Data.csv', index=False)
