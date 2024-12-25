import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils import login_button, password_button, click_button
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
@pytest.fixture(scope="module")
def base_url():
    return "http://10.10.215.5"

@pytest.fixture(scope="module")
def test_user():
    return {
        "email": "test@protei.ru",
        "password": "1111"
    }

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def login(browser, base_url, test_user):
    browser.get(base_url)
    login_button(browser, test_user["email"])
    password_button(browser, test_user["password"])
    click_button(browser)
    yield browser

@pytest.fixture
def header_main_page(browser):
    WebDriverWait(browser, 20).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))
    yield


@pytest.fixture
def header_error_message(browser):
    WebDriverWait(browser, 20).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p")))
    yield