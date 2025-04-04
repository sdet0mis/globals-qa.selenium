from typing import Generator, Any

import pytest

from config.models import EntityIdModel
from data.entity import EntityData
from services.entity import EntityService


@pytest.fixture()
def entity_service() -> EntityService:
    entity_service = EntityService()
    return entity_service


@pytest.fixture()
def entity(
    entity_service: EntityService
) -> Generator[EntityIdModel, Any, None]:
    entity = entity_service.create_entity(*(EntityData().entity()))
    entity_service.check_status_code()
    yield entity
    entity_service.delete_entity(entity["model"].root)
    entity_service.check_status_code(204)
