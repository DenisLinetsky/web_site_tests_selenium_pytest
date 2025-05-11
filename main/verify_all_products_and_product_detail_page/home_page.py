from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://automationexercise.com"
        self.products_button = (By.XPATH, "//a[@href='/products']")

    def open(self):
        self.driver.get(self.url)

    def navigate_to_products(self):
        self.driver.find_element(*self.products_button).click()
