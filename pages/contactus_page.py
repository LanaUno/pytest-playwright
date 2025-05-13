from playwright.sync_api import expect, Page
from data.test_data import Data
from utils.tools import take_screenshot
import allure

class ContactUsPage:

    def __init__(self, page: Page):
        self.page = page
        self.__get_in_touch_heading = self.page.get_by_role("heading", name="Get In Touch")
        self.__contactus_name = self.page.get_by_role("textbox", name="Name")
        self.__contactus_email = self.page.get_by_role("textbox", name="Email", exact=True)
        self.__contactus_subject = self.page.get_by_role("textbox", name="Subject")
        self.__contactus_message = self.page.get_by_role("textbox", name="Your Message Here")
        self.__contactus_submit_btn = self.page.get_by_role("button", name="Submit")
        self.__success_text = self.page.locator("#contact-page").get_by_text("Success! Your details have")
        self.__success_btn = self.page.locator('div~div > a[href = "/"]')



    def verify_get_in_touch_heading(self):
        with allure.step("Verify Get In Touch heading is visible"):
            expect(self.__get_in_touch_heading).to_be_visible()
        take_screenshot(self.page, "get_in_touch_heading")

    def fill_contactus_name(self):
        with allure.step("Fill name"):
            self.__contactus_name.fill(Data.name)

    def fill_contactus_email(self):
        with allure.step("Fill email"):
            self.__contactus_email.fill(Data.email)

    def fill_contactus_subject(self):
        with allure.step("Fill subject"):
            self.__contactus_subject.fill(Data.subj)

    def fill_contactus_message(self):
        with allure.step("Fill message"):
            self.__contactus_message.fill(Data.message)

    def upload_files(self):
        with allure.step("Upload file"):
            with self.page.expect_file_chooser() as fc_info:
                self.page.locator('input[name="upload_file"]').click()
                file_chooser = fc_info.value
                file_chooser.set_files("./data/img.jpg")
                take_screenshot(self.page, "upload_file")


    def click_contactus_submit_btn(self):
        with allure.step("Click Submit button"):
            self.__contactus_submit_btn.click()

    def verify_success_text(self):
        with allure.step("Verify Success text is visible"):
            expect(self.__success_text).to_be_visible()
        take_screenshot(self.page, "success_text")

    def click_success_btn(self):
        with allure.step("Click Success button"):
            self.__success_btn.click()