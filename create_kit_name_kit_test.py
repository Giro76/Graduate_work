# Поташов Игорь, 17-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Проверяем, что код ответа равен 200.

def test_response_code():
    receiving = sender_stand_request.get_receiving_a_order()
    assert receiving.status_code == 200
