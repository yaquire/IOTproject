# This is the files used that runs the Insight Tracker
import time
import requests
import os
import json
import csv
#import RPi.GPIO as GPIO # type: ignore
import time
from datetime import datetime




# ChatGPT gave me the values for this color parts & told me how to add colour
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Variables
csvfile = 'test'


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

def main():
    APIkey = 'APIkey'
    ChannelID= 'ChannelID'
    writeAPIkey = checkItem(APIkey)
    actualChannelID = checkItem(ChannelID)
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
