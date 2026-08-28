"""Тесты авторизации пользователя."""

import allure

from api.user_api import UserApi


@allure.feature("Авторизация пользователя")
class TestLoginUser:

    @allure.story("Вход под существующим пользователем")
    @allure.title("Вход с корректными данными возвращает 200 и accessToken")
    def test_login_existing_user(self, registered_user):
        user_api = UserApi()
        payload = {
            "email": registered_user["email"],
            "password": registered_user["password"],
        }
        response = user_api.login_user(payload)

        assert response.status_code == 200
        response_json = response.json()
        assert response_json["success"] is True
        assert "accessToken" in response_json
        assert "refreshToken" in response_json
        assert response_json["user"]["email"] == registered_user["email"].lower()

    @allure.story("Вход с неверным логином и паролем")
    @allure.title("Вход с неверными данными возвращает 401 и сообщение об ошибке")
    def test_login_with_wrong_credentials(self):
        user_api = UserApi()
        payload = {
            "email": "wrong_email@example.com",
            "password": "wrong_password",
        }
        response = user_api.login_user(payload)

        assert response.status_code == 401
        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "email or password are incorrect"