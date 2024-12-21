from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    LOGIN_FORM = (By.XPATH, '//*[@id="form"]/div/div/div[1]/div/form/input[2]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')
    LOGGED_IN_AS = (By.XPATH, '//b[text()="Logged in as"]')
    DELETE_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Delete Account')
    ACCOUNT_DELETED = (By.NAME, 'Account Deleted!')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_login_form(self):
        return self.wait_for_element(self.LOGIN_FORM).is_displayed()

    def login(self, email, password):
        self.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.find_element(*self.LOGIN_BUTTON).click()

    def verify_logged_in(self, username):
        return self.wait_for_element(self.LOGGED_IN_AS).is_displayed()

    def delete_account(self):
        self.find_element(*self.DELETE_ACCOUNT_BUTTON).click()

    def verify_account_deleted(self):
        return self.wait_for_element(self.ACCOUNT_DELETED).is_displayed()
