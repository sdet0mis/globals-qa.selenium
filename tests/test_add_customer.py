import allure
import pytest

from tests.base_test import BaseTest


@allure.feature("Создание клиента")
class TestAddCustomer(BaseTest):

    @allure.title("Создание клиента")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_add_customer(self, get_new_customer):
        self.manager_page.open_page()
        self.manager_page.click_add_customer_button()
        self.add_customer_page.enter_first_name(get_new_customer["first_name"])
        self.add_customer_page.enter_last_name(get_new_customer["last_name"])
        self.add_customer_page.enter_post_code(get_new_customer["post_code"])
        self.add_customer_page.make_screenshot(
            "Скриншот страницы создания клиента"
        )
        self.add_customer_page.click_add_customer_button_2()
        alert = self.add_customer_page.get_alert()
        assert (
            "Customer added successfully with customer id :" in alert.text
        ), f"Клиент {get_new_customer['first_name']} не создан"
        customer_id = alert.text.split(":")[1]
        alert.accept()
        self.add_customer_page.click_customers_button()
        self.customers_page.fill_search_customer_field(
            get_new_customer["first_name"]
        )
        self.customers_page.make_screenshot("Скриншот страницы клиентов")
        assert get_new_customer["first_name"] in (
            self.customers_page.get_customers_first_names()
        ), f"Клиент {get_new_customer['first_name']} не найден"
        self.customers_page.clear_search_customer_field()
        self.customers_page.click_delete_button(
            customer_id, get_new_customer["first_name"]
        )
        assert get_new_customer["first_name"] not in (
            self.customers_page.get_customers_first_names()
        ), f"Клиент {get_new_customer['first_name']} не удален"

    @allure.title("Создание клиента без фамилии")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_add_customer_without_last_name(self, get_new_customer):
        self.manager_page.open_page()
        self.manager_page.click_add_customer_button()
        self.add_customer_page.enter_first_name(get_new_customer["first_name"])
        self.add_customer_page.enter_post_code(get_new_customer["post_code"])
        self.add_customer_page.click_add_customer_button_2()
        invalid_fields = (
            self.add_customer_page.get_fields_with_invalid_values()
        )
        self.add_customer_page.make_screenshot(
            "Скриншот страницы создания клиента", sleep_time=1
        )
        assert (
            "".join(invalid_fields) == "Last Name"
        ), "В поле Last Name не сработала валидация"
