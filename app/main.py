from flask import Flask, render_template, request
from data import DataPull, DataLists, coin_pull, data_req
from twisted.internet import task, reactor
import orjson

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


#View


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


#Controller

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


@app.route("/index_data", methods=['GET', 'POST'])
def index_data():
    timeout = 11.0
    l = task.LoopingCall(data_req)
    l.start(timeout)
    reactor.run()
    return data_req()
