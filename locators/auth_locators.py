from selenium.webdriver.common.by import By


class AuthLocators:
    LOGIN = (By.NAME, "login")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "add-btn")
