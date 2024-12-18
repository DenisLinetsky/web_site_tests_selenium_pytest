import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Path to the newly downloaded ChromeDriver
chrome_driver_path = r"C:/Users/denis/Downloads/chromedriver-win64/chromedriver.exe"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start browser maximized
chrome_options.add_argument("--disable-infobars")  # Disable infobars
#hrome_options.add_argument("--incognito")  # Open browser in incognito mode

# Initialize ChromeDriver with options
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

try:
    # Open URL: http://automationexercise.com
    driver.get("http://automationexercise.com")

    # Click on 'Signup / Login' button
    signup_login_button = driver.find_element(By.LINK_TEXT, 'Signup / Login')
    signup_login_button.click()

    # Enter name and email address
    name_input = driver.find_element(By.NAME, 'name')
    name_input.send_keys("Test Name")
    email_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="signup-email"]')
    email_input.click()
    email_input.send_keys("denislinec13@gmail.com")

    # Click 'Signup' button
    signup_button = driver.find_element(By.XPATH, '//button[text()="Signup"]')
    signup_button.click()
    time.sleep(7)

    # Fill details: Title, Name, Email, Password, Date of birth
    title_mr = driver.find_element(By.ID, 'id_gender1')
    title_mr.click()
    password_input = driver.find_element(By.NAME, 'password')
    dob_day = driver.find_element(By.NAME, 'days')
    dob_month = driver.find_element(By.NAME, 'months')
    dob_year = driver.find_element(By.NAME, 'years')
    password_input.send_keys("testpassword")
    dob_day.send_keys("1")
    dob_month.send_keys("January")
    dob_year.send_keys("2000")

    # Select checkboxes
    newsletter_checkbox = driver.find_element(By.NAME, 'newsletter')
    offers_checkbox = driver.find_element(By.NAME, 'optin')
    newsletter_checkbox.click()
    offers_checkbox.click()

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    first_name = driver.find_element(By.NAME, 'first_name')
    last_name = driver.find_element(By.NAME, 'last_name')
    company = driver.find_element(By.NAME, 'company')
    address1 = driver.find_element(By.NAME, 'address1')
    address2 = driver.find_element(By.NAME, 'address2')
    country = driver.find_element(By.NAME, 'country')
    state = driver.find_element(By.NAME, 'state')
    city = driver.find_element(By.NAME, 'city')
    zipcode = driver.find_element(By.NAME, 'zipcode')
    mobile_number = driver.find_element(By.NAME, 'mobile_number')
    first_name.send_keys("Test")
    last_name.send_keys("User")
    company.send_keys("TestCompany")
    address1.send_keys("123 Test St")
    address2.send_keys("Suite 1")
    country.send_keys("United States")
    state.send_keys("New York")
    city.send_keys("New York")
    zipcode.send_keys("10001")
    mobile_number.send_keys("1234567890")

    # Click 'Create Account' button
    create_account_button = driver.find_element(By.XPATH, '//button[text()="Create Account"]')
    create_account_button.click()

    # Click 'Continue' button
    continue_button = driver.find_element(By.XPATH, '//a[text()="Continue"]')
    continue_button.click()


    # Click 'Delete Account' button
    # delete_account_button = driver.find_element(By.LINK_TEXT, 'Delete Account')
    # delete_account_button.click()

    # Click 'Continue' button on confirmation page
    # continue_button_confirm = driver.find_element(By.XPATH, '//a[text()="Continue"]')
    # time.sleep(7)
    # continue_button_confirm.click()


finally:
    # Close the browser
    driver.quit()

