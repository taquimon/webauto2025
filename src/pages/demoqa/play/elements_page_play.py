from playwright.sync_api import Page, Locator
from pages.demoqa.play.base_page_play import BasePagePlay

class ElementsPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.text_box : Locator = page.get_by_role("list").get_by_text("Text Box")
        self.username : Locator = page.get_by_role("textbox", name="Full Name")
        self.submit_button: Locator = page.get_by_role("button", name="Submit")

    def navigate(self):
        self.navigate_url(url="http://demoqa.com/elements")

    def click_on_text_box(self):
        self.click_element(self.text_box)
        
    def enter_username(self, username):
        self.enter_text(self.username, username)
    
    def click_submit_button(self):
        self.click_element(self.submit_button)