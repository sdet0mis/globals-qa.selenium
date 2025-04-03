from typing import Generator, Any

import pytest

from config.models import EntityIdModel
from data.entity import EntityData


@pytest.fixture()
def entity(
    request: pytest.FixtureRequest
) -> Generator[EntityIdModel, Any, None]:
    entity_service = request.getfixturevalue("setup")
    entity = entity_service.create_entity(*(EntityData().entity()))
    entity_service.check_status_code()
    yield entity
    entity_service.delete_entity(entity["model"].root)
    entity_service.check_status_code(204)
