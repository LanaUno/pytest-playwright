from pages.home_page import HomePage


def test_verify_subscription_in_home_page(get_webdriver_chrome):
    """
    Test to verify a user can subscribe in the home page

    :param get_webdriver_chrome:
    :return: None
    """
    page = get_webdriver_chrome
    home_page = HomePage(page)

    home_page.scroll_down_to_footer()
    home_page.fill_subscribe_email()
    home_page.click_subscribe_btn()
    home_page.verify_subscribe_success_msg()