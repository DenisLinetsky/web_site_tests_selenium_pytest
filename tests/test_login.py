import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from main.login_user_with_correct_email_and_password.home_page import HomePage
from main.login_user_with_correct_email_and_password.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    chrome_driver_path = r"C:/Users/denis/Downloads/chromedriver-win64/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    yield driver
    driver.quit()

@pytest.mark.create
def test_login_and_delete_account(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    # Step 1: Launch browser and navigate to the URL
    home_page.open()
    driver.maximize_window()

    # Step 2: Verify that home page is visible successfully
    assert "Automation Exercise" in driver.title

    # Step 3: Click on 'Signup / Login' button
    home_page.click_signup_login()

    # Step 4: Verify 'Login to your account' is visible
    assert login_page.verify_login_form()

    # Step 5: Enter correct email address and password
    login_page.login("denislinec13@gmail.com", "testpassword")

    # Step 6: Verify that 'Logged in as username' is visible
    # assert login_page.verify_logged_in("username")

    # Step 7: Click 'Delete Account' button
    login_page.delete_account()
    time.sleep(8)

    # Assert the presence of 'ACCOUNT DELETED!' message
    # assert driver.find_element(By.XPATH, '//b[text()="Account Deleted!"]').is_displayed()
    # time.sleep(7)

    continue_button_confirm = driver.find_element(By.XPATH, '//a[text()="Continue"]')
    continue_button_confirm.click()

    driver.quit()
