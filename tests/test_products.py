from pages.home_page import HomePage
from pages.products_page import ProductsPage
import re
from playwright.sync_api import expect
from data.test_data import Data


def test_verify_all_products_and_product_detail_page(get_webdriver_chrome):
    """
    Test to verify product page and products list details download and seen properly

    :param get_webdriver_chrome:
    :return: None
    """
    page = get_webdriver_chrome
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.click_products_btn()
    products_page.verify_products_heading()
    products_page.verify_products_list()
    products_page.click_first_product_view_btn()
    expect(page).to_have_url(re.compile(Data.first_product_url))
    products_page.verify_first_product_name()
    products_page.verify_first_product_category()
    products_page.verify_first_product_price()
    products_page.verify_first_product_availability()
    products_page.verify_first_product_condition()
    products_page.verify_first_product_brand()


def test_search_product(get_webdriver_chrome):
    """
    Test to verify products search works properly

    :param get_webdriver_chrome:
    :return: products list
    """
    page = get_webdriver_chrome
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    home_page.click_products_btn()
    products_page.verify_products_heading()
    products_page.fill_search_bar()
    products_page.click_search_btn()
    products_page.verify_search_products_heading()
    products_page.verify_search_products_list()