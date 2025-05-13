from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def click_element(self, by, locator):
        self.find_element(by, locator).click()

    def enter_text(self, by, locator, text):
        self.find_element(by, locator).send_keys(text)
