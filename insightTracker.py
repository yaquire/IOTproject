# This is the files used that runs the Insight Tracker
import time
import requests
import os
import json


# ChatGPT gave me the values for this color parts & told me how to add colour
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


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
            itemSubstance = file.readline()
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


def main():
    APIkey = "APIkey"
    ChannelID = "ChannelID"
    writeAPIkey = checkItem(APIkey)
    actualChannelID = checkItem(ChannelID)

    print(actualChannelID)
    print(writeAPIkey)
    # infoFromCloud = getFromCloud(APIkey)


# DONOT ADD ANYTHING ELSE UNDER THIS
main()
