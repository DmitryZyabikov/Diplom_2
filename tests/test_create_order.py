"""Тесты создания заказа."""

import allure

from api.order_api import OrderApi
from data.test_data import VALID_INGREDIENTS, INVALID_HASH


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Создание заказа с авторизацией и ингредиентами")
    @allure.title("Создание заказа с авторизацией возвращает 200 и номер заказа")
    def test_create_order_with_auth(self, registered_user):
        order_api = OrderApi()
        payload = {"ingredients": VALID_INGREDIENTS}
        response = order_api.create_order(
            payload, access_token=registered_user["access_token"]
        )

        assert response.status_code == 200
        response_json = response.json()
        assert response_json["success"] is True
        assert "order" in response_json
        assert "number" in response_json["order"]

    @allure.story("Создание заказа без авторизации")
    @allure.title("Создание заказа без авторизации возвращает 200")
    def test_create_order_without_auth(self):
        order_api = OrderApi()
        payload = {"ingredients": VALID_INGREDIENTS}
        response = order_api.create_order(payload)

        assert response.status_code == 200
        response_json = response.json()
        assert response_json["success"] is True

    @allure.story("Создание заказа без ингредиентов")
    @allure.title("Создание заказа без ингредиентов возвращает 400")
    def test_create_order_without_ingredients(self, registered_user):
        order_api = OrderApi()
        payload = {"ingredients": []}
        response = order_api.create_order(
            payload, access_token=registered_user["access_token"]
        )

        assert response.status_code == 400
        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "Ingredient ids must be provided"

    @allure.story("Создание заказа с неверным хешем ингредиентов")
    @allure.title("Создание заказа с неверным хешем возвращает 500")
    def test_create_order_with_invalid_hash(self, registered_user):
        order_api = OrderApi()
        payload = {"ingredients": [INVALID_HASH]}
        response = order_api.create_order(
            payload, access_token=registered_user["access_token"]
        )

        assert response.status_code == 500