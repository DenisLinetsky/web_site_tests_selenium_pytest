from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.signup_login_button = (By.LINK_TEXT, 'Signup / Login')

    def click_signup_login(self):
        self.driver.find_element(*self.signup_login_button).click()
