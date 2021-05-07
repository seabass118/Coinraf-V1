from flask import Flask, render_template, request
from data import DataPull, DataLists
import threading
import requests
import orjson


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


@app.route("/ss_search", methods=['GET', 'POST'])
def search():
    input_text = request.args['searchText']
    coins = []
    counter = 0
    for i in DataPull.coin_output:
        if str(input_text).lower() in i['id'].lower() or str(input_text).lower() in i['name'].lower():
            counter += 1

            if i['logo_url'] != "":
                ss_logo = i['logo_url']
            else:
                ss_logo = "/static/_images/_icons/ficon.png"
            
            if "rank" in i:
                ss_rank = i['rank']
            else:
                ss_rank = "unranked"

            coins.append([i['id'], i['name'], ss_logo, ss_rank])
            if counter == 5:
                break
    return_coins = []
    for i in coins:
        return_coins.append({'id': i[0], 'name': i[1], 'logo_url': i[2], 'rank': i[3]})
    return orjson.dumps(return_coins)


coin_api = "https://api.nomics.com/v1/currencies/ticker?key=202c24a2628a42174eb7b568f21230fe"


def data_pull():
    coin_pull2 = requests.get(coin_api)
    new_data = orjson.loads(coin_pull2.text)
    return new_data


threading.Timer(10.0, data_pull).start()


def data_push():
    index_coins = []
    counter = 0
    for i in data_pull():
        counter += 1
        if "price" in i:
            index_coins.append([i['rank'], i['price']])
        else:
            index_coins.append([i['rank'], "null"])
        if counter == 5:
            break
    coin_output = []
    for i in index_coins:
        coin_output.append({"rank": i[0], "price": i[1]})
    print(coin_output)
    return orjson.dumps(coin_output)


@app.route("/index_data", methods=['GET', 'POST'])
def index_data():
    return data_push()


