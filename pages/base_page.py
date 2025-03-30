from time import sleep

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def open_page(self) -> None:
        with allure.step(f"Перейти по ссылке {self.URL}"):
            self.driver.get(self.URL)

    def find_elements(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def fill_field(self, locator: tuple, data: str) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator)).send_keys(
            data
        )

    def clear_field(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator)).clear()

    def get_fields_with_invalid_values(self) -> list[str]:
        return [field.get_attribute("placeholder") for field in (
            self.wait.until(EC.presence_of_all_elements_located(
                self.INVALID_FIELDS
            ))
        )]

    def click(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_alert(self) -> WebElement:
        return self.wait.until(EC.alert_is_present())

    def make_screenshot(self, name: str, sleep_time: int = 0) -> None:
        sleep(sleep_time)
        allure.attach(
            name=name,
            body=self.driver.get_screenshot_as_png(),
            attachment_type=AttachmentType.PNG
        )
