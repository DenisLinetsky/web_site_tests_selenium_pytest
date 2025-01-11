from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_element(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))
