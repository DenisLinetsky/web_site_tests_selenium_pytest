from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/products"  # Define URL
        self.driver.get(self.url)
        self.view_product_button = (By.XPATH, "(//a[text()='View Product'])[1]")  # Correct XPath

    def open(self):
        self.driver.get(self.url)  # Use instance variable

    def verify_products_list_visible(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "features_items")) > 0

    def click_first_product(self):
        self.driver.find_element(*self.view_product_button).click()  # Correct usage

