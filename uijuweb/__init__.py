from flask import *
import os

app = Flask(__name__)

@app.route("/")
def mainpage():
    return "Hello World"
