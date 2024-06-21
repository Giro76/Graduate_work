import configuration
import requests
import data


# Создаём POST-запрос запрос на создание заказа.
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_AN_ORDER,
                         json=body,
                         headers=data.headers_order)


# Создаём GET-запрос на  получения заказа по треку заказа.
def get_receiving_a_order():
    response = post_new_order(data.order_body)
    new_track = str(response.json()['track'])  # Сохраняем номер трека заказа.
    return requests.get(configuration.URL_SERVICE + configuration.GETTING_A_TRACK + new_track)




