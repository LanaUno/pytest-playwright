import os
import dotenv
dotenv.load_dotenv()


from playwright.sync_api import Playwright, Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from pages.account_page import AccountPage
import pytest

@pytest.fixture()
def get_webdriver_chrome(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(os.getenv("BASE_URL"))
    home_page = HomePage(page)
    home_page.check_home_link_visible()
    yield page
    browser.close()


@pytest.fixture(scope= "function")
def signup_and_logout_real_user(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignUpPage(page)
    account_page = AccountPage(page)

    home_page.navigate()
    home_page.check_home_link_visible()
    home_page.click_signup_login_btn()
    login_page.verify_new_user_signup_text()
    login_page.signup_real_user_init()
    signup_page.real_user_signup()
    signup_page.click_continue_btn()
    account_page.verify_account_name()
    account_page.click_logout_link()
    yield page



