import allure
import pytest

from services.entity import EntityService


@allure.epic("API")
class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.entity = EntityService()
        return self.entity
