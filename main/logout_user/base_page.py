from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_for_element(self, by, value, condition=EC.presence_of_element_located, timeout=15):
        return WebDriverWait(self.driver, timeout).until(condition((by, value)))

