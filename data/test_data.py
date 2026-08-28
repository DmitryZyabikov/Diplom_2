import random
import string

INGREDIENT_IDS = {
    "bun_1": "61c0c5a71d1f82001bdaaa6d",
    "bun_2": "61c0c5a71d1f82001bdaaa6c",
    "sauce_1": "61c0c5a71d1f82001bdaaa72",
    "sauce_2": "61c0c5a71d1f82001bdaaa73",
    "main_1": "61c0c5a71d1f82001bdaaa6f",
    "main_2": "61c0c5a71d1f82001bdaaa70",
}

VALID_INGREDIENTS = [INGREDIENT_IDS["bun_1"], INGREDIENT_IDS["sauce_1"]]
INVALID_HASH = "invalid_hash_12345"


def generate_random_string(length=10):
    """Генерирует случайную строку из букв и цифр."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_unique_user_payload():
    """Генерирует payload для создания уникального пользователя."""
    unique_str = generate_random_string()
    return {
        "email": f"test_{unique_str}@example.com",
        "password": generate_random_string(12),
        "name": f"User_{unique_str}"
    }


def generate_user_payload_without_field(missing_field):
    """Генерирует payload без указанного поля."""
    payload = generate_unique_user_payload()
    del payload[missing_field]
    return payload