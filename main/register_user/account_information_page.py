from selenium.webdriver.common.by import By

class AccountInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.title_mr = (By.ID, 'id_gender1')
        self.password_input = (By.NAME, 'password')
        self.dob_day = (By.NAME, 'days')
        self.dob_month = (By.NAME, 'months')
        self.dob_year = (By.NAME, 'years')
        self.newsletter_checkbox = (By.NAME, 'newsletter')
        self.offers_checkbox = (By.NAME, 'optin')
        self.first_name = (By.NAME, 'first_name')
        self.last_name = (By.NAME, 'last_name')
        self.company = (By.NAME, 'company')
        self.address1 = (By.NAME, 'address1')
        self.address2 = (By.NAME, 'address2')
        self.country = (By.NAME, 'country')
        self.state = (By.NAME, 'state')
        self.city = (By.NAME, 'city')
        self.zipcode = (By.NAME, 'zipcode')
        self.mobile_number = (By.NAME, 'mobile_number')
        self.create_account_button = (By.XPATH, '//button[text()="Create Account"]')

    def fill_account_information(self, password, day, month, year, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile_number):
        self.driver.find_element(*self.title_mr).click()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.dob_day).send_keys(day)
        self.driver.find_element(*self.dob_month).send_keys(month)
        self.driver.find_element(*self.dob_year).send_keys(year)
        self.driver.find_element(*self.newsletter_checkbox).click()
        self.driver.find_element(*self.offers_checkbox).click()
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.company).send_keys(company)
        self.driver.find_element(*self.address1).send_keys(address1)
        self.driver.find_element(*self.address2).send_keys(address2)
        self.driver.find_element(*self.country).send_keys(country)
        self.driver.find_element(*self.state).send_keys(state)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.zipcode).send_keys(zipcode)
        self.driver.find_element(*self.mobile_number).send_keys(mobile_number)

    def click_create_account(self):
        self.driver.find_element(*self.create_account_button).click()
