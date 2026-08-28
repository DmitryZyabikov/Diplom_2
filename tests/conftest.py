"""Фикстуры для API-тестов."""

import pytest

from api.user_api import UserApi
from data.test_data import generate_unique_user_payload


@pytest.fixture
def user_payload():
    """Генерирует данные для создания уникального пользователя."""
    return generate_unique_user_payload()


@pytest.fixture
def registered_user(user_payload):
    """Создаёт и возвращает зарегистрированного пользователя.
    Удаляет пользователя после теста."""
    user_api = UserApi()
    response = user_api.register_user(user_payload)
    response_json = response.json()

    access_token = response_json.get("accessToken")
    user_data = {
        "email": user_payload["email"],
        "password": user_payload["password"],
        "name": user_payload["name"],
        "access_token": access_token,
    }

    yield user_data

    if access_token:
        user_api.delete_user(access_token)


@pytest.fixture
def created_user(user_payload):
    """Создаёт пользователя и возвращает его данные вместе с access_token.
    Удаляет пользователя после теста."""
    user_api = UserApi()
    response = user_api.register_user(user_payload)
    response_json = response.json()
    access_token = response_json.get("accessToken")

    yield {
        "email": user_payload["email"],
        "password": user_payload["password"],
        "name": user_payload["name"],
        "access_token": access_token,
    }

    if access_token:
        user_api.delete_user(access_token)