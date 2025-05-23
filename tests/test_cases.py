from pages.testcases_page import TesTCasesPage
from pages.home_page import HomePage


def test_verify_test_cases_page(get_webdriver_chrome):
    """
    Test to verify Test Cases heading is visible

    :param get_webdriver_chrome:
    :return: None
    """

    page = get_webdriver_chrome
    home_page = HomePage(page)
    testcases_page = TesTCasesPage(page)

    home_page.click_test_cases_btn()
    testcases_page.verify_test_cases_heading()
