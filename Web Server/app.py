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


### This is a test
def writeCart(name):
    name = name
    # print(name)
    data = []
    filepath = "Web Server/purchases.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

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

    hasInteger = any(isinstance(x, int) for x in rangeNo)
    # print(RED,hasInteger,RESET)
    if hasInteger is False:
        row = {}
        row['Name'] = name
        row["Quantity"] = 1
        data.append(row)
    elif hasInteger is True:
        quant = int(data[i]['Quantity'])
        quant += 1
        data[i]['Quantity'] = quant
    else:
        print(RED + 'ERROR' + RESET)

    # print('--' * 50)
    # print(data)
    with open(filepath, mode="w", newline="") as file:
        fieldnames = ["Name", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row

        for person in data:
            writer.writerow(person)

    ####
    # print(CYAN + str(data) + RESET)

    datas = []
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            datas.append(row)
    print(MAGENTA + str(datas) + RESET)
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


###

# meant for adding items to cart
@app.route("/cart")
def cart():
    datas = []
    filepath = "Web Server/purchases.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            datas.append(row)

    return render_template("cart.html", data=datas)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
