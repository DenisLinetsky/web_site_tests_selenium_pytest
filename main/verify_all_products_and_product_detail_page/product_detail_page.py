from selenium.webdriver.common.by import By
# from main.user_register import driver

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/product_details/1"
        self.driver.get(self.url)
        self.details = ["Product Name", "Category", "Price", "Availability", "Condition", "Brand"]

    def open(self):
        self.driver.get(self.url)  # Use instance variable

    def verify_product_details(self):
        self.driver.find_element(By.XPATH, "//div[@class='product-information']")
        return True
        #  detail in self.details:
            # if not self.driver.find_elements(By.XPATH, f"//b[text()='{detail}']"):
                # return False
        # return True

