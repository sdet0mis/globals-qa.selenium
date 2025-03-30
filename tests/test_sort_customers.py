import allure

from tests.base_test import BaseTest


@allure.feature("Сортировка клиентов")
class TestSortCustomers(BaseTest):

    @allure.title("Сортировка клиентов по имени")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_customers_by_first_name(self):
        self.manager_page.open_page()
        self.manager_page.click_customers_button()
        first_names = self.customers_page.get_customers_first_names()
        self.customers_page.make_screenshot("Скриншот страницы клиентов")
        self.customers_page.click_first_name_sort_button()
        sorted_first_names = self.customers_page.get_customers_first_names()
        self.customers_page.make_screenshot(
            "Скриншот страницы клиентов после сортировки по имени"
        )
        assert (
            sorted_first_names == sorted(first_names)
        ), "Клиенты не отсортированы"
        self.customers_page.click_first_name_sort_button()
        reverse_sorted_first_names = (
            self.customers_page.get_customers_first_names()
        )
        self.customers_page.make_screenshot(
            "Скриншот страницы клиентов после обратной сортировки по имени"
        )
        assert (
            reverse_sorted_first_names == sorted(first_names, reverse=True)
        ), "Клиенты не отсортированы в обратном порядке"
