from typing import Any

import allure
import pytest

from config.models import EntityIdModel
from data.entity import EntityData
from tests.base_test import BaseTest


@allure.feature("Сущность")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
class TestEntity(BaseTest):

    @allure.title("Создание сущности")
    def test_create_entity(
        self, entity: dict[str, dict[str, Any] | EntityIdModel]
    ) -> None:
        self.entity.attach_response_body()
        response = self.entity.get_entity(entity["model"].root)
        self.entity.check_status_code()
        self.entity.check_field(
            "id",
            response.id,
            entity["model"].root
        )
        self.entity.check_field(
            "title",
            response.title,
            entity["payloads"]["title"]
        )
        self.entity.check_field(
            "verified",
            response.verified,
            entity["payloads"]["verified"]
        )
        self.entity.check_field(
            "addition(id)",
            response.addition.id,
            entity["model"].root
        )
        self.entity.check_field(
            "addition(additional_info)",
            response.addition.additional_info,
            entity["payloads"]["addition"]["additional_info"]
        )
        self.entity.check_field(
            "addition(additional_number)",
            response.addition.additional_number,
            entity["payloads"]["addition"]["additional_number"]
        )
        self.entity.check_field(
            "important_numbers",
            response.important_numbers,
            entity["payloads"]["important_numbers"]
        )

    @allure.title("Удаление сущности")
    def test_delete_entity(self) -> None:
        entity = self.entity.create_entity(*(EntityData().entity()))
        self.entity.check_status_code()
        self.entity.delete_entity(entity["model"].root)
        self.entity.check_status_code(204)
        self.entity.attach_response_body()
        self.entity.get_entity(entity["model"].root)
        self.entity.check_status_code(404)

    @allure.title("Получение сущности")
    def test_get_entity(
        self, entity: dict[str, dict[str, Any] | EntityIdModel]
    ) -> None:
        response = self.entity.get_entity(entity["model"].root)
        self.entity.check_status_code()
        self.entity.attach_response_body()
        self.entity.check_field(
            "id",
            response.id,
            entity["model"].root
        )
        self.entity.check_field(
            "title",
            response.title,
            entity["payloads"]["title"]
        )
        self.entity.check_field(
            "verified",
            response.verified,
            entity["payloads"]["verified"]
        )
        self.entity.check_field(
            "addition(id)",
            response.addition.id,
            entity["model"].root
        )
        self.entity.check_field(
            "addition(additional_info)",
            response.addition.additional_info,
            entity["payloads"]["addition"]["additional_info"]
        )
        self.entity.check_field(
            "addition(additional_number)",
            response.addition.additional_number,
            entity["payloads"]["addition"]["additional_number"]
        )
        self.entity.check_field(
            "important_numbers",
            response.important_numbers,
            entity["payloads"]["important_numbers"]
        )

    @allure.title("Получение всех сущностей")
    def test_get_entities(
        self, entity: dict[str, dict[str, Any] | EntityIdModel]
    ) -> None:
        entity2 = self.entity.create_entity(*(EntityData().entity()))
        self.entity.check_status_code()
        entity3 = self.entity.create_entity(*(EntityData().entity()))
        self.entity.check_status_code()
        response = self.entity.get_entities()
        self.entity.check_status_code()
        self.entity.attach_response_body()
        response_entities = response.entity
        response_entities_ids = [ent.id for ent in response_entities]
        assert entity["model"].root in response_entities_ids and \
            entity2["model"].root in response_entities_ids and \
            entity3["model"].root in response_entities_ids
        self.entity.delete_entity(entity2["model"].root)
        self.entity.check_status_code(204)
        self.entity.delete_entity(entity3["model"].root)
        self.entity.check_status_code(204)

    @allure.title("Обновление сущности")
    def test_update_entity(
        self, entity: dict[str, dict[str, Any] | EntityIdModel]
    ) -> None:
        updated_entity = self.entity.update_entity(
            entity["model"].root, *(EntityData().entity())
        )
        self.entity.check_status_code(204)
        self.entity.attach_response_body()
        response = self.entity.get_entity(entity["model"].root)
        self.entity.check_status_code()
        self.entity.check_field(
            "id",
            response.id,
            entity["model"].root
        )
        self.entity.check_field(
            "title",
            response.title,
            updated_entity["payloads"]["title"]
        )
        self.entity.check_field(
            "verified",
            response.verified,
            updated_entity["payloads"]["verified"]
        )
        self.entity.check_field(
            "addition(id)",
            response.addition.id,
            entity["model"].root
        )
        self.entity.check_field(
            "addition(additional_info)",
            response.addition.additional_info,
            updated_entity["payloads"]["addition"]["additional_info"]
        )
        self.entity.check_field(
            "addition(additional_number)",
            response.addition.additional_number,
            updated_entity["payloads"]["addition"]["additional_number"]
        )
        self.entity.check_field(
            "important_numbers",
            response.important_numbers,
            updated_entity["payloads"]["important_numbers"]
        )
