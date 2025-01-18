from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.get_in_touch_text = (By.XPATH, "//h2[contains(text(),'Get In Touch')]")
        self.name_field = (By.NAME, "name")
        self.email_field = (By.NAME, "email")
        self.subject_field = (By.NAME, "subject")
        self.message_field = (By.NAME, "message")
        self.upload_field = (By.NAME, "upload_file")
        self.submit_button = (By.NAME, "submit")
        self.success_message = (By.XPATH, "//div[contains(text(),'Success!')]")
        self.home_button = (By.XPATH, "//a[contains(text(),'Home')]")

    def is_get_in_touch_visible(self):
        return self.driver.find_element(*self.get_in_touch_text).is_displayed()

    def enter_details(self, name, email, subject, message):
        self.driver.find_element(*self.name_field).send_keys(name)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.subject_field).send_keys(subject)
        self.driver.find_element(*self.message_field).send_keys(message)

    def upload_file(self, file_path):
        self.driver.find_element(*self.upload_field).send_keys(file_path)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def click_ok_button(self):
        Alert(self.driver).accept()

    def is_success_message_visible(self):
        return self.driver.find_element(*self.success_message).is_displayed()

    def click_home(self):
        self.driver.find_element(*self.home_button).click()

    def is_home_page_visible(self):
        return self.driver.find_element(*self.home_button).is_displayed()
