from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
