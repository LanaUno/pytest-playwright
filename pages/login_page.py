from playwright.sync_api import expect, Page
from data.test_data import Data
import os
import dotenv
dotenv.load_dotenv()
import allure
from utils.tools import take_screenshot


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.__new_user_sighup_text = self.page.get_by_role("heading", name="New User Signup!")
        self.__user_name = self.page.get_by_role("textbox", name="Name")
        self.__user_email = self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.__signup_btn = self.page.get_by_role("button", name="Signup")
        self.__user_login_text = self.page.get_by_role("heading", name="Login to your account")
        self.__login_user_email = self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.__login_user_password = self.page.get_by_role("textbox", name="Password")
        self.__login_btn = self.page.get_by_role("button", name="Login")
        self.__incorrect_cred_error_message = self.page.get_by_text("Your email or password is")
        self.__existing_email_error_message = self.page.locator('p[style="color: red;"]')

    def verify_new_user_signup_text(self):
        with allure.step('Verify "New User Signup!" text is visible'):
            expect(self.__new_user_sighup_text).to_be_visible()
        take_screenshot(self.page, "new_user_signup_text")

    @allure.step("Initial Signup random user with name=Data.f_name, email=Data.email,"
                 "click Signup button" )
    def sign_up(self):
        self.__user_name.fill(Data.f_name)
        self.__user_email.fill(Data.email)
        self.__signup_btn.click()

    @allure.step("Initial Signup real user with name=Data.f_name, email=MY_EMAIL,"
                 "click Signup button")
    def signup_real_user_init(self):
        self.__user_name.fill(Data.f_name)
        self.__user_email.fill(os.getenv("MY_EMAIL"))
        self.__signup_btn.click()

    def verify_user_login_text(self):
        with allure.step('Verify "Login to your account" text is visible'):
            expect(self.__user_login_text).to_be_visible()
        take_screenshot(self.page, "user_login_text")

    @allure.step("Login real user with email=MY_EMAIL, password=MY_PASS,"
                 "click Login button")
    def login(self):
        self.__login_user_email.fill(os.getenv("MY_EMAIL"))
        self.__login_user_password.fill(os.getenv("MY_PASS"))
        self.__login_btn.click()

    @allure.step("Login user with incorrect credentials:"
                 "email=email, password=pass,"
                 "click Login button")
    def login_with_incorrect_cred(self, creds):
        email, passw = creds
        self.__login_user_email.fill(email)
        self.__login_user_password.fill(passw)
        self.__login_btn.click()

    def verify_incorrect_cred_error_message(self):
        with allure.step('Verify incorrect credentials error message is visible'):
            expect(self.__incorrect_cred_error_message).to_be_visible()
        take_screenshot(self.page, "incorrect_cred_error_message")

    def verify_existing_email_error_message(self):
        with allure.step('Verify existing email error message is visible'):
            expect(self.__existing_email_error_message).to_be_visible()
        take_screenshot(self.page, "existing_email_error_message")
