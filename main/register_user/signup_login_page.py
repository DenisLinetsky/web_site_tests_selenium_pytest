from selenium.webdriver.common.by import By

class SignupLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.NAME, 'name')
        self.email_input = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
        self.signup_button = (By.XPATH, '//button[text()="Signup"]')
        self.error_message = (By.XPATH, "//p[contains(text(),'Email Address already exist!')]")

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()

    def is_error_message_visible(self):
        return self.driver.find_element(*self.error_message).is_displayed()
