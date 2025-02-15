class TestCasesPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_test_cases_page(self):
        assert "Test Cases" in self.driver.title
