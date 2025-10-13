from playwright.sync_api import Page, Locator
from pages.demoqa.play.base_page_play import BasePagePlay
from pages.demoqa.play.elements_page_play import ElementsPagePlay
from pages.demoqa.play.forms_page_play import FormsPagePlay

class LandingPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.elements : Locator = page.get_by_role("heading").get_by_text("Elements")
        self.forms : Locator = page.get_by_role("heading").get_by_text("Forms")
        self.alerts_frames_windows : Locator = page.get_by_role("heading").get_by_text("Alerts, Frame & Windows")
        self.widgets : Locator = page.get_by_role("heading").get_by_text("Widgets")
        self.interactions : Locator = page.get_by_role("heading").get_by_text("Interactions")
        self.book_store : Locator = page.get_by_role("heading").get_by_text("Book Store Application")
        
    
    def navigate(self):
        self.navigate_url(url="http://demoqa.com/")
    
    def click_on_elements(self):
        self.click_element(self.elements)
        return ElementsPagePlay(self.page)
    
    def click_on_forms(self):
        self.click_element(self.forms)
        return FormsPagePlay(self.page)
    
    def click_on_alerts_frames_windows(self):
        self.click_element(self.alerts_frames_windows)
    
    def click_on_widgets(self):
        self.click_element(self.widgets)
    
    def click_on_interactions(self):
        self.click_element(self.interactions)
    
    def click_on_book_store(self):
        self.click_element(self.book_store)