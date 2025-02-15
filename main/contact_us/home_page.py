from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.contact_us_button = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a')

    def open(self):
        self.driver.get(self.url)

    def click_contact_us(self):
        self.driver.find_element(*self.contact_us_button).click()

    def is_home_page_visible(self):
        return self.driver.find_element(*self.contact_us_button).is_displayed()

