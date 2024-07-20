import csv
import datetime
import os
# Function to generate example data
def generate_data(num_entries):
    data = [
    ["3", "43", "32", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    ["4", "23", "12", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    ["6", "3", "41", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    ["5", "8", "5", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    ["7", "64", "63", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    ]
    #Amount_of_Sales = Function()
    #Income_earned = Function()
    #Left_InStock = Function()
   # for i in range(1, num_entries + 1): 
        # Sample data categories
       # category1 = Amount_of_Sales{i}
       # category2 = Income_earned{i}
      #  category3 = Left_InStock{i}
        # Generate a timestamp for each entry
      #  timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Add data entry
      #  data.append([category1, category2, category3, timestamp])
    print (data)
    return data

# Write data to CSV file
def write_to_csv(file_name, data):
    headers = ['Amount_of_Sales', 'Income_earned', 'Left_InStock', 'Timestamp']
    #Check if file path exists
    file_exists = os.path.isfile(file_name) 
    with open(file_name, 'w', newline='') as file:
        
        writer = csv.writer(file)
        if not file_exists:

            writer.writerow(headers)
        writer.writerows(data)

# Example usage
num_entries = 10  # Number of entries to generate
file_name = 'categorized_data_with_headers.csv'
data = generate_data(num_entries)
write_to_csv(file_name, data)

print(f"Data written to {file_name}")
