from main.login_user_with_correct_email_and_password.home_page import HomePage
from main.login_user_with_correct_email_and_password.login_page import LoginPage
from main.login_user_with_incorrect_email_and_password.invalid_login_page import LoginPage
import pytest


@pytest.mark.special
def test_invalid_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    # Step 1: Launch browser and navigate to the URL
    home_page.open()

    # Step 2: Verify that home page is visible successfully
    assert "Automation Exercise" in driver.title

    # Step 3: Click on 'Signup / Login' button
    home_page.click_signup_login()

    # Step 4: Verify 'Login to your account' is visible
    assert login_page.verify_login_form()

    # Step 5: Enter incorrect email address and password
    login_page.login("invalid@example.com", "invalidpassword")

    # Step 6: Verify error 'Your email or password is incorrect!' is visible
    assert login_page.verify_error_message()