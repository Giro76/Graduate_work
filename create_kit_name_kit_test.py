# Поташов Игорь, 17-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Проверяем, что код ответа равен 200.
def test_get_order_by_track_success():
    response = sender_stand_request.post_new_order()
    new_track = str(response.json()['track'])  # Сохраняем номер трека заказа.
    receiving = sender_stand_request.get_receiving_a_order(new_track)
    assert receiving.status_code == 200
