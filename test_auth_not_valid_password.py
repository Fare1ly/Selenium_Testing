import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_auth(login, header_error_message):
    error_message = WebDriverWait(login, 5).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "p")))

    assert error_message.is_displayed()
    assert error_message.text == "Неверный E-Mail или пароль"