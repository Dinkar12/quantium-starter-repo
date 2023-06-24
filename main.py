import pandas as pd

# Read and transform the CSV files
data_file1 = pd.read_csv('data/daily_sales_data_0.csv')
data_file1 = data_file1[data_file1['product'] == 'Pink Morsels']
data_file1['sales'] = data_file1['quantity'] * data_file1['price']

data_file2 = pd.read_csv('data/daily_sales_data_1.csv')
data_file2 = data_file2[data_file2['product'] == 'Pink Morsels']
data_file2['sales'] = data_file2['quantity'] * data_file2['price']

data_file3 = pd.read_csv('data/daily_sales_data_2.csv')
data_file3 = data_file3[data_file3['product'] == 'Pink Morsels']
data_file3['sales'] = data_file3['quantity'] * data_file3['price']

# Merge the DataFrames into a single DataFrame
merged_data = pd.concat([data_file1, data_file2, data_file3])

# Select the desired fields for the output file
output_data = merged_data[['sales', 'date', 'region']]

# Save the output data to a CSV file
output_data.to_csv('output.csv', index=False)
