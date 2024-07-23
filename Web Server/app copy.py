from flask import Flask, render_template, request, redirect, url_for, session

# import pandas as pd
import os
import csv

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

# def addingPrice():
#     purchaseData = []
#     storeData = []
#
#
#     purchasePath = "Web Server/purchases.csv"
#     with open(purchasePath, mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             purchaseData.append(row)
#
#
#     storePath = "Web Server/data.csv"
#
#     with open(storePath, mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             storeData.append(row)
#
#     for row in storeData:
#         # print(MAGENTA, row, RESET)
#
#         name = row["Name"]
#         number = row["Quantity"]
#         price = row["Price"]
#
#         for i in range(len(purchaseData)):
#             if purchaseData[i]['Name'] == name:
#                 print('Adding Price')
#                 purchaseData[i]['Price'] = price
#             else:
#                 print('ERROR')
#
#     print(RED,purchaseData,RESET)
#     return ()
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
    print(RED,itemData,RESET)

    data = []
    filepath = 'Web Server/buyee.csv'
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    file.close()
    #the below code written by Yaq
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

    #This is taken from chatGPT
    indexsData = []
    indexsItemData = []
    for i in range(len(data)):indexsData.append(data[i]['Name'])
    for i in range(len(itemData)):indexsItemData.append(itemData[i]['Name'])
    matchingIndexforItem_data = [i for i,item in enumerate(indexsItemData) if item in indexsData]
    #~~~#

    newData = []
    for i in range(len(data)):
        mergeDict = {**itemData[(matchingIndexforItem_data[i])],**data[i]}
        newData.append(mergeDict)

    for row in newData:
        cost = int(row['Quantity']) * float(row['Price'])
        row['Cost'] = cost

    print(MAGENTA,newData,RESET)

    headers = list(newData[0].keys())
    print(headers)

    with open(filepath, mode="w+", newline='') as file:
        writer = csv.DictWriter(file,fieldnames=headers)
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
        print("Button Value:",buttonValue)
        writerC = writeCart(buttonValue)
    return redirect(url_for("index"))

# meant for adding items to cart
@app.route("/cart", methods = ['GET'])
def cart():
    data = []
    filepath = "Web Server/purchases.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    print(RED, data ,RESET)
    return render_template("cart.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
