import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from api_client.client import FormClient
from api_client.models.add_user import AddUserModel
from api_client.models.register import RegisterModel
from pages.add_user_page import addUserPage
from pages.auth_page import AuthPage


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
    chrome_options.add_argument("--window-size=1920x1080")
    if is_headless:
        chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
    # options = webdriver.ChromeOptions()
    # if os.getenv('GITHUB_ACTIONS') == 'true':
    #     options.add_argument("--headless=new")
    #     options.add_argument("--no-sandbox")
    #     options.add_argument("--disable-dev-shm-usage")
    #     options.add_argument("--disable-gpu")
    #     options.add_argument("--window-size=1920,1080")
    # else:
    #     user_data_dir = os.path.join(tempfile.mkdtemp(), "chrome_profile")
    #     options.add_argument(f"--user-data-dir={user_data_dir}")
    #     options.add_argument("--start-maximized")




@pytest.fixture(scope="session")
def auth_page(driver, request):
    url = request.config.getoption('--url')
    driver.get(url)
    try:
        auth_page = AuthPage(driver)
        yield auth_page
    finally:
        driver.quit()


@pytest.fixture(scope="session")
def auth_admin(auth_page, api_client):
    body = RegisterModel.random()
    response = api_client.register_admin(body=body)
    auth_page.login(login_text=body['login'], password_text=body['password'])


@pytest.fixture(scope="session")
def add_user_page(driver):
    try:
        add_user_page = addUserPage(driver)
        yield add_user_page
    finally:
        driver.quit()


@pytest.fixture(autouse=True)
def reset_state(add_user_page):
    # Автоматически обновляет страницу перед каждым тестом.
    add_user_page.refresh_page()
    yield

@pytest.fixture(scope="session")
def default_user_data():
    data_user = AddUserModel.random()
    return data_user
