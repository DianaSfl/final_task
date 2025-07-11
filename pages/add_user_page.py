import logging

from locators.add_user_locators import AddUserFormLocators
from pages.base_page import BasePage
from utils.logger_add_user import log_data_add_user

logger = logging.getLogger("add_user_tests")


class addUserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_user(self, name_text, age_text, gender_text, data_birth_text, active_check):
        text = self.text(locator=AddUserFormLocators.PAGE_NAME)
        logger.info(f"Название страницы: {text}")
        self.fill(value=name_text, locator=AddUserFormLocators.NAME)
        self.fill(value=age_text, locator=AddUserFormLocators.AGE)
        self.fill(value=gender_text, locator=AddUserFormLocators.GENDER)
        self.fill(value=data_birth_text, locator=AddUserFormLocators.DATE_BIRTH)
        self.fill(value=active_check, locator=AddUserFormLocators.ACTIVE)
        log_data_add_user(name_text, age_text, gender_text, data_birth_text, active_check)
        self.click(locator=AddUserFormLocators.ADD_BTN)

    def get_result_text(self):
        result = self.text(AddUserFormLocators.RESULT_TEXT)
        logger.info(f"Result: {result}")
        return result

    def get_empty_name_text(self):
        result = self.text(AddUserFormLocators.EMPTY_NAME_TEXT)
        logger.info(f"Result: {result}")
        return result

    def get_empty_age_text(self):
        result = self.text(AddUserFormLocators.EMPTY_AGE_TEXT)
        logger.info(f"Result: {result}")
        return result

    def refresh_page(self):
        self.refresh()

    def logout_admin(self):
        self.logout(locator=AddUserFormLocators.LOGOUT_BUTTON)
