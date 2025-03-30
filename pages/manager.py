import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ManagerPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"  # noqa
        self.ADD_CUSTOMER_BUTTON = (
            By.XPATH, "//button[@ng-class='btnClass1']"
        )
        self.CUSTOMERS_BUTTON = (By.XPATH, "//button[@ng-class='btnClass3']")

    @allure.step("Нажать на кнопку 'Add Customer'")
    def click_add_customer_button(self) -> None:
        self.click(self.ADD_CUSTOMER_BUTTON)

    @allure.step("Нажать на кнопку 'Customers'")
    def click_customers_button(self) -> None:
        self.click(self.CUSTOMERS_BUTTON)
