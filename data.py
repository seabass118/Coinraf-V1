import requests
import orjson

coin_api = "https://api.nomics.com/v1/currencies/ticker?key=202c24a2628a42174eb7b568f21230fe"
coin_pull = requests.get(coin_api)
coin_output = orjson.loads(coin_pull.text)

class DataPull:
    search_data = [d['id'] for d in coin_output]
    # print(coin_output)

class DataLists:
    data_dict = coin_output
    id_list = [d['id'].lower() for d in coin_output]
    list_length = len(id_list)
        