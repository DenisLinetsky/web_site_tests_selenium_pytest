import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from main.logout_user.home_page import HomePage
from main.logout_user.login_page import LoginPage

def test_logout_user(driver):
    home_page = HomePage(driver, "https://automationexercise.com/")
    login_page = LoginPage(driver)

    # Step 1: Launch browser and navigate to the URL
    home_page.open()
    driver.maximize_window()

    # Step 2: Verify home page
    assert "Automation Exercise" in driver.title

    # Step 3: Click on 'Signup / Login' button
    home_page.click_signup_login()

    # Step 4: Verify 'Login to your account' is visible
    assert login_page.wait_for_element(*login_page.email_input).is_displayed()

    # Step 5: Enter correct email address and password
    login_page.login("denislinec13@gmail.com", "testpassword")

    # Step 6: Verify 'Logged in as username' is visible
    assert login_page.verify_logged_in()

    # Step 7: Click 'Logout' button
    login_page.logout()

    # Step 8: Verify that user is navigated to login page
    assert login_page.wait_for_element(*login_page.email_input).is_displayed()
