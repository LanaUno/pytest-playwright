from playwright.sync_api import expect, Page
from data.test_data import Data

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
        expect(self.__get_in_touch_heading).to_be_visible()

    def fill_contactus_name(self):
        self.__contactus_name.fill(Data.name)

    def fill_contactus_email(self):
        self.__contactus_email.fill(Data.email)

    def fill_contactus_subject(self):
        self.__contactus_subject.fill(Data.subj)

    def fill_contactus_message(self):
        self.__contactus_message.fill(Data.message)

    def upload_files(self):
        self.page.locator('input[name="upload_file"]').set_input_files('data\\img.jpg')

    def click_contactus_submit_btn(self):
        self.__contactus_submit_btn.click()

    def verify_success_text(self):
        expect(self.__success_text).to_be_visible()

    def click_success_btn(self):
        self.__success_btn.click()