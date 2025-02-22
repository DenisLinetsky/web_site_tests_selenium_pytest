import pytest
from main.register_user.home_page import HomePage
from main.register_user.signup_login_page import SignupLoginPage


@pytest.mark.special
def test_existing_email_signup(driver):

    # Launch browser and navigate to the URL
    driver.get("http://automationexercise.com")

    # Verify home page is visible
    assert driver.title == "Automation Exercise"

    home_page = HomePage(driver)
    home_page.click_signup_login()
    assert "Login" in driver.title

    signup_login_page = SignupLoginPage(driver)
    signup_login_page.enter_name("Test Name")
    signup_login_page.enter_email("denislinec13@gmail.com")
    signup_login_page.click_signup()

    # Verify error 'Email Address already exist!' is visible
    assert signup_login_page.is_error_message_visible()
