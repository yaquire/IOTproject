# the code that works so far {}_{}


import csv
import json 
import random
import requests
import time


RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

def creatingUSERjson(data,randomID):
    json_string = json.dumps(data,indent=4)
    json_file_name = str(randomID)+'.json'
    with open(f'{json_file_name}','w') as json_file:
        json.dump(data, json_file, indent=4)

    return()


def write_ThingSpeak(data):
    data = data
    apiKEY = ''
    channelID =''
    filepath = 'APIkey.csv'
    with open(filepath, mode="r") as file:
        reed = file.readlines()
        apiKEY = reed[0]

    filepath = 'ChannelID.csv'
    with open(filepath, mode="r") as file:
        reed = file.readlines()
        channelID = reed[0]

    #field 2 ~ Number User 
    readTS = requests.get(f'https://api.thingspeak.com/channels/{channelID}/fields/2.json?results=1')
    numPPL = json.loads(readTS.text)
    
    number_of_Orders = (numPPL['feeds'][0]['field2'])
    if number_of_Orders == None: number_of_Orders = 1
    else: 
        number_of_Orders= int(number_of_Orders)
        number_of_Orders+=1
    #field 4 ~ Total Items Bought (Num)
    number_items = 0
    #field 5 ~ Total Bought ($)
    totalPurchase = 0
    for row in data:
        quant = row['Quantity']
        number_items+=int(quant)
        cost = row['Cost']
        totalPurchase+=float(cost)


    #print("apiKey: ",apiKEY)
    send_data = requests.get(f"https://api.thingspeak.com/update?api_key={apiKEY}&field4=%s&field5=%s&field2=%s" %(number_items,totalPurchase,number_of_Orders))
    time.sleep(20)
    print(send_data)
    return()

def checkout():
    data = []
    totalCost = 0

    filepath = 'Web Server/buyee.csv'
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
            totalCost += float(row['Cost'])

    # FOR CHECKOUT
    if data == []:
        print('No items, so no chackout')
    else:
        randomID = random.randint(10000, 99999)
        print('CUSTOMER ID:', randomID)
        # print(RED, data, RESET)
        #creatingUSERjsons = creatingUSERjson(data,randomID)
        writeTS =write_ThingSpeak(data)
    return ()

run = checkout()