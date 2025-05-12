from playwright.sync_api import expect, Page
from utils.tools import take_screenshot


class TesTCasesPage:
    def __init__(self, page: Page):
        self.page = page
        self.__testcases_heading = self.page.locator("b")

    def verify_test_cases_heading(self):
        expect(self.__testcases_heading).to_be_visible()
        take_screenshot(self.page, "testcase_heading")

