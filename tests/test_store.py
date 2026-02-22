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