import allure
import jsonschema
import requests

from .schemas.store_schema import STORE_SCHEMA

BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature('Store')
class TestStore:
    @allure.title('Размещение заказа')
    def test_place_an_order(self):
        with allure.step('Подготовка данных для размещения заказа'):
            payload = {
                "id": 1,
                "petId": 1,
                "quantity": 1,
                "status": "placed",
                "complete": True
            }
            response = requests.post(f'{BASE_URL}/store/order', json=payload)
        with allure.step('Проверка статуса ответа и валидация JSON-схемы'):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            jsonschema.validate(response.json(), STORE_SCHEMA)


    @allure.title('Получение информации о заказе по ID')
    def test_get_info_of_order_by_id(self, create_order):
        with allure.step('Получение ID созданного заказа'):
            order_id = create_order['id']
        with allure.step('Отправка запроса на получение инфо о заказе по ID'):
            response = requests.get(f'{BASE_URL}/store/order/{order_id}')
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            assert response.json()['id'] == order_id


    @allure.title('Удаление заказа по ID')
    def test_delete_order_by_id(self, create_order):
        with allure.step('Получение ID заказа'):
            order_id = create_order['id']
        with allure.step('Отправка запроса на удаление по ID'):
            response = requests.delete(f'{BASE_URL}/store/order/{order_id}')
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
        with allure.step('Отправка запроса на получение инфо об удаленном заказе'):
            response = requests.get(f'{BASE_URL}/store/order/{order_id}')
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"


    @allure.title('Попытка получить информацию о несуществующем заказе')
    def test_get_info_of_nonexistent_order(self):
        with allure.step('Отправка запроса на поулчение инфо о несуществующем заказе'):
            response = requests.get(f'{BASE_URL}/store/order/9999')
        with allure.step('Проверка статуса и текста ответа'):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"
            assert response.text == "Order not found", "Текст ответа не совпал с ожидаемым"





