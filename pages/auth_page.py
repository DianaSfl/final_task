import logging

from locators.add_user_locators import AddUserFormLocators
from locators.auth_locators import AuthLocators
from pages.base_page import BasePage

logger = logging.getLogger("add_user_tests")


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, login_text, password_text):
        self.fill(value=login_text, locator=AuthLocators.LOGIN)
        self.fill(value=password_text, locator=AuthLocators.PASSWORD)
        self.click(locator=AuthLocators.LOGIN_BUTTON)
        self.wait_url(locator=AddUserFormLocators.LINK_LIST_USER)
        text = self.text(locator=AddUserFormLocators.LIST_USER)
        logger.info(f"Страница: {text}")

