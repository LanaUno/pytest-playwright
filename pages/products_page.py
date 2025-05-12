from playwright.sync_api import expect, Page
from data.test_data import Data
import re
from utils.tools import take_screenshot


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.__products_heading = self.page.get_by_role("heading", name="All Products")
        self.__products_list = self.page.get_by_text("All Products  Added! Your")
        self.__first_product_view_btn = self.page.locator(".choose > .nav > li > a").first
        self.__first_product_name = self.page.locator('div[class="product-information"]>h2')
        self.__first_product_category = self.page.get_by_text("Category:")
        self.__first_product_price = self.page.get_by_text("Rs.")
        self.__first_product_availability = self.page.get_by_text("Availability:")
        self.__first_product_condition = self.page.get_by_text("Condition:")
        self.__first_product_brand = self.page.get_by_text("Brand:")
        self.__search_bar = self.page.locator("#search_product")
        self.__search_btn = self.page.locator('#submit_search')
        self.__search_products_heading = self.page.locator('.title').and_(page.locator('.text-center'))
        self.__search_products_list = self.page.locator('div[class="col-sm-4"]>div>div>div>div>h2~p')

    def verify_products_heading(self):
        expect(self.__products_heading ).to_be_visible()
        take_screenshot(self.page, "verify_products_heading")

    def verify_products_list(self):
        expect(self.__products_list).to_be_visible()
        take_screenshot(self.page, "products_list")

    def click_first_product_view_btn(self):
        self.__first_product_view_btn.click()

    def verify_first_product_name(self):
        expect(self.__first_product_name).to_be_visible()
        take_screenshot(self.page, "first_product_name")

    def verify_first_product_category(self):
        expect(self.__first_product_category).to_be_visible()

    def verify_first_product_price(self):
        expect(self.__first_product_price).to_be_visible()

    def verify_first_product_availability(self):
        expect(self.__first_product_availability).to_be_visible()

    def verify_first_product_condition(self):
        expect(self.__first_product_condition).to_be_visible()

    def verify_first_product_brand(self):
        expect(self.__first_product_brand).to_be_visible()

    def fill_search_bar(self):
        self.__search_bar.fill(Data.product_name)

    def click_search_btn(self):
        self.__search_btn.click()

    def verify_search_products_heading(self):
        expect(self.__search_products_heading).to_be_visible()
        take_screenshot(self.page, "search_products_heading")

    def verify_search_products_list(self):
        texts = self.__search_products_list.all_inner_texts()
        print(texts)
        found_words = [match.group().lower() for text in texts for match in
                       re.finditer(rf"\b{Data.product_name}\b", text, re.IGNORECASE)]
        print(found_words)
        for fw in found_words:
            if fw == Data.product_name:
                print(True)
            else:
                print(False)



