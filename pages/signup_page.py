from playwright.sync_api import expect, Page
from data.test_data import Data
import os
import dotenv
dotenv.load_dotenv()


class SignUpPage:

    def __init__(self, page: Page):
        self.page = page
        self.__enter_account_text = self.page.get_by_text("Enter Account Information")
        self.__radio_gender = self.page.get_by_role("radio", name="Mrs.")
        self.__your_password = self.page.get_by_role("textbox", name="Password *")
        self.__day_of_birth = self.page.locator("#days")
        self.__month_of_birth = self.page.locator("#months")
        self.__year_of_birth = self.page.locator("#years")
        self.__signup_for_newsletter = self.page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.__receive_offers = self.page.get_by_role("checkbox", name="Receive special offers from")
        self.__first_name = self.page.get_by_role("textbox", name="First name *")
        self.__last_name = self.page.get_by_role("textbox", name="Last name *")
        self.__company_name = self.page.get_by_role("textbox", name="Company", exact=True)
        self.__your_address1 = self.page.get_by_role("textbox", name="Address * (Street address, P.")
        self.__your_address2 = self.page.get_by_role("textbox", name="Address 2")
        self.__your_country = self.page.get_by_label("Country *")
        self.__your_state = self.page.get_by_role("textbox", name="State *")
        self.__your_city = self.page.get_by_role("textbox", name="City * Zipcode *")
        self.__your_zipcode = self.page.locator("#zipcode")
        self.__your_mobile = self.page.get_by_role("textbox", name="Mobile Number *")
        self.__create_account_btn = self.page.get_by_role("button", name="Create Account")
        self.__continue_btn = self.page.get_by_role("link", name="Continue")

    def verify_heading_text_is(self):
        expect(self.__enter_account_text).to_be_visible()

    def click_continue_btn(self):
        self.__continue_btn.click()

    def user_signup(self):
            self.__radio_gender.check()
            self.__your_password.fill(Data.password)
            self.__day_of_birth.select_option('1')
            self.__month_of_birth.select_option(Data.month)
            self.__year_of_birth.select_option('2021')
            self.__signup_for_newsletter.check()
            self.__receive_offers.check()
            self.__first_name.fill(Data.f_name)
            self.__last_name.fill(Data.l_name)
            self.__company_name.fill(Data.company)
            self.__your_address1.fill(Data.address1)
            self.__your_address2.fill(Data.address2)
            self.__your_country.select_option(Data.country)
            self.__your_state.fill(Data.state)
            self.__your_city.fill(Data.city)
            self.__your_zipcode.fill(Data.zipcode)
            self.__your_mobile.fill(Data.mobile)
            self.__create_account_btn.click()

    def real_user_signup(self):
            self.__radio_gender.check()
            self.__your_password.fill(os.getenv("MY_PASS"))
            self.__day_of_birth.select_option('28')
            self.__month_of_birth.select_option(Data.month)
            self.__year_of_birth.select_option('1900')
            self.__signup_for_newsletter.check()
            self.__receive_offers.check()
            self.__first_name.fill(Data.f_name)
            self.__last_name.fill(Data.l_name)
            self.__company_name.fill(Data.company)
            self.__your_address1.fill(Data.address1)
            self.__your_address2.fill(Data.address2)
            self.__your_country.select_option(Data.country)
            self.__your_state.fill(Data.state)
            self.__your_city.fill(Data.city)
            self.__your_zipcode.fill(Data.zipcode)
            self.__your_mobile.fill(Data.mobile)
            self.__create_account_btn.click()




        
    
