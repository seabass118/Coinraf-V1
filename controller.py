from flask import request
import requests
import orjson
import threading


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
    return orjson.dumps(coin_output)