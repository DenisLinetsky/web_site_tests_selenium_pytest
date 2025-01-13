from selenium.webdriver.common.by import By
from main.logout_user.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.signup_login_button = (By.XPATH, "//a[@href='/login']")

    def click_signup_login(self):
        self.wait_for_element(*self.signup_login_button).click()
