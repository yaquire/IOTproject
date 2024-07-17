from flask import Flask, render_template, request, redirect, url_for, session

# import pandas as pd
import os
import csv

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

    # print(data)
    items = []
    return render_template("main.html", data=data, item=items)


@app.route("/np")
def np():
    return render_template("productDatabase.html")


# mean for adding items to cart
@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    item = request.form.get("item")
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(item)
    return redirect(url_for("index"))


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
