import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_auth(login, header_main_page):
    main_title = WebDriverWait(login, 20).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))
    assert main_title.is_displayed()
    assert main_title.text == "Добро пожаловать!"


