from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.add_user_locators import AddUserFormLocators
from pages.base_page import BasePage


class addUserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_user(self, name_text, age_text, gender_text, data_birth_text, active_check):
        self.fill(value=name_text, locator=AddUserFormLocators.NAME)
        self.fill(value=age_text, locator=AddUserFormLocators.AGE)
        self.fill(value=gender_text, locator=AddUserFormLocators.GENDER)
        self.fill(value=data_birth_text, locator=AddUserFormLocators.DATE_BIRTH)
        self.fill(value=active_check, locator=AddUserFormLocators.ACTIVE)
        self.click(locator=AddUserFormLocators.ADD_BTN)

    def get_result_text(self):
        return self.text(AddUserFormLocators.RESULT_TEXT)

    def get_empty_name_text(self):
        return self.text(AddUserFormLocators.EMPTY_NAME_TEXT)

    def get_empty_age_text(self):
        return self.text(AddUserFormLocators.EMPTY_AGE_TEXT)

    def refresh_page(self):
        self.refresh()
