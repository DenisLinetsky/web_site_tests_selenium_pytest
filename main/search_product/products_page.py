from main.search_product.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_RESULTS = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    PRODUCT_ITEMS = (By.CLASS_NAME, "features_items")

    def __init__(self, driver):
        super().__init__(driver)  # Initialize base class
        self.url = "https://automationexercise.com/products"

    def open(self):
        self.driver.get(self.url)

    def search_product(self, product_name):
        self.enter_text(*self.SEARCH_INPUT, product_name)
        self.click_element(*self.SEARCH_BUTTON)

    def is_search_results_visible(self):
        return self.find_element(*self.SEARCH_RESULTS).is_displayed()

    def are_products_listed(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS)) > 0

