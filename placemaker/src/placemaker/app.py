__author__ = 'jermellbeane'
from flask import Flask
app = Flask(__name__)
from flask import abort, render_template,request, jsonify
import json
import pickle
import pytz
import datetime
import mongoengine
from settings import MONGO_HOST, MONGO_DB
mongoengine.connect(MONGO_DB, host=MONGO_HOST)

@app.route('/')
def index():
    return render_template('home.html')