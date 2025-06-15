from selenium.webdriver.common.by import By


class AuthLocators:
    LOGIN = (By.NAME, "login")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "add-btn")
    LINK_ADD_USER = (By.CSS_SELECTOR, 'a[href="/add-user"]')
