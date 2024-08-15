import csv
import datetime
import os
import time
import requests


# Replace these with your channel ID and API key
CHANNEL_ID = '2551972'
READ_API_KEY = 'QEZ5RSS1HY0SUT6T'
URL = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=8000'

def get_thingspeak_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def Total_People():
    people = 0
    for feed in feeds:
        try:
            value = int(feed['field1'])
            people += value
        except (ValueError, TypeError):
            print(f"Skipping invalid entry: {feed['field1']}")
    return people

def Total_Orders():
    orders = 0
    for feed in feeds:
        try:
            value = int(feed['field2'])
            orders += value
        except (ValueError, TypeError):
            print(f"Skipping invalid entry: {feed['field2']}")
    return orders
# Function to generate example data
def generate_data():

    while True: 
        # Sample data categories
        data = []
        category1 = ('-')
        category2 = Total_People()
        category3 = Total_Orders()
        # Generate a timestamp for each entry
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Add data entry
        data.append([category1, category2, category3, timestamp])
        print (data)
        return data

# Write data to CSV file
def write_to_csv(file_name, data):
    headers = ['Header', 'Total People', 'Total Orders', 'Timestamp']
    file_name = f"{file_name}.csv"
    #Check if file path exists
    if os.path.exists(file_name): 
      with open(file_name, 'w', newline='') as file:
          writer = csv.writer(file)
          writer.writerow(headers)
          writer.writerow(data)

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



data = get_thingspeak_data()
if data:
        feeds = data.get('feeds', [])
        for feed in feeds:
            print(f"Entry ID: {feed['entry_id']}")
            print(f"Field1: {feed['field1']}")
            print(f"Field2: {feed['field2']}")
            # Add more fields if needed
            print("----")
        else:
             print("No data retrieved.")
data = generate_data()
file_name = os.path.join(os.getcwd(), 'IOTproject/test')
append_data_every_minute(file_name)
print(os.getcwd())
print(f"Data written to {file_name}")