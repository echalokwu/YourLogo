import pytest
from selenium import webdriver
from pages.registration import RegistrationPage


@pytest.fixture()
def test_setUp():
    global driver
    driver = webdriver.Chrome(executable_path="/Users/echalo/Desktop/YourLogo/automation/drivers/chromedriver")
    driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()


def test_verify_user_can_register(test_setUp):
    register = RegistrationPage(driver)

    register.enter_create_account_email("iwe301@gmail.com")
    register.click_create_account_button()
    register.select_title()
    register.enter_customer_firstName("iwe")
    register.enter_customer_lastName("iwer")
    register.enter_create_account_password("moimoi123")
    register.select_title()
    register.select_dob_day().select_by_value("24")
    register.select_dob_month().select_by_value("11")
    register.select_dob_year().select_by_value("1970")
    register.enter_shipping_firstName("iwe")
    register.enter_shipping_lastName("iwe")
    register.enter_address("34 zeus dr")
    register.enter_city("Orange")
    register.select_state().select_by_visible_text("New Jersey")
    register.enter_zipCode("07502")
    register.select_country().select_by_visible_text("United States")
    register.enter_mobile("4586996666")
    register.enter_address_alia("My address")
    register.click_register_button()

