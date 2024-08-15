# This is the files used that runs the Insight Tracker
import time
import requests
import os
import json
import csv
import RPi.GPIO as GPIO # type: ignore
import time
from datetime import datetime

# Define the GPIO pins
TRIG_PIN = 25
ECHO_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN,GPIO.OUT) #GPIO25 as Trig
GPIO.setup(ECHO_PIN,GPIO.IN) #GPIO27 as Echo

# ChatGPT gave me the values for this color parts & told me how to add colour
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Variables
csvfile = os.path.join(os.getcwd(), 'IOTproject/test')
people_count = 0
count = 0
last_detection_time = 0
detection_cooldown = 2
current_minute = datetime.now().minute 
feeds = 0
# This piece of code runs @ the start when the API key has not been added
# Here the item is the the same as the item from the chunk of code below
def gettingItemFromUser(item):
    # filePath = f"{item}.csv"
    # This loops to make sure that the person puts in the correct key
    # This is simple error correction & might be developed further but I'll see

    while True:
        intake1 = input(f"Please enter in your {item}:")
        intake2 = input(f"Please enter in your {item} again:")
        # This  is an error message made with colors to make it more obvious
        if intake1 != intake2:
            print(
                RED
                + "They do not match \n"
                + YELLOW
                + f"!Please Enter the {item} key again!"
                + RESET
            )
        else:
            itemName = intake1
            break

    return itemName
    # This is returned back to the function below


# This piece of code checks for an API key, if they don exist another code will be run
def checkItem(item):
    # ChatGPT told me to do this part
    # This check for the existance of the APIkey which is in a seperate CSV file
    filePath = f"{item}.csv"
    if os.path.exists(filePath):
        with open(filePath, "r") as file:
            itemSubstance = file.readlines()
            file.close()

    # This creates a new file for the API key
    else:
        itemFromUser = gettingItemFromUser(item)
        itemSubstance = itemFromUser
        # print("ad" + APIkey)
        with open(filePath, "w") as file:
            writingFile = file.writelines(itemSubstance)
        file.close()
    return itemSubstance

def getFromCloud(APIkey):
    resp = requests.get(APIkey)
    resultsFromCloud = json.loads(resp.text)

def get_thingspeak_data(api_key, channel_id):
    URL = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results=8000'
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
def write_to_thingspeak(api_key, channel_id, data):

    formatedData = []
    needsToReplace = f'\n'
    for i in data:
        line = i.replace(needsToReplace,'')
        formatedData.append(line)
    print(formatedData)
    # Removes the \n behind each string
    processed_data = [row.split(',') for row in formatedData]
    # Splits each string into list of fields
    url = f"https://api.thingspeak.com/update?"
    for index,row in enumerate(processed_data):
        if index == 0 and not row[0].isdigit():
            print("Skipping header row.")
            continue 
        # Assuming your data rows contain fields that map directly to ThingSpeak fields
        payload = {
            "field1": row[0],
            "field6": row[1],
            "field7": row[2],
            "api_key": api_key
            # Add more fields as needed
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(GREEN + "Data written to ThingSpeak successfully." + RESET)
        else:
            print(RED + f"Failed to write data to ThingSpeak: {response.text}" + RESET)
            print('Response code:', response.status_code)
        
        # Add a delay to comply with ThingSpeak's rate limit (15 seconds per update)
        import time
        time.sleep(15)  # 15-second delay to meet rate limits

def Total_People():
    people = 0
    for feed in feeds:
        try:
            value = int(feed['field1'])
            people += value
        except (ValueError, TypeError):
            print(f"Skipping invalid entry: {feed['field1']}")
    return people

#Calculate data 
def Total_Orders():
    orders = 0
    for feed in feeds:
        try:
            value = int(feed['field2'])
            orders += value
        except (ValueError, TypeError):
            print(f"Skipping invalid entry: {feed['field2']}")
    return orders

# Function to generate data into csv file
def generate_data():

    while True: 
        # Sample data categories
        data = []
        category1 = PeopleCounter()
        category2 = Total_People()
        category3 = Total_Orders()
        # Generate a timestamp for each entry
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Add data entry
        data.append([category1, category2, category3, timestamp])
        print (data)
        return data
    
# Write the people count to the CSV file
def write_to_csv(file_path, data):
    filePath = f"{file_path}.csv"
    headers = ['Header', 'Number of People', 'No of Orders', 'Timestamp']
    try:
        with open(filePath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerow(data)
            print("Current working directory:", os.getcwd())
            print(f"Writing to CSV: No_of_People: {count}")
    except Exception as e:
        print(f"An error occurred while writing to the CSV file: {e}")

#Data written to CSV file every minute
def append_data_every_minute(file_path):
      while True:
          data = generate_data()
          write_to_csv(file_path, data)
          now = datetime.datetime.now()
          next_minute = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
          sleep_time = (next_minute - now).total_seconds()
        
          time.sleep(sleep_time)
        
def ultrasound():
        # Set TRIG_PIN high for 10 microseconds to trigger the measurement
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

        # Measure pulse width of the echo
    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time() #capture start of pulse
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time() #capture end of pulse

    # Calculate the distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Speed of sound is 34300 cm/s (17150 cm/s round trip)
    return round(distance, 2)


def PeopleCounter():
    global last_detection_time #declare last_detection_time as global
    global detection_cooldown  # 2 seconds cooldown
    global count
    global current_minute
    global people_count
    try:
        while True:
            distance = ultrasound()
            if distance is not None:
                print(f"Distance: {distance} cm")
            time.sleep(1)
            # Check if the distance is within the range of 5cm to 40cm
            if 1 <= distance <= 200:
                current_time = time.time()
                if current_time - last_detection_time > detection_cooldown:
                    count += 1
                    last_detection_time = current_time
                    print(f"Person detected! Total count: {count}")
                    return count
                time.sleep(0.1)  # Wait a bit before the next loop
    except KeyboardInterrupt:
     print("Measurement stopped by user")
     people_count = count
     GPIO.cleanup()
     return count

def main():
    writeAPIkey = checkItem(os.path.join(os.getcwd(), 'IOTproject/APIkey'))
    actualChannelID = checkItem(os.path.join(os.getcwd(), 'IOTproject/ChannelID'))
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
    append_data_every_minute(csvfile)
    print(os.getcwd())
    print(f"Data written to {csvfile}")
    time.sleep(0.1)  # Delay for 0.1s
    # Read the CSV file
    csv_data = checkItem(csvfile)
    print (csv_data)
    if csv_data:

        write_to_thingspeak(writeAPIkey, actualChannelID, csv_data)

    #print(actualChannelID)
    #print(writeAPIkey)
    # infoFromCloud = getFromCloud(APIkey)


# DONOT ADD ANYTHING ELSE UNDER THIS
main()
