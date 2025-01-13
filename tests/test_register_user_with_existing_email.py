import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from main.register_user import signup_login_page
from main.register_user.home_page import HomePage
from main.register_user.signup_login_page import SignupLoginPage

@pytest.fixture(scope="module")
def driver():
    chrome_driver_path = r"C:/Users/denis/Downloads/chromedriver-win64/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    yield driver
    driver.quit()


@pytest.mark.special
def test_existing_email_signup(driver):
    home_page = HomePage(driver)
    signup_page = SignupLoginPage(driver)

    # Step 1: Launch browser and navigate to the URL
    driver.get("http://automationexercise.com")

    # Step 2: Verify home page is visible
    assert driver.title == "Automation Exercise"

    home_page = HomePage(driver)
    home_page.click_signup_login()
    assert "Login" in driver.title

    signup_login_page = SignupLoginPage(driver)
    signup_login_page.enter_name("Test Name")
    signup_login_page.enter_email("denislinec13@gmail.com")
    signup_login_page.click_signup()

    # Step 7: Verify error 'Email Address already exist!' is visible
    assert signup_login_page.is_error_message_visible()
