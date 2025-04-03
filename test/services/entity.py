from typing import Any

import allure
import requests

from services.base_service import BaseService
from config.endpoints import EntityEndpoints
from config.payloads import EntityPayloads
from config.models import EntityIdModel
from config.models import EntityDateModel
from config.models import EntityModel
from config.models import EntitiesModel


class EntityService(BaseService):

    def __init__(self):
        super().__init__()
        self.endpoints = EntityEndpoints()
        self.payloads = EntityPayloads()

    @allure.step("Создать сущность с заголовком {title}")
    def create_entity(
        self,
        additional_info: str,
        additional_number: int,
        important_numbers: list[int],
        title: str,
        verified: bool
    ) -> dict[str, dict[str, Any] | EntityIdModel]:
        payloads = self.payloads.entity(
            additional_info,
            additional_number,
            important_numbers,
            title,
            verified
        )
        self.response = requests.post(
            url=self.endpoints.CREATE_ENTITY,
            json=payloads
        )
        model = self.validate(200, EntityIdModel)
        return {"payloads": payloads, "model": model}

    @allure.step("Удалить сущность с id {id}")
    def delete_entity(self, id: int) -> EntityDateModel:
        self.response = requests.delete(url=self.endpoints.DELETE_ENTITY(id))
        return self.validate(204, EntityDateModel)

    @allure.step("Получить сущность с id {id}")
    def get_entity(self, id: int) -> EntityModel:
        self.response = requests.get(url=self.endpoints.GET_ENTITY(id))
        return self.validate(200, EntityModel)

    @allure.step("Получить все сущности")
    def get_entities(self) -> EntitiesModel:
        self.response = requests.get(url=self.endpoints.GET_ENTITIES)
        return self.validate(200, EntitiesModel)

    @allure.step("Обновить сущность с id {id}")
    def update_entity(
        self,
        id: int,
        additional_info: str,
        additional_number: int,
        important_numbers: list[int],
        title: str,
        verified: bool
    ) -> dict[str, dict[str, Any] | EntityDateModel]:
        payloads = self.payloads.entity(
            additional_info,
            additional_number,
            important_numbers,
            title,
            verified
        )
        self.response = requests.patch(
            url=self.endpoints.UPDATE_ENTITY(id),
            json=payloads
        )
        model = self.validate(204, EntityDateModel)
        return {"payloads": payloads, "model": model}
