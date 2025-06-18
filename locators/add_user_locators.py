from selenium.webdriver.common.by import By


class AddUserFormLocators:
    LINK_ADD_USER = (By.CSS_SELECTOR, 'a[href="/add-user"]')
    LINK_LIST_USER = '/users-page'
    PAGE_NAME = (By.CSS_SELECTOR, 'h2.mb-4')
    NAME = (By.ID, "name")
    AGE = (By.ID, "age")
    GENDER = (By.ID, "gender")
    DATE_BIRTH = (By.ID, "date_birthday")
    ACTIVE = (By.ID, "isActive")
    ADD_BTN = (By.ID, "add-btn")
    RESULT_TEXT = (By.CSS_SELECTOR, 'div.alert')
    EMPTY_NAME_TEXT = (By.ID, 'nameError')
    EMPTY_AGE_TEXT = (By.ID, 'ageError')
