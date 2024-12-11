import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from main.register_user.home_page import HomePage
from main.register_user.signup_login_page import SignupLoginPage
from main.register_user.account_information_page import AccountInformationPage
from main.register_user.account_created_page import AccountCreatedPage
from main.register_user.account_deletion_page import AccountDeletionPage

@pytest.fixture(scope="module")
def driver():
    chrome_driver_path = r"C:/Users/denis/Downloads/chromedriver-win64/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    yield driver
    driver.quit()

def test_signup_and_delete_account(driver):
    driver.get("http://automationexercise.com")
    assert "Automation Exercise" in driver.title

    home_page = HomePage(driver)
    home_page.click_signup_login()
    assert "Login" in driver.title

    signup_login_page = SignupLoginPage(driver)
    signup_login_page.enter_name("Test Name")
    signup_login_page.enter_email("denislinec12@gmail.com")
    signup_login_page.click_signup()
    time.sleep(7)


    account_info_page = AccountInformationPage(driver)
    # Verify elements are present
    assert driver.find_element(By.ID, 'id_gender1').is_displayed()
    assert driver.find_element(By.NAME, 'password').is_displayed()
    assert driver.find_element(By.NAME, 'days').is_displayed()
    assert driver.find_element(By.NAME, 'months').is_displayed()
    assert driver.find_element(By.NAME, 'years').is_displayed()
    assert driver.find_element(By.NAME, 'first_name').is_displayed()
    assert driver.find_element(By.NAME, 'last_name').is_displayed()
    assert driver.find_element(By.NAME, 'company').is_displayed()
    assert driver.find_element(By.NAME, 'address1').is_displayed()
    assert driver.find_element(By.NAME, 'address2').is_displayed()
    assert driver.find_element(By.NAME, 'country').is_displayed()
    assert driver.find_element(By.NAME, 'state').is_displayed()
    assert driver.find_element(By.NAME, 'city').is_displayed()
    assert driver.find_element(By.NAME, 'zipcode').is_displayed()
    assert driver.find_element(By.NAME, 'mobile_number').is_displayed()
    account_info_page.fill_account_information("testpassword", "1", "January", "2000",
                                               "Test", "User", "TestCompany", "123 Test St",
                                               "Suite 1", "United States", "New York", "New York",
                                               "10001", "1234567890")

    account_info_page.click_create_account()

    # Assert the presence of 'Account Created!' message
    assert driver.find_element(By.XPATH, '//b[text()="Account Created!"]').is_displayed()

    account_created_page = AccountCreatedPage(driver)
    account_created_page.click_continue()

    # Assert the presence of 'Logged in as Test Name' text
    # assert "Logged in as Test Name" in driver.page_source

    account_deletion_page = AccountDeletionPage(driver)
    account_deletion_page.click_delete_account()

    # Assert the presence of 'ACCOUNT DELETED!' message
    assert driver.find_element(By.XPATH, '//b[text()="Account Deleted!"]').is_displayed()
    time.sleep(7)
    account_deletion_page.click_continue_confirm()
