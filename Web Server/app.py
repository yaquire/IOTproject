from flask import Flask, render_template, request, redirect, url_for, session
# import pandas as pd
import os
import csv

app = Flask(__name__)


@app.route("/" , methods=["get","POST"])
def index():
    # Check if data.csv exists
    data = []
    filepath = "Web Server/data.csv"
    with open(filepath, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)


    if request.method == 'POST':
        for item in data:
            #print (item)
            #print(item["Name"])
            if  request.form['addingToCart'] == item["Name"]:
                print('works')
                namee=item['Name']
                writeC = writeCart(namee)
    return render_template("main.html", data=data)


def writeCart(name):
    name = name 
    print(name)
    filepath = "Web Server/purchases.csv"
    with open(filepath, mode="w") as file:
        writeer = csv.DictWriter(file,name)
    return ()

@app.route("/np")
def np():
    return render_template("productDatabase.html")


# meant for adding items to cart


@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    return render_template("cart.html", cart_items=cart_items)


@app.route("/template")
def template():
    return render_template("template.html")


@app.route("/filter")
def filter():
    return render_template("filteredPage.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
