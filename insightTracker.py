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


# this this where the CHANNEL ID comes from
def doingChannelID():
    while True:
        # need to check how long the ID is
        input1 = input("Please Enter the channelID, No:")
        input2 = input("Please Enter the channelID, No Again:")

        if input1 != input2:
            print(
                RED
                + "They do not match \n"
                + YELLOW
                + "!Please Enter the channel ID again!"
                + RESET
            )
        else:
            break
    channelID = input1
    return channelID


# This piece of code runs @ the start when the API key has not been added
def gettingAPIkeyFromUser():
    # This loops to make sure that the person puts in the correct key
    while True:
        intake1 = input("Please enter in your API key:")
        intake2 = input("Please enter in your API key again:")

        if intake1 != intake2:
            print(
                RED
                + "They do not match \n"
                + YELLOW
                + "!Please Enter the API key again!"
                + RESET
            )
        else:
            APIkey = intake1
            break

    return APIkey


# This piece of code checks for an API key, if they don exist another code will be run
def checkAPIkey():
    # ChatGPT told me to do this part
    # This check for the existance of the APIkey which is in a seperate CSV file
    if os.path.exists("APIkey.csv"):
        with open("APIkey.csv", "r") as file:
            APIkey = file.readline()
            file.close()

    # This creates a new file for the API key
    else:
        getAPIkey = gettingAPIkeyFromUser()
        APIkey = getAPIkey
        print("ad" + APIkey)
        with open("APIkey.csv", "w") as file:
            writingAPIkey = file.writelines(APIkey)
        file.close()
    print(APIkey)
    return APIkey


def getFromCloud(APIkey):
    resp = requests.get(APIkey)
    resultsFromCloud = json.loads(resp.text)


def main():
    writeAPIkey = checkAPIkey()
    print(writeAPIkey)
    # infoFromCloud = getFromCloud(APIkey)


# DONOT ADD ANYTHING ELSE UNDER THIS
main()
