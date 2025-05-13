from main.search_product.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    URL = "http://automationexercise.com"

    PRODUCTS_BUTTON = (By.XPATH, "//a[contains(text(),'Products')]")

    def navigate_to_homepage(self):
        self.driver.get(self.URL)

    def click_products(self):
        self.click_element(*self.PRODUCTS_BUTTON)

