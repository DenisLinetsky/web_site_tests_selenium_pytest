from selenium.webdriver.common.by import By

from main.verify_all_products_and_product_detail_page.home_page import HomePage
from main.verify_all_products_and_product_detail_page.products_page import ProductsPage
from main.verify_all_products_and_product_detail_page.product_detail_page import ProductDetailPage


def test_product_navigation(driver):

    # Home Page
    home = HomePage(driver)
    home.open()
    assert "Automation Exercise" in driver.title
    home.navigate_to_products()

    # Products Page
    products = ProductsPage(driver)
    products.open()
    assert "ALL PRODUCTS" in driver.find_element(By.CSS_SELECTOR, "h2.title.text-center").text
    assert products.verify_products_list_visible()
    products.click_first_product()

    # Product Detail Page
    details = ProductDetailPage(driver)
    details.open()
    assert details.verify_product_details()


