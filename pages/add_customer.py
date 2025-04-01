import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.manager import ManagerPage


class AddCustomerPage(ManagerPage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"  # noqa
        self.FIRST_NAME_FIELD = (By.XPATH, "//input[@ng-model='fName']")
        self.LAST_NAME_FIELD = (By.XPATH, "//input[@ng-model='lName']")
        self.POST_CODE_FIELD = (By.XPATH, "//input[@ng-model='postCd']")
        self.ADD_CUSTOMER_BUTTON_2 = (By.XPATH, "//button[@type='submit']")
        self.INVALID_FIELDS = (
            By.XPATH, "//input[contains(@class, 'ng-invalid')]"
        )

    @allure.step("Ввести имя {first_name} в поле 'First Name'")
    def enter_first_name(self, first_name: str) -> None:
        self.fill_field(self.FIRST_NAME_FIELD, first_name)

    @allure.step("Ввести фамилию {last_name} в поле 'Last Name'")
    def enter_last_name(self, last_name: str) -> None:
        self.fill_field(self.LAST_NAME_FIELD, last_name)

    @allure.step("Ввести почтовый индекс {post_code} в поле 'Post Code'")
    def enter_post_code(self, post_code: str) -> None:
        self.fill_field(self.POST_CODE_FIELD, post_code)

    @allure.step("Нажать на кнопку 'Add Customer' под полем 'Post Code'")
    def click_add_customer_button_2(self) -> None:
        self.click(self.ADD_CUSTOMER_BUTTON_2)
