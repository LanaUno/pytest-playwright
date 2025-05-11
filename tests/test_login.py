from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


def test_login_user_with_correct_email_and_password(signup_and_logout_real_user):
    page = signup_and_logout_real_user
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    login_page.login()
    account_page.verify_account_name()
    account_page.click_delete_account_link()
    account_page.verify_account_deleted()


def test_login_user_with_incorrect_email_and_password(get_webdriver_chrome):
    page = get_webdriver_chrome
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.click_signup_login_btn()
    login_page.verify_user_login_text()
    login_page.login_with_incorrect_cred()
    login_page.verify_incorrect_cred_error_message()
