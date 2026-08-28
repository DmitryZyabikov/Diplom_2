"""Тесты создания пользователя."""

import allure
import pytest

from api.user_api import UserApi
from data.test_data import generate_user_payload_without_field


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.story("Создание уникального пользователя")
    @allure.title("Создание уникального пользователя возвращает 200 и success=True")
    def test_create_unique_user(self, created_user):
        assert created_user["access_token"] is not None

    @allure.story("Создание пользователя, который уже зарегистрирован")
    @allure.title("Повторная регистрация возвращает 403 и сообщение об ошибке")
    def test_create_duplicate_user(self, registered_user):
        user_api = UserApi()
        payload = {
            "email": registered_user["email"],
            "password": registered_user["password"],
            "name": registered_user["name"],
        }
        response = user_api.register_user(payload)

        assert response.status_code == 403
        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "User already exists"

    @allure.story("Создание пользователя без обязательного поля")
    @allure.title("Создание пользователя без поля {missing_field} возвращает 403")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_without_required_field(self, missing_field):
        user_api = UserApi()
        payload = generate_user_payload_without_field(missing_field)
        response = user_api.register_user(payload)

        assert response.status_code == 403
        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "Email, password and name are required fields"