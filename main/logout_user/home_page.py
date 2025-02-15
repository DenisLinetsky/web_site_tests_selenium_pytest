from selenium.webdriver.common.by import By
from main.logout_user.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver = driver
        self.url = url
        self.signup_login_button = (By.XPATH, "//a[@href='/login']")

    def open(self):
        self.driver.get(self.url)

    def click_signup_login(self):
        self.wait_for_element(*self.signup_login_button).click()

