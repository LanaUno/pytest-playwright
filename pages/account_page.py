from playwright.sync_api import expect, Page
from utils.tools import take_screenshot

class AccountPage:

    def __init__(self, page: Page):
        self.page = page
        self.__account_username = self.page.locator(".fa").and_(page.locator(".fa-user"))
        self.__delete_account_link = self.page.get_by_role("link", name=" Delete Account")
        self.__account_deleted_msg = self.page.get_by_text("Account Deleted!")
        self.__logout_link = self.page.locator('a[href="/logout"]')

    def verify_account_name(self):
        expect(self.__account_username).to_be_visible()
        take_screenshot(self.page, "username_visible")

    def click_delete_account_link(self):
        self.__delete_account_link.click()

    def verify_account_deleted(self):
        expect(self.__account_deleted_msg).to_be_visible()

    def click_logout_link(self):
        self.__logout_link.click()
