from flask import Flask, render_template, request
from data import DataPull, DataLists, coin_output


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
  return render_template('index.html', list_length=DataLists.list_length);


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
       
       
