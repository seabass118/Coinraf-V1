from flask import Flask, render_template, request
from data import DataPull, DataLists
import orjson

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/ss_search", methods=['GET', 'POST'])
def search():
    input_text = request.args['searchText']
    coins = []
    counter = 0
    for i in DataPull.coin_output:
        if str(input_text).lower() in i['id'].lower() or str(input_text).lower() in i['name'].lower():
            counter += 1
            coins.append([i['id'],i['name'],i['logo_url'],i['rank']])
            if counter == 5:
                break
    return_coins = []
    for i in coins:
        return_coins.append({'id':i[0], 'name':i[1], 'logo_url':i[2], 'rank':i[3]})
    return orjson.dumps(return_coins)

@app.route('/', methods=['GET', 'POST'])
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
       
       
