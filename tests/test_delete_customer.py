import allure
import pytest

from data.customers import customer_to_delete
from tests.base_test import BaseTest


@allure.feature("Удаление клиента")
class TestDeleteCustomer(BaseTest):

    @allure.title("Удаление клиента")
    @allure.description(
        "Удаление клиента с тем именем, у которого длина будет ближе \
            к среднему арифметическому"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_delete_customer(self):
        self.manager_page.open_page()
        self.manager_page.click_customers_button()
        customer = customer_to_delete(
            self.customers_page.get_customers_first_names()
        )
        self.customers_page.make_screenshot("Скриншот страницы клиентов")
        self.customers_page.click_delete_button(
            customer["customer_id"], customer["name"]
        )
        assert customer["name"] not in (
                self.customers_page.get_customers_first_names()
        ), f"Клиент {customer['name']} не удален"
        self.customers_page.fill_search_customer_field(customer["name"])
        self.customers_page.make_screenshot(
            "Скриншот страницы клиентов после удаления клиента"
        )
