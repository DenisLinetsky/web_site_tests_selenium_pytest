import pytest
from main.contact_us.home_page import HomePage
from main.contact_us.contact_us_page import ContactUsPage  # Import the ContactUsPage class


@pytest.mark.special
def test_contact_us_form(driver):
    home_page = HomePage(driver, "https://automationexercise.com/")
    contact_us_page = ContactUsPage(driver)  # Create an instance of ContactUsPage

    # Open the home page
    home_page.open()  # Assuming you have defined the `open` method in the HomePage class

    # Click on 'Contact Us' button
    home_page.click_contact_us()

    # Verify 'GET IN TOUCH' is visible
    assert contact_us_page.is_get_in_touch_visible()

    # Enter name, email, subject, and message
    contact_us_page.enter_details("John Doe", "john@example.com", "Subject", "This is a message.")

    # Upload file (if needed)
    # contact_us_page.upload_file("path/to/file")

    # Click 'Submit' button
    contact_us_page.click_submit()

    # Click OK button
    contact_us_page.click_ok_button()

    # Verify success message is visible
    assert contact_us_page.is_success_message_visible()

    # Click 'Home' button and verify that we've landed back on the home page
    contact_us_page.click_home()
    assert home_page.is_home_page_visible()


