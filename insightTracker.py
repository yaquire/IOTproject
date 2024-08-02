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
TRIG_PIN = 23
ECHO_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN,GPIO.OUT) #use GPIO4 as Trig
GPIO.setup(ECHO_PIN,GPIO.IN) #use GPIO17 as Echo

# ChatGPT gave me the values for this color parts & told me how to add colour
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Variables
last_detection_time = 0 
detection_cooldown = 2  # 2 seconds cooldown
current_hour = datetime.now().hour 
csvfile = "test"


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


# Write the people count to the CSV file
def write_to_csv(file_path, hour, count):
    filePath = f"{file_path}.csv"
    try:
        with open(filePath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([hour, count])
    except Exception as e:
        print(f"An error occurred while writing to the CSV file: {e}")

def getFromCloud(APIkey):
    resp = requests.get(APIkey)
    resultsFromCloud = json.loads(resp.text)
    
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
            "field1": row[1],
            "field2": row[2],
            "field3": row[3],
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

def ultrasound(distance):
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

def PeopleCounter(count):
    try:
        while True:
            distance = ultrasound()
            if distance is not None:
                print(f"Distance: {distance} cm")

            # Check if the distance is within the range of 5cm to 40cm
            if 5 <= distance <= 40:
                current_time = time.time()
                if current_time - last_detection_time > detection_cooldown:
                    count += 1
                    last_detection_time = current_time
                    print(f"Person detected! Total count: {count}")

                    # Check if the hour has changed
            new_hour = datetime.now().hour
            if new_hour != current_hour:
                people_count = count
                # Write the count for the past hour to the CSV file
                write_to_csv(csvfile, current_hour, people_count)
                # Reset the people count for the new hour
                people_count = 0
                count = people_count
                # Update the current hour
                current_hour = new_hour

            time.sleep(0.1)  # Wait a bit before the next loop

    except KeyboardInterrupt:
     print("Measurement stopped by user")
     GPIO.cleanup()

def main():
    APIkey = "APIkey"
    ChannelID = "ChannelID"
    count = "count"
    writeAPIkey = checkItem(APIkey)
    actualChannelID = checkItem(ChannelID)
    PeopleCounter(count) 
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
