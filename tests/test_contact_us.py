import pytest
from selenium import webdriver
from main.contact_us.home_page import HomePage
from main.contact_us.contact_us_page import ContactUsPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path='C:/Users/denis/Downloads/chromedriver-win64/chromedriver.exe')
    driver.maximize_window()
    driver.get("http://automationexercise.com")
    request.cls.driver = driver
    request.cls.home_page = HomePage(driver)
    request.cls.contact_us_page = ContactUsPage(driver)
    # Make sure the teardown happens after test execution
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestContactUs:

    def test_home_page_is_visible(self):
        assert self.home_page.is_home_page_visible()

    def test_contact_us_form(self):
        # Click on 'Contact Us' button
        self.home_page.click_contact_us()

        # Verify 'GET IN TOUCH' is visible
        assert self.contact_us_page.is_get_in_touch_visible()

        # Enter name, email, subject, and message
        self.contact_us_page.enter_details("John Doe", "john@example.com", "Subject", "This is a message.")

        # Upload file
        # self.contact_us_page.upload_file("path/to/file")

        # Click 'Submit' button
        self.contact_us_page.click_submit()

        # Click OK button
        self.contact_us_page.click_ok_button()

        # Verify success message is visible
        assert self.contact_us_page.is_success_message_visible()

        # Click 'Home' button and verify that we've landed back on the home page
        self.contact_us_page.click_home()
        assert self.home_page.is_home_page_visible()
