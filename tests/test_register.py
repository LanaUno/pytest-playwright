from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from pages.account_page import AccountPage


def test_register_user(get_webdriver_chrome):
    """
    Test to verify a new user can register an account

    :param get_webdriver_chrome:
    :return:
    """
    page = get_webdriver_chrome
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignUpPage(page)
    account_page = AccountPage(page)

    home_page.click_signup_login_btn()
    login_page.verify_new_user_signup_text()
    login_page.sign_up()
    signup_page.verify_heading_text_is()
    """
    register new user account
    """
    signup_page.user_signup()
    signup_page.click_continue_btn()
    account_page.verify_account_name()
    """
    delete new user account
    """
    account_page.click_delete_account_link()
    account_page.verify_account_deleted()


def test_register_user_with_existing_email(signup_and_logout_real_user):
    """
    Test to verify a user can't register account with existing email

    :param signup_and_logout_real_user:
    :return: None
    """
    page = signup_and_logout_real_user
    login_page = LoginPage(page)
    account_page = AccountPage(page)
    """
    register account with existing email
    """
    login_page.signup_real_user_init()
    login_page.verify_existing_email_error_message()
    """
    login and delete account
    """
    login_page.login()
    account_page.click_delete_account_link()
