import csv
import datetime
import os
import time


# Function to generate example data
def generate_data():
    # data = [
    # ["3", "43", "32", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    # ["4", "23", "12", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    # ["6", "3", "41", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    # ["5", "8", "5", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    # ["7", "64", "63", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
    # ]
    # Amount_of_Sales = Function()
    # Income_earned = Function()
    # Left_InStock = Function()
    while True:
        # Sample data categories
        category1 = ["-"]
        category2 = Amount_of_Sales()
        category3 = Income_earned()
        category4 = Left_InStock()
        # Generate a timestamp for each entry
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Add data entry
        data.append([category1, category2, category3, category4, timestamp])
        print(data)
        return data


# Write data to CSV file
def write_to_csv(file_name, data):
    headers = ['Header', 'Amount_of_Sales', 'Income_earned', 'Left_InStock', 'Timestamp']
    file_name = f"{file_name}.csv"
    # Check if file path exists
    if os.path.exists(file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

            time.sleep(0.1)  # Wait a bit before the next loop
    else:
        print(f"An error occurred while writing to the CSV file")


def append_data_every_minute(file_name):
    while True:
        data = generate_data()
        write_to_csv(file_name, data)
        now = datetime.datetime.now()
        next_minute = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
        sleep_time = (next_minute - now).total_seconds()

        time.sleep(sleep_time)


# Example usage
data = generate_data()
file_name = os.path.join(os.getcwd(), 'IOTproject/categorized')
append_data_every_minute(file_name)
print(os.getcwd())
print(f"Data written to {file_name}")
