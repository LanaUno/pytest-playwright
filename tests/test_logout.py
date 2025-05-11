from pages.login_page import LoginPage
from pages.account_page import AccountPage


def test_logout_user(signup_and_logout_real_user):
    page = signup_and_logout_real_user
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    login_page.login()
    account_page.verify_account_name()
    account_page.click_logout_link()
    login_page.verify_user_login_text()
    login_page.login()
    account_page.click_delete_account_link()
