from typing import Any

import allure


class Checkers:

    @staticmethod
    @allure.step("Проверить статус код {expected_code}")
    def check_status_code(expected_code: int, response_code: int) -> None:
        assert response_code == expected_code, f"\n \
    Ожидаемый статус код: {expected_code}\n \
    Фактический статус код: {response_code}"

    @staticmethod
    @allure.step("Проверить значение поля {field}")
    def check_field(field_value: Any, expected_value: Any) -> None:
        assert field_value == expected_value, f"\n \
    Ожидаемое значение: {expected_value}\n \
    Фактическое значение: {field_value}"
