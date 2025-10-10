import re
import time

from playwright.sync_api import Page, expect
from pages.demoqa.play.elemenst_page_play import ElementsPagePlay
from pages.demoqa.play.forms_page_play import FormsPagePlay

class TestFormsPagePlay:

    def test_forms(self, page: Page) -> None:
        forms_page = FormsPagePlay(page)
        forms_page.navigate()        
        forms_page.click_on_practice_form_menu()
        forms_page.enter_first_name("Edwin")        
        forms_page.enter_last_name("Taquichiri")        
        forms_page.enter_email("taquimon@gmail.com")
        forms_page.click_on_gender()        
        forms_page.enter_mobile_number("5917807290")
        forms_page.click_on_hobbies()
        forms_page.click_on_hobbies_2()
        forms_page.click_on_hobbies_3()
        # forms_page.click_on_state()
        # forms_page.click_on_city()
        forms_page.click_on_submit_button()
        

        # page.goto("https://demoqa.com/")
        # page.get_by_role("heading", name="Forms").click()
        # page.get_by_text("Practice Form").click()
        # page.get_by_role("textbox", name="First Name").click()
        # page.get_by_role("textbox", name="First Name").fill("Edwin")
        # page.get_by_role("textbox", name="First Name").press("Tab")
        # page.get_by_role("textbox", name="Last Name").fill("Taquichiri")
        # page.get_by_role("textbox", name="name@example.com").click()
        # page.get_by_role("textbox", name="name@example.com").fill("taquimon@gmail.com")
        # page.get_by_text("Male", exact=True).click()
        # page.get_by_role("textbox", name="Mobile Number").click()
        # page.get_by_role("textbox", name="Mobile Number").fill("5917807290")
        # page.get_by_role("textbox", name="Mobile Number").press("ArrowLeft")
        # page.get_by_role("textbox", name="Mobile Number").press("ArrowLeft")
        # page.get_by_text("Sports").click()
        # page.get_by_text("Reading").click()
        # page.get_by_text("Music").click()
        # page.locator("#state svg").click()
        # page.get_by_text("NCR", exact=True).click()
        # page.locator("#city svg").click()
        # page.get_by_text("Delhi", exact=True).click()
        # page.get_by_role("button", name="Submit").click()
        #page.get_by_role("dialog", name="Thanks for submitting the form").click()
        #page.locator("div").filter(has_text="LabelValuesStudent NameEdwin").nth(3).click()
       # page.get_by_role("dialog", name="Thanks for submitting the form").click()