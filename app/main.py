from flask import Flask, render_template
from data import DataLists
 

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
 

@app.route('/')
def index():
  return render_template('index.html', coin_length=DataLists.list_length);


@app.route('/crypto')
def news():
  return render_template('crypto.html')
  

@app.route('/exchanges')
def exchanges():
  return render_template('exchanges.html');
  

@app.route('/discover')
def data():
  return render_template('discover.html')
  