import allure
import requests

from data.urls import REGISTER_URL, LOGIN_URL, REQUEST_TIMEOUT


class UserApi:
    """Методы для работы с API пользователей."""

    @allure.step("Отправить запрос на регистрацию пользователя")
    def register_user(self, payload):
        return requests.post(REGISTER_URL, json=payload, timeout=REQUEST_TIMEOUT)

    @allure.step("Отправить запрос на авторизацию пользователя")
    def login_user(self, payload):
        return requests.post(LOGIN_URL, json=payload, timeout=REQUEST_TIMEOUT)

    @allure.step("Удалить пользователя")
    def delete_user(self, access_token):
        headers = {"Authorization": access_token}
        return requests.delete(
            f"{REGISTER_URL}/user",
            headers=headers,
            timeout=REQUEST_TIMEOUT
        )