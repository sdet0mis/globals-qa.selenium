import json
from typing import Any

import allure
from allure_commons.types import AttachmentType
from pydantic import BaseModel
from pydantic import ValidationError


class BaseService:

    def __init__(self) -> None:
        self.response = None

    def validate(self, code: int, model: BaseModel) -> BaseModel:
        if self.response.status_code == code:
            try:
                if "Content-Type" in self.response.headers:
                    return model(**self.response.json()) \
                        if self.response.headers[
                            "Content-Type"
                        ] == "application/json" else model(self.response.text)
                return model(self.response.headers["Date"])
            except ValidationError as e:
                raise AssertionError(e)

    @allure.step("Проверить статус код {code}")
    def check_status_code(self, code: int = 200) -> None:
        assert self.response.status_code == code, f"\n \
Ожидаемый статус код: {code}\n \
Фактический статус код: {self.response.status_code}\n \
Ответ: {self.response.text}"

    def check_field(
        self, field: str, field_value: Any, expected_value: Any
    ) -> None:
        with allure.step(f"Проверить значение поля {field}"):
            assert field_value == expected_value, f"\n \
Ожидаемое значение: {expected_value}\n \
Фактическое значение: {field_value}"

    def attach_response_body(self) -> None:
        try:
            allure.attach(
                name="Тело ответа",
                body=json.dumps(self.response.json(), indent=4),
                attachment_type=AttachmentType.JSON
            )
        except:  # noqa
            pass
