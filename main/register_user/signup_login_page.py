from selenium.webdriver.common.by import By

class SignupLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.NAME, 'name')
        self.email_input = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
        self.signup_button = (By.XPATH, '//button[text()="Signup"]')

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()
