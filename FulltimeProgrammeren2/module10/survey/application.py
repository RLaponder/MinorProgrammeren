# **************************************************************************************
# application.py
#
# Fulltime Programmeren 2
# Robin Laponder
#
# This file represents my web app’s “controller”.
# **************************************************************************************


import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # Show an error message when information is missing.
    if not request.form.get("name") or not request.form.get("gender") or not request.form.get("age"):
        return render_template("error.html", message="Oops! It looks like you forgot something...")

    # Write the entered information in survey.csv.
    with open("survey.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "gender", "age"])
        writer.writerow({"name": request.form.get("name"), "gender": request.form.get("gender"), "age": request.form.get("age")})
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    # Put data in a list and data.html creates a table.
    file = open("survey.csv", "r")
    reader = csv.DictReader(file)
    data = list(reader)
    return render_template("data.html", data=data)
