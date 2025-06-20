from selenium.common import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import logging
logger = logging.getLogger("add_user_tests")
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator))
        return element

    def click(self, locator, wait_time=10):
        element = self._find_element(locator, wait_time)
        element.click()

    def fill(self, value: str, locator, wait_time=60):
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator, wait_time=20) -> str:
        element = self._find_element(locator, wait_time)
        return element.text

    def wait_url(self, locator, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(
            EC.url_contains(locator)
        )

    def refresh(self):
        self.driver.refresh()
        return self

    def logout(self, locator, wait_time=10):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator))
            element.click()
            logger.info("Разлогин")
        except ElementNotInteractableException:
            logger.info("Разлогин не требуется")
