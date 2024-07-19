from cgi import print_environ
from dataclasses import dataclass
from tkinter.font import names

from Cython.Compiler.TypeSlots import lenfunc
from flask import Flask, render_template, request, redirect, url_for, session

# import pandas as pd
import os
import csv

from libpasteurize.fixes.fix_imports2 import name_import

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

    data = []
    filepath = "Web Server/purchases.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
        print(data)


        # print(rowName)
        row = {}
        print(print('--' * 50))
        if data == []:
            print('inNew')
            row['Name'] = name
            row['Quantity'] = 1
            data.append(row)

        else:
            for i in range(len(data)):
                print('Number of Rows', len(data))
                print('--' * 50)
                itemName  = data[i]['Name']
                row = data[i]
                print('Name of item?',itemName)
                if itemName == name:
                    print("inadd")
                    quantity = int(row["Quantity"])
                    quantity += 1
                    # print(name, quantity)
                    row["Quantity"] = quantity

                else:
                    newRow ={}
                    print('addNew Item')
                    newRow['Name'] = name
                    newRow['Quantity'] = 1
                    data.append(newRow)


    print('--'*50)
    print(data)
    with open(filepath, mode="w", newline="") as file:
        fieldnames = ["Name", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row

        for person in data:
            writer.writerow(person)

    ####
    filepath = "Web Server/purchases.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)
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


@app.route("/np")
def np():
    return render_template("productDatabase.html")


# meant for adding items to cart
@app.route("/cart")
def cart():
    return render_template("cart.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
