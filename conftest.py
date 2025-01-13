import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    chrome_driver_path = r"C:/Users/denis/Downloads/chromedriver-win64/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")

    service = ChromeService(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
