from selenium.webdriver.common.by import By
from main.logout_user.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[text()='Login']")
        self.logged_in_as = (By.XPATH, "//a[contains(text(), 'Logged in as')]/b[contains(text(), 'Test Name')]")
        self.logout_button = (By.XPATH, "//a[@href='/logout']")

    def login(self, email, password):
        self.wait_for_element(*self.email_input).send_keys(email)
        self.wait_for_element(*self.password_input).send_keys(password)
        self.wait_for_element(*self.login_button).click()

    def verify_logged_in(self):
        return self.wait_for_element(*self.logged_in_as).is_displayed()

    def logout(self):
        self.wait_for_element(*self.logout_button).click()
