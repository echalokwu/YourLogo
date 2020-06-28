import pytest
from selenium import webdriver
from pages.loginPage import LoginPage
import time


@pytest.fixture
def test_setUp():
    global driver
    driver = webdriver.Chrome(executable_path="/Users/echalo/Desktop/YourLogo/automation/drivers/chromedriver")
    driver.get("http://automationpractice.com/index.php")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()


def test_verify_login_with_valid_details(test_setUp):
    login = LoginPage(driver)
    login.click_signIn_link()
    time.sleep(3)
    login.enter_email("iwe43@gmail.com")
    login.enter_password("moimoi123")
    login.click_signIn_button()
    time.sleep(5)
