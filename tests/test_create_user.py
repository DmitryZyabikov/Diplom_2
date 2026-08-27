"""Тесты создания пользователя."""

import allure
import pytest

from api.user_api import UserApi
from data.test_data import generate_user_payload_without_field


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.story("Создание уникального пользователя")
    @allure.title("Создание уникального пользователя возвращает 200 и success=True")
    def test_create_unique_user(self, user_payload):
        user_api = UserApi()
        response = user_api.register_user(user_payload)

        assert response.status_code == 200
        response_json = response.json()
        assert response_json["success"] is True
        assert "accessToken" in response_json
        assert "refreshToken" in response_json
        assert response_json["user"]["email"] == user_payload["email"].lower()
        assert response_json["user"]["name"] == user_payload["name"]

        user_api.delete_user(response_json["accessToken"])

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