from flask import request
import requests
import orjson
import threading
import locale


locale.setlocale(locale.LC_ALL, 'English_United States.1252')


ticker_api = "https://api.nomics.com/v1/currencies/ticker?key=202c24a2628a42174eb7b568f21230fe"
ticker_pull = requests.get(ticker_api)
ticker_json = orjson.loads(ticker_pull.text)


def total_coins():
    total_list =  [p['id'].lower() for p in ticker_json]
    total_coins = len(total_list)
    return total_coins


def data_search():
    input_text = request.args['searchText']
    coins = []
    counter = 0
    for i in ticker_json:
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


def data_pull():
    coin_pull2 = requests.get(ticker_api)
    new_data = orjson.loads(coin_pull2.text)
    return new_data


threading.Timer(10.0, data_pull).start()


def pc_conv(p):
    pre_change = float(p) * 100
    change = "{:.2f}".format(pre_change)
    return str(change)


def format_currency(p):
    change = locale.currency(float(p), grouping=True)
    return str(change)


def data_push():
    index_coins = []
    counter = 0
    for i in data_pull():
        counter += 1
        if "1d" in i:
            coin_percentage_change = pc_conv(i['1d']['price_change_pct'])
        else:
            coin_percentage_change = "no 24hr data"
        if "price" in i:
            coin_price = format_currency(i['price'])
        else:
            coin_price = "no price data"
        index_coins.append([i['logo_url'], i['name'], i['id'], coin_percentage_change, coin_price])
        if counter == 10:
            break
    coin_output = []
    for i in index_coins:
        coin_output.append({"logo_url": i[0], "name": i[1], "id": i[2], "change": i[3], "price": i[4]})
    return orjson.dumps(coin_output)