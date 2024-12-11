from selenium.webdriver.common.by import By

class AccountCreatedPage:
    def __init__(self, driver):
        self.driver = driver
        self.continue_button = (By.XPATH, '//a[text()="Continue"]')

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
