import json
from flask import Flask, request, render_template, make_response
from time import time, localtime
import pymysql

db = None
cur = None
app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    result= "TEST"
    return render_template("home.html", result=result)

@app.route('/map')
def map():
    result = "TEST"
    return render_template("mainMap.html", result=result)

@app.route('/login')
def login():
    result = "TEST"
    return render_template("login.html", result=result)


if __name__ == '__main__':
    app.run()
