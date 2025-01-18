from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.contact_us_button = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a')

    def click_contact_us(self):
        self.driver.find_element(*self.contact_us_button).click()

    def is_home_page_visible(self):
        return self.driver.find_element(*self.contact_us_button).is_displayed()
