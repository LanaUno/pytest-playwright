from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
import pytest


def test_login_user_with_correct_email_and_password(signup_and_logout_real_user):
    """
    Test to verify a user can log in with correct credentials

    :param signup_and_logout_real_user:
    :return: None
    """
    page = signup_and_logout_real_user
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    login_page.login()
    account_page.verify_account_name()
    account_page.click_delete_account_link()
    account_page.verify_account_deleted()


@pytest.mark.parametrize('creds',
    [
        ('auto@auto.com', '123test'),
        ('auto@admin.com', 'auto123test')
        ]
    )
def test_login_user_with_incorrect_email_and_password(get_webdriver_chrome, creds):
    """
    Test to verify a user can't log in with incorrect credentials

    :param get_webdriver_chrome:
    :return: None
    """
    page = get_webdriver_chrome
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.click_signup_login_btn()
    login_page.verify_user_login_text()
    login_page.login_with_incorrect_cred(creds)
    login_page.verify_incorrect_cred_error_message()
