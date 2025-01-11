import time

from selenium.webdriver.common.by import By
from main.login_user_with_correct_email_and_password.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_FORM = (By.XPATH, '//h2[text()="Login to your account"]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')
    ERROR_MESSAGE = (By.XPATH, '//*[text()="Your email or password is incorrect!"]')

    def verify_login_form(self):
        return self.wait_for_element(self.LOGIN_FORM).is_displayed()

    def login(self, email, password):
        self.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(5)

    def verify_error_message(self):
        # return self.wait_for_element(self.ERROR_MESSAGE).is_displayed()
        try:
            error_element = self.wait_for_element(self.ERROR_MESSAGE)
            # print(f"Error element found: {error_element}")
            return error_element.is_displayed()
        except Exception as e:
            # print(f"Error message not found: {e}")
            return False