from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.test_cases_button = (By.LINK_TEXT, 'Test Cases')

    def open_home_page(self):
        self.driver.get("http://automationexercise.com")

    def verify_home_page(self):
        assert "Automation Exercise" in self.driver.title

    def click_test_cases(self):
        self.driver.find_element(*self.test_cases_button).click()
