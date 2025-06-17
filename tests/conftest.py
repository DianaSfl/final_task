import os
import tempfile
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api_client.client import FormClient
from api_client.models.add_user import AddUserModel
from api_client.models.register import RegisterModel
from pages.add_user_page import addUserPage
from pages.auth_page import AuthPage

logger = logging.getLogger("add_user_tests")


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        default="http://158.160.87.146:5000",
        help="API URL"
    )
    parser.addoption(
        "--url",
        action="store",
        default="http://158.160.87.146:5000/login",
        help="URL"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Base application URL"
    )


@pytest.fixture(scope="session")
def api_client(request):
    url = request.config.getoption("--api-url")
    client = FormClient(url=url)
    return client


@pytest.fixture(scope="session")
def driver(request):
    is_headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument("window-size=1920x1080")
    if is_headless:
        chrome_options.add_argument("--headless=new")
    logger.info(f"Headless is {is_headless}")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def auth_page(driver, request):
    url = request.config.getoption('--url')
    driver.get(url)
    auth_page = AuthPage(driver)
    return auth_page


@pytest.fixture(scope="session")
def auth_admin(auth_page, api_client):
    body = RegisterModel.random()
    response = api_client.register_admin(body=body)
    auth_page.login(login_text=body['login'], password_text=body['password'])


@pytest.fixture(scope="session")
def add_user_page(driver):
    add_user_page = addUserPage(driver)
    return add_user_page


@pytest.fixture(autouse=True)
def reset_state(add_user_page):
    # Автоматически обновляет страницу перед каждым тестом.
    add_user_page.refresh_page()
    yield


@pytest.fixture(scope="session")
def default_user_data():
    data_user = AddUserModel.random()
    return data_user
