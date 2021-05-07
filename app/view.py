from flask import Flask, render_template, request
from controller import data_push, data_search, total_coins
import threading
import requests
import orjson


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html', list_length=total_coins());


@app.route('/crypto')
def news():
    return render_template('crypto.html')


@app.route('/bsc')
def bsc():
    return render_template('BSC.html')
  

@app.route('/exchanges')
def exchanges():
    return render_template('exchanges.html');
  

@app.route('/discover')
def data():
    return render_template('discover.html')


@app.route("/ss_search", methods=['GET'])
def search():
    return data_search()


@app.route("/index_data", methods=['GET'])
def index_data():
    return data_push()


