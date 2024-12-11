from selenium.webdriver.common.by import By

class AccountDeletionPage:
    def __init__(self, driver):
        self.driver = driver
        self.delete_account_button = (By.LINK_TEXT, 'Delete Account')
        self.continue_button_confirm = (By.XPATH, '//a[text()="Continue"]')

    def click_delete_account(self):
        self.driver.find_element(*self.delete_account_button).click()

    def click_continue_confirm(self):
        self.driver.find_element(*self.continue_button_confirm).click()
