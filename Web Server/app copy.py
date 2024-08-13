import threading
from flask import Flask, render_template, request, redirect, url_for, session

# import pandas as pd
import csv
import json
import random
import requests
import time

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'
app = Flask(__name__)


@app.route("/")
def index():
    # Check if data.csv exists
    data = []
    filepath = "Web Server/data.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)
    # if request.method == 'POST':
    #     for item in data:
    #         #print (item)
    #         #print(item["Name"])
    #         if  request.form['addingToCart'] == item["Name"]:
    #             print('works')
    #             namee=item['Name']
    #             writeC = writeCart(namee)
    return render_template("main.html", data=data)


### This is a test
def writeCart(name):
    name = name
    itemData = []
    filepath = 'Web Server/data.csv'
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row.pop('image-link')
            row.pop('Quantity')
            row.pop('Description')
            row.pop('Subtext')
            itemData.append(row)
    file.close()
    print(RED, itemData, RESET)

    data = []
    filepath = 'Web Server/buyee.csv'
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    file.close()
    # the below code written by Yaq
    rangeNo = []
    number = 0
    for i in range(len(data)):
        dictName = data[i]['Name']
        if name == dictName:
            # print(i,'In dict')
            rangeNo.append(i)
            number = i
        else:
            rangeNo.append('Not in Data')
    # print('RangeNo' , rangeNo)
    # i = index of the item (This is a local var)
    i = 0
    hasInteger = any(isinstance(x, int) for x in rangeNo)
    for x in rangeNo:
        if type(x) == int:
            i = x
    # print(RED,hasInteger,RESET)
    if hasInteger is False:
        row = {}
        row['Name'] = name
        row["Quantity"] = 1
        data.append(row)
    elif hasInteger is True:
        print('The index of the item is:', i)
        quant = int(data[i]['Quantity'])
        quant += 1
        data[i]['Quantity'] = quant
    else:
        print(RED + 'ERROR' + RESET)

    # This is taken from chatGPT
    indexsData = []
    indexsItemData = []
    for i in range(len(data)): indexsData.append(data[i]['Name'])
    for i in range(len(itemData)): indexsItemData.append(itemData[i]['Name'])
    matchingIndexforItem_data = [i for i, item in enumerate(indexsItemData) if item in indexsData]
    # ~~~#

    newData = []
    print(matchingIndexforItem_data)
    for i in range(len(data)):
        print(GREEN, data[i], RESET)
        mergeDict = {**itemData[(matchingIndexforItem_data[i])], **data[i]}
        newData.append(mergeDict)

    for row in newData:
        cost = int(row['Quantity']) * float(row['Price'])
        row['Cost'] = cost

    print(MAGENTA, newData, RESET)

    headers = list(newData[0].keys())
    print(headers)

    with open(filepath, mode="w+", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in newData:
            writer.writerow(row)

    # print(GREEN,data,RESET)
    return ()


# This works it from chatGPT
@app.route("/", methods=["POST"])
def add_to_cart():
    # print("Request method:", request.method)
    if "addingToCart" in request.form:
        buttonValue = request.form["addingToCart"]
        print("Button Value:", buttonValue)
        writerC = writeCart(buttonValue)
    return redirect(url_for("index"))


def changeCART(name, change):
    data = []
    filepath = 'Web Server/buyee.csv'
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    file.close()

    for row in data:
        print(row)
        if row['Name'] == name:
            if change == '+':
                quant = int(row['Quantity'])
                quant += 1
                row['Quantity'] = quant
            elif change == '-':
                quant = int(row['Quantity'])
                quant -= 1
                row['Quantity'] = quant

            print(GREEN, row, RESET)
            print(RED + 'WORKS' + RESET)
        else:
            print(RED + 'ERROR' + RESET)

    j = None
    for i in range(len(data)):
        print(GREEN, data, RESET)
        quant = int(data[i]['Quantity'])
        if quant == 0: j = i
    try:
        del data[j]
    except TypeError:
        print('NOTHING TO REMOVE')

    headers = ['Name', 'Price', 'Quantity', 'Cost']
    with open(filepath, mode="w+", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    return ()


# this is adding item for CART
@app.route("/cart", methods=["POST"])
def plus_item_cart():
    # print("Request method:", request.method)
    if "plus-item" in request.form:
        buttonValue = request.form["plus-item"]
        print("Button Value:", buttonValue)
    elif "item-minus" in request.form:
        buttonValue = request.form["item-minus"]
        print("Button Value:", buttonValue)

    # buttonValue is a string
    type_of_change = buttonValue[-1]
    name = buttonValue[:-2]
    print(name + ':' + type_of_change)
    changeCart = changeCART(name, type_of_change)
    return redirect(url_for("cart"))


# meant for adding items to cart
@app.route("/cart", methods=['GET'])
def cart():
    data = []
    totalCost = 0
    filepath = 'Web Server/buyee.csv'
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
            totalCost += float(row['Cost'])

    return render_template("cart.html", data=data, totalCost=totalCost)


# This is the last step
def creatingUSERjson(data, randomID):
    json_string = json.dumps(data, indent=4)
    json_file_name = 'purchases_user/' + str(randomID) + '.json'
    with open(f'{json_file_name}', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return ()


def write_ThingSpeak(data):
    data = data
    apiKEY = ''
    channelID = ''
    filepath = 'APIkey.csv'
    with open(filepath, mode="r") as file:
        reed = file.readlines()
        apiKEY = reed[0]

    filepath = 'ChannelID.csv'
    with open(filepath, mode="r") as file:
        reed = file.readlines()
        channelID = reed[0]

    # field 2 ~ Number User
    readTS = requests.get(f'https://api.thingspeak.com/channels/{channelID}/fields/2.json?results=1')
    numPPL = json.loads(readTS.text)

    try:
        number_of_Orders = (numPPL['feeds'][0]['field2'])
    except IndexError:
        number_of_Orders = None
    if number_of_Orders == None:
        number_of_Orders = 1
    else:
        number_of_Orders = int(number_of_Orders)
        number_of_Orders += 1
    # field 4 ~ Total Items Bought (Num)
    number_items = 0
    # field 5 ~ Total Bought ($)
    totalPurchase = 0
    for row in data:
        quant = row['Quantity']
        number_items += int(quant)
        cost = row['Cost']
        totalPurchase += float(cost)

    # print("apiKey: ",apiKEY)
    send_data = requests.get(f"https://api.thingspeak.com/update?api_key={apiKEY}&field4=%s&field5=%s&field2=%s" % (
        number_items, totalPurchase, number_of_Orders))
    time.sleep(1)
    print(send_data)
    return ()


# this is adding item for CART


@app.route("/checkout", methods=['GET', "POST"])
def checkout():
    data = []
    totalCost = 0

    filepath = 'Web Server/buyee.csv'
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
            totalCost += float(row['Cost'])
    file.close()

    filepath = 'purchases_user/random.csv'
    with open(filepath, mode='r+') as file:
        randomID = file.readline()
        if randomID == '':
            randomID = random.randint(10000, 99999)
            file.writelines(str(randomID))
    print('CUSTOMER ID:', randomID)
    file.close()

    # FOR CHECKOUT
    if data == []:
        print('No items, so no chackout')
        randomID = 0
        return redirect('/')
    else:
        print('CUSTOMER ID:', randomID)
        if "DONE" in request.form:
            print('CUSTOMER ID:', randomID)
            buttonValue = request.form["DONE"]
            print(buttonValue)
            creatingUSERjsons = creatingUSERjson(data, randomID)
            writeTS = write_ThingSpeak(data)

            with open(filepath, mode='w') as file:
                file.writelines('')
            filepath = 'Web Server/buyee.csv'
            with open(filepath, mode='w') as file:
                file.writelines('')
            return redirect('/')
        else:

            return render_template('checkout.html', randomID=randomID, data=data, totalCost=totalCost)


if __name__ == "__main__":
    print(RED, 'No of Threads:', threading.active_count(), RESET)
    app.run(debug=True, host="0.0.0.0")
