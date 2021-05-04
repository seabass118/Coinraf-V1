from flask import Flask, render_template, request
from data import DataPull, DataLists
from flask_paginate import Pagination, get_page_args
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

            if i['logo_url'] != "":
              ss_logo = i['logo_url']
            else:
              ss_logo = "/static/_images/_icons/ficon.png"
            
            if "rank" in i:
              ss_rank = i['rank']
            else:
              ss_rank = "unranked"

            coins.append([i['id'],i['name'],ss_logo,ss_rank])
            if counter == 5:
                break
    return_coins = []
    for i in coins:
        return_coins.append({'id':i[0], 'name':i[1], 'logo_url':i[2], 'rank':i[3]})
    return orjson.dumps(return_coins)


def get_coins(page, offset=0, per_page=50):
    offset = ((page - 1) * per_page)
    return DataPull.coin_output[offset: offset + per_page]


@app.template_filter()
def format_currency(value):
    return "${:,.2f}".format(value)


@app.template_filter()
def string_chop(value):
    return value[:-3]


@app.route('/')
def index():
  page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
  total = len(DataPull.coin_output)
  per_page = 50
  pagination_coins = get_coins(page=page, offset=offset, per_page=per_page)
  pagination = Pagination(page=page, per_page=per_page, total=total)
  return render_template('index.html', list_length=DataLists.list_length, table_data=pagination_coins,page=page,per_page=per_page,pagination=pagination);


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
       
       
