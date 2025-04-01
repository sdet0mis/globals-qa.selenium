import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from data.customers import customer_to_delete
from pages.manager import ManagerPage


class CustomersPage(ManagerPage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"  # noqa
        self.SEARCH_CUSTOMER_FIELD = (
            By.XPATH, "//input[@ng-model='searchCustomer']"
        )
        self.FIRST_NAME_SORT_BUTTON = (By.XPATH, "//thead/tr/td[1]")
        self.CUSTOMERS_FIRST_NAMES = (By.XPATH, "//tbody/tr/td[1]")
        self.DELETE_BUTTON = lambda customer_id: (  # noqa
            By.XPATH,
            f"//tbody/tr[{customer_id}]//button"
        )

    @allure.step("Ввести {data} в поле 'Search Customer'")
    def fill_search_customer_field(self, data: str) -> None:
        self.fill_field(self.SEARCH_CUSTOMER_FIELD, data)

    def clear_search_customer_field(self) -> None:
        self.clear_field(self.SEARCH_CUSTOMER_FIELD)

    def get_customers_first_names(self) -> list[str]:
        return [name.text for name in self.find_elements(
            self.CUSTOMERS_FIRST_NAMES
        )]

    @allure.step("Нажать на заголовок столбца 'First Name' в таблице клиентов")
    def click_first_name_sort_button(self) -> None:
        self.click(self.FIRST_NAME_SORT_BUTTON)

    def click_delete_button(self, customer_id: str, name: str) -> None:
        with allure.step(
            f"Нажать на кнопку 'Delete' в строке клиента с именем {name}"
        ):
            self.click(self.DELETE_BUTTON(customer_id))

    def click_delete_button_for_customer_with_average_name_length(
        self
    ) -> dict[str, str]:
        customer = customer_to_delete(self.get_customers_first_names())
        self.click_delete_button(customer["customer_id"], customer["name"])
        return customer
