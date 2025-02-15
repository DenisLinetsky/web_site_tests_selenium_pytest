import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    # Path to the ChromeDriver executable in the Docker container
    chrome_driver_path = "/usr/bin/chromedriver"

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Use Service to specify the ChromeDriver path
    service = Service(chrome_driver_path)

    # Initialize the WebDriver with the service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    driver.quit()



