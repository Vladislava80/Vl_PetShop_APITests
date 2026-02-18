import allure
import requests
from .schemas.pet_schema import PET_SCHEMA
import jsonschema

BASE_URL = "http://5.181.109.28:9090/api/v3"


@allure.feature('Pet')
class TestPet:
    @allure.title('Попытка удалить несуществующего питомца')
    def test_delete_nonexistent_pet(self):
        with allure.step('Отправка запроса на удаление несуществующего питомца'):
            response = requests.delete(url=f'{BASE_URL}/pet/9999')

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
        with allure.step('Проверка текста ответа'):
            assert response.text == "Pet deleted", "Текст не совпадает с ожидаемым"


    @allure.title('Попытка обновить несуществующего питомца')
    def test_update_nonexistent_pet(self):
        with allure.step('Отправка запроса на обновление несуществующего питомца'):
            payload = {
                "id": 9999,
                "name": "Non-existent Pet",
                "status": "available"
            }
            response = requests.put(url=f'{BASE_URL}/pet', json=payload)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"
        with allure.step('Проверка текста ответа'):
            assert response.text == "Pet not found", "Текст не совпадает с ожидаемым"


    @allure.title('Попытка получить информацию о несуществующем питомце')
    def test_get_info_of_nonexistent_pet(self):
        with allure.step('Отправка запроса на информацию о несуществующем питомце'):
            response = requests.get(url=f'{BASE_URL}/pet/9999')
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"


    @allure.title('Добавление нового питомца')
    def test_add_pet(self):
        with allure.step('Подготовка данных для создания питомца'):
            payload = {
                "id": 1,
                "name": "Buddy",
                "status": "available"
            }
            response = requests.post(url=f'{BASE_URL}/pet', json=payload)
        with allure.step('Проверка статуса ответа и валидация JSON-схемы'):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            jsonschema.validate(response.json(), PET_SCHEMA)

    @allure.title('Добавление нового питомца c полными данными')
    def test_add_new_pet_full_dates(self):
        with allure.step('Подготовка полных данных для создания нового питомца'):
            payload = {
                "id": 10,
                "name": "doggie",
                "category": {
                    "id": 1,
                    "name": "Dogs"
                },
                "photoUrls": ["string"],
                "tags": [{
                    "id": 0,
                    "name": "string"
                }],
                "status": "available"
            }
            response = requests.post(url=f'{BASE_URL}/pet', json=payload)
        with allure.step('Проверка статуса ответа и валидация JSON-схемы'):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            jsonschema.validate(response.json(), PET_SCHEMA)