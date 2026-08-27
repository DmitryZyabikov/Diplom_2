import allure
import requests

from data.urls import ORDERS_URL, INGREDIENTS_URL, REQUEST_TIMEOUT


class OrderApi:
    """Методы для работы с API заказов."""

    @allure.step("Отправить запрос на создание заказа")
    def create_order(self, payload, access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        return requests.post(
            ORDERS_URL,
            json=payload,
            headers=headers,
            timeout=REQUEST_TIMEOUT
        )

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        return requests.get(INGREDIENTS_URL, timeout=REQUEST_TIMEOUT)