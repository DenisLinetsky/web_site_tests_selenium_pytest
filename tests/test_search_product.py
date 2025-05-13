from selenium.webdriver.common.by import By

from main.search_product.home_page import HomePage
from main.search_product.products_page import ProductsPage


def test_search_product(driver):
    home_page = HomePage(driver)
    products_page = ProductsPage(driver)

    # Step 1: Launch browser & Navigate
    home_page.navigate_to_homepage()
    assert "Automation Exercise" in driver.title

    # Step 2: Click 'Products' button
    home_page.click_products()

    # Step 3: Verify navigation to 'ALL PRODUCTS' page
    products_page.open()
    assert driver.find_element(By.XPATH, "//h2[@class='title text-center']").is_displayed()

    # Step 4: Search for a product (e.g., "Dress")
    products_page.search_product("Dress")

    # Step 5: Verify 'SEARCHED PRODUCTS' text
    assert products_page.is_search_results_visible()

    # Step 6: Verify related products are displayed
    assert products_page.are_products_listed()
