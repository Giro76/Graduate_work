import configuration
import requests
import data


# Создаём POST-запрос запрос на создание заказа.
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_AN_ORDER,
                         json=data.order_body,
                         headers=data.headers_order)


# Создаём GET-запрос на получения заказа по треку заказа.
def get_receiving_a_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GETTING_A_TRACK + track)




