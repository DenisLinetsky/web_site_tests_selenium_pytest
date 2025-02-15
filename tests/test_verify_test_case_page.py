import pytest
from main.verify_test_case_page.home_page import HomePage
from main.verify_test_case_page.test_cases_page import TestCasesPage


@pytest.mark.special
def test_verify_test_case_page(driver):
    home_page = HomePage(driver)
    test_cases_page = TestCasesPage(driver)

    home_page.open_home_page()
    home_page.verify_home_page()
    home_page.click_test_cases()
    test_cases_page.verify_test_cases_page()




