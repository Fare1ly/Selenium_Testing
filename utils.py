from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def login_button(browser, email):
    login_field = WebDriverWait(browser, 20).until(
        expected_conditions.presence_of_element_located((By.ID, "loginEmail"))
    )
    login_field.send_keys(email)

def password_button(browser, password):
    password_field = WebDriverWait(browser, 20).until(
        expected_conditions.presence_of_element_located((By.ID, "loginPassword"))
    )
    password_field.send_keys(password)

def click_button(browser):
    auth_button = browser.find_element(By.CSS_SELECTOR, ".uk-button")
    auth_button.click()


