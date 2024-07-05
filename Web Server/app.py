from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/np")
def np():
    return render_template("productDatabase.html")


@app.route("/cart")
def cart():
    return render_template("cartPage.html")


@app.route("/template")
def template():
    return render_template("template.html")


@app.route("/filter")
def filter():
    return render_template("filteredPage.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
