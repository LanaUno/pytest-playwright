from pages.home_page import HomePage
from playwright.sync_api import Page, Dialog
from pages.contactus_page import ContactUsPage

def test_contact_us_form(page: Page):
    home_page = HomePage(page)
    contactus_page = ContactUsPage(page)

    home_page.navigate()

    def accept_alert(alert: Dialog):
        alert.accept()

    page.on('dialog',accept_alert)
    home_page.click_contact_us_link()
    contactus_page.verify_get_in_touch_heading()
    contactus_page.fill_contactus_name()
    contactus_page.fill_contactus_email()
    contactus_page.fill_contactus_subject()
    contactus_page.fill_contactus_message()
    contactus_page.upload_files()
    contactus_page.click_contactus_submit_btn()
    contactus_page.verify_success_text()
    contactus_page.click_success_btn()
    home_page.check_home_link_visible()
