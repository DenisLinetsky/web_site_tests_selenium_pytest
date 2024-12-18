from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SIGNUP_LOGIN_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://automationexercise.com"

    def open(self):
        self.driver.get(self.url)

    def click_signup_login(self):
        self.find_element(*self.SIGNUP_LOGIN_BUTTON).click()
