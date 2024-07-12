from flask import Flask, render_template
import pandas as pd
import os
import csv

app = Flask(__name__)


@app.route("/")
def index():
    # Check if data.csv exists
    data = []
    with open("data.csv", mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    # print(data)

    return render_template("main.html")


@app.route("/np")
def np():
    return render_template("productDatabase.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/template")
def template():
    return render_template("template.html")


@app.route("/filter")
def filter():
    return render_template("filteredPage.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
