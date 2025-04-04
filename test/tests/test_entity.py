from typing import Any

import allure
import pytest

from config.models import EntityIdModel
from data.entity import EntityData
from services.entity import EntityService


@allure.epic("API")
@allure.feature("Сущность")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
class TestEntity:

    @allure.title("Создание сущности")
    def test_create_entity(self, entity_service: EntityService) -> None:
        entity = entity_service.create_entity(*(EntityData().entity()))
        entity_service.check_status_code()
        entity_service.attach_response_body()
        entity_service.get_entity(entity["model"].root)
        entity_service.check_status_code()

    @allure.title("Удаление сущности")
    def test_delete_entity(self, entity_service: EntityService) -> None:
        entity = entity_service.create_entity(*(EntityData().entity()))
        entity_service.check_status_code()
        entity_service.delete_entity(entity["model"].root)
        entity_service.check_status_code(204)
        entity_service.attach_response_body()
        entity_service.get_entity(entity["model"].root)
        entity_service.check_status_code(404)

    @allure.title("Получение сущности")
    def test_get_entity(
        self,
        entity_service: EntityService,
        entity: dict[str, dict[str, Any] | EntityIdModel]
    ) -> None:
        entity_service.get_entity(entity["model"].root)
        entity_service.check_status_code()
        entity_service.attach_response_body()

    @allure.title("Получение всех сущностей")
    def test_get_entities(
        self,
        entity_service: EntityService,
        entity: dict[str, dict[str, Any] | EntityIdModel]
    ) -> None:
        entity2 = entity_service.create_entity(*(EntityData().entity()))
        entity_service.check_status_code()
        entity3 = entity_service.create_entity(*(EntityData().entity()))
        entity_service.check_status_code()
        response = entity_service.get_entities()
        entity_service.check_status_code()
        entity_service.attach_response_body()
        response_entities = response.entity
        response_entities_ids = [ent.id for ent in response_entities]
        assert entity["model"].root in response_entities_ids and \
            entity2["model"].root in response_entities_ids and \
            entity3["model"].root in response_entities_ids
        entity_service.delete_entity(entity2["model"].root)
        entity_service.check_status_code(204)
        entity_service.delete_entity(entity3["model"].root)
        entity_service.check_status_code(204)

    @allure.title("Обновление сущности")
    def test_update_entity(
        self,
        entity_service: EntityService,
        entity: dict[str, dict[str, Any] | EntityIdModel]
    ) -> None:
        updated_entity = entity_service.update_entity(
            entity["model"].root, *(EntityData().entity())
        )
        entity_service.check_status_code(204)
        entity_service.attach_response_body()
        entity_service.get_entity(entity["model"].root)
        entity_service.check_status_code()
