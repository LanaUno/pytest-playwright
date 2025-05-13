from playwright.sync_api import expect, Page
from data.test_data import Data
import os
import dotenv
dotenv.load_dotenv()
from utils.tools import take_screenshot
import allure

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.__home_link = self.page.get_by_role("link", name=" Home")
        self.__signup_login_btn = self.page.get_by_role("listitem").filter(has_text="Signup / Login")
        self.__contact_us_btn = self.page.get_by_role("link", name=" Contact us")
        self.__test_cases_btn = self.page.get_by_role("link", name=" Test Cases")
        self.__products_btn = self.page.get_by_role("link", name=" Products")
        self.__footer = self.page.locator('#footer')
        self.__subscribe_email = self.page.locator('#susbscribe_email')
        self.__subscribe_btn = self.page.locator('#subscribe')
        self.__subscribe_success_msg = self.page.locator('//div[@class="alert-success alert"]')

    def navigate(self):
        with allure.step('Website is opened'):
            self.page.goto(os.getenv("BASE_URL"))

    def check_home_link_visible(self):
        with allure.step('Home page is visible'):
            expect(self.__home_link).to_be_visible()
        take_screenshot(self.page, "home_link_visible")

    def click_signup_login_btn(self):
        with allure.step('Click Signup/Login button'):
            self.__signup_login_btn.click()

    def click_contact_us_link(self):
        with allure.step('Click Contact us link'):
            self.__contact_us_btn.click()

    def click_test_cases_btn(self):
        with allure.step('Click Test Cases button'):
            self.__test_cases_btn.click()

    def click_products_btn(self):
        with allure.step('Click Products button'):
            self.__products_btn.click()

    def scroll_down_to_footer(self):
        with allure.step('Scroll down to footer'):
            self.__footer.click()

    def fill_subscribe_email(self):
        with allure.step('Fill Subscribe textbox with email'):
            self.__subscribe_email.fill(Data.email)

    def click_subscribe_btn(self):
        with allure.step('Click Subscribe button'):
            self.__subscribe_btn.click()

    def verify_subscribe_success_msg(self):
        with allure.step('Verify Subscribe success message is visible'):
            expect(self.__subscribe_success_msg).to_be_visible()
        take_screenshot(self.page, "subscribe_success")