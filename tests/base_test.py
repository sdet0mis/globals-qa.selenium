import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.add_customer import AddCustomerPage
from pages.customers import CustomersPage
from pages.manager import ManagerPage


@allure.epic("UI тесты")
class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, request: pytest.FixtureRequest, driver: WebDriver) -> None:
        request.cls.driver = driver
        request.cls.add_customer_page = AddCustomerPage(driver)
        request.cls.customers_page = CustomersPage(driver)
        request.cls.manager_page = ManagerPage(driver)
