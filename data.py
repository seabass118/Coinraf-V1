import requests
import json
import orjson

coin_api = "https://api.nomics.com/v1/currencies/ticker?key=202c24a2628a42174eb7b568f21230fe"
coin_pull = requests.get(coin_api)


def data_req():
    coin_pull2 = requests.get(coin_api)
    new_data = orjson.loads(coin_pull2.text)
    index_coins = []
    counter = 0
    for i in new_data:
        counter += 1
        if "price" in i:
            index_coins.append([i['price']])
        else:
            index_coins.append(["price"])
        if counter == 1:
            break
    coin_output = []
    for i in index_coins:
        coin_output.append({"price": i[0]})
    return orjson.dumps(coin_output)


class DataPull:
    coin_output = orjson.loads(coin_pull.text)


class DataLists:
    id_list = [d['id'].lower() for d in DataPull.coin_output]
    list_length = len(id_list)
        