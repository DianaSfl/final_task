from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.auth_locators import AuthLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, login_text, password_text):
        self.fill(value=login_text, locator=AuthLocators.LOGIN)
        self.fill(value=password_text, locator=AuthLocators.PASSWORD)
        self.click(locator=AuthLocators.LOGIN_BUTTON)

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Список пользователей')]")),
            message="Страница после авторизации не загрузилась"
        )

        self.wait_and_click(locator=AuthLocators.LINK_ADD_USER)
