import requests
import orjson


coin_api = "https://api.nomics.com/v1/currencies/ticker?key=202c24a2628a42174eb7b568f21230fe"
coin_pull = requests.get(coin_api)

class DataPull:
    coin_output = orjson.loads(coin_pull.text)


class DataLists:
    id_list = [d['id'].lower() for d in DataPull.coin_output]
    list_length = len(id_list)