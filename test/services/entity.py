import json
from dataclasses import asdict
from typing import Any

import allure

from services.http_client import HTTPClient
from config.endpoints import EntityEndpoints
from config.payloads import Entity, Addition
from helpers.checkers import Checkers
from config.models import EntityIdModel
from config.models import EntityDateModel
from config.models import EntityModel
from config.models import EntitiesModel


class EntityService(HTTPClient):

    def __init__(self):
        super().__init__()
        self.endpoints = EntityEndpoints()

    @allure.step("Создать сущность с заголовком {title}")
    def create_entity(
        self,
        additional_info: str,
        additional_number: int,
        important_numbers: list[int],
        title: str,
        verified: bool,
        expected_code: int = 200
    ) -> dict[str, dict[str, Any] | EntityIdModel]:
        payloads = Entity(
            Addition(
                additional_info,
                additional_number
            ),
            important_numbers,
            title,
            verified
        )
        self.response = self.post(
            url=self.endpoints.CREATE_ENTITY,
            json=asdict(payloads)
        )
        Checkers.check_status_code(expected_code, self.response.status_code)
        if expected_code == 200:
            model = EntityIdModel.model_validate(
                json.loads(self.response.content)
            )
            return {"payloads": payloads, "model": model}

    @allure.step("Удалить сущность с id {id}")
    def delete_entity(
        self, id: int, expected_code: int = 204
    ) -> EntityDateModel:
        self.response = self.delete(url=self.endpoints.DELETE_ENTITY(id))
        Checkers.check_status_code(expected_code, self.response.status_code)
        if expected_code == 204:
            return EntityDateModel.model_validate(self.response.headers)

    @allure.step("Получить сущность с id {id}")
    def get_entity(self, id: int, expected_code: int = 200) -> EntityModel:
        self.response = self.get(url=self.endpoints.GET_ENTITY(id))
        Checkers.check_status_code(expected_code, self.response.status_code)
        if expected_code == 200:
            return EntityModel.model_validate(self.response.json())

    @allure.step("Получить все сущности")
    def get_entities(self, expected_code: int = 200) -> EntitiesModel:
        self.response = self.get(url=self.endpoints.GET_ENTITIES)
        Checkers.check_status_code(expected_code, self.response.status_code)
        if expected_code == 200:
            return EntitiesModel.model_validate(self.response.json())

    @allure.step("Обновить сущность с id {id}")
    def update_entity(
        self,
        id: int,
        additional_info: str,
        additional_number: int,
        important_numbers: list[int],
        title: str,
        verified: bool,
        code: int = 204
    ) -> dict[str, dict[str, Any] | EntityDateModel]:
        payloads = Entity(
            Addition(
                additional_info,
                additional_number
            ),
            important_numbers,
            title,
            verified
        )
        self.response = self.patch(
            url=self.endpoints.UPDATE_ENTITY(id),
            json=asdict(payloads)
        )
        Checkers.check_status_code(code, self.response.status_code)
        if code == 204:
            model = EntityDateModel.model_validate(self.response.headers)
            return {"payloads": payloads, "model": model}
