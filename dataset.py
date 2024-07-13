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
