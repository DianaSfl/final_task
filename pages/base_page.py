from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator, wait_time=30):  # Увеличьте таймаут
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден за {wait_time} сек"
        )
    # def _find_element(self, locator, wait_time=10):
    #     element = WebDriverWait(self.driver, wait_time).until(
    #         EC.presence_of_element_located(locator))
    #     return element

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

    def wait_and_click(self, locator, timeout=30):  # Увеличено до 30 секунд
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator),
                message=f"Элемент {locator} не стал кликабельным за {timeout} сек"
            )
            element.click()
        except StaleElementReferenceException:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator),
                message=f"Элемент {locator} стал stale и не кликабельным за {timeout} сек"
            )
            element.click()
        except Exception as e:
            self.driver.save_screenshot("click_error.png")
            raise
    # def wait_and_click(self, locator, timeout=10):
    #     try:
    #         WebDriverWait(self.driver, timeout).until(
    #             EC.element_to_be_clickable(locator)
    #         ).click()
    #     except StaleElementReferenceException:
    #         element = WebDriverWait(self.driver, timeout).until(
    #             EC.element_to_be_clickable(locator)
    #         )
    #         element.click()

    def refresh(self):
        self.driver.refresh()
        return self
