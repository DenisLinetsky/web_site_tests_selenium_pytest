import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from main.logout_user.home_page import HomePage
from main.logout_user.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    chrome_driver_path = r"C:/Users/denis/Downloads/chromedriver-win64/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get("http://automationexercise.com")
    yield driver
    driver.quit()

def test_logout_user(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    # Step 1: Verify home page
    assert "Automation Exercise" in driver.title

    # Step 2: Click on 'Signup / Login' button
    home_page.click_signup_login()

    # Step 3: Verify 'Login to your account' is visible
    assert login_page.wait_for_element(*login_page.email_input).is_displayed()

    # Step 4: Enter correct email address and password
    login_page.login("denislinec13@gmail.com", "testpassword")

    # Step 5: Verify 'Logged in as username' is visible
    assert login_page.verify_logged_in()

    # Step 6: Click 'Logout' button
    login_page.logout()

    # Step 7: Verify that user is navigated to login page
    assert login_page.wait_for_element(*login_page.email_input).is_displayed()
