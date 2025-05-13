from playwright.sync_api import expect, Page
from utils.tools import take_screenshot
import allure

class AccountPage:

    def __init__(self, page: Page):
        self.page = page
        self.__account_username = self.page.locator(".fa").and_(page.locator(".fa-user"))
        self.__delete_account_link = self.page.get_by_role("link", name=" Delete Account")
        self.__account_deleted_msg = self.page.get_by_text("Account Deleted!")
        self.__logout_link = self.page.locator('a[href="/logout"]')

    def verify_account_name(self):
        with allure.step("Verify account name is visible"):
            expect(self.__account_username).to_be_visible()
        take_screenshot(self.page, "username_visible")

    def click_delete_account_link(self):
        with allure.step("Click Delete Account link"):
            self.__delete_account_link.click()

    def verify_account_deleted(self):
        with allure.step("Verify account deleted message is visible"):
            expect(self.__account_deleted_msg).to_be_visible()
        take_screenshot(self.page, "account_deleted")

    def click_logout_link(self):
        with allure.step("Click Logout link"):
            self.__logout_link.click()
