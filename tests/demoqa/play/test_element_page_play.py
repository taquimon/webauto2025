import re
import time

from playwright.sync_api import Page, expect
from pages.demoqa.play.elemenst_page_play import ElementsPagePlay
from pages.demoqa.play.landing_page_play import LandingPagePlay

class TestElementsPagePlay:

    def test_elements_text_box_page(self, page: Page) -> None:
        landing_page = LandingPagePlay(page)
        landing_page.navigate()        
        elements_page = landing_page.click_on_elements()
        elements_page.click_on_text_box()
        elements_page.enter_username("Edwin Taquichiri")
        elements_page.click_submit_button()
        time.sleep(2)
        

    def test_example_checkbox(self, page: Page) -> None:
        page.goto("https://demoqa.com/")
        page.get_by_role("heading", name="Elements").click()
        page.get_by_text("Check Box").click()
        page.locator("#tree-node").get_by_role("img").nth(3).click()
        page.get_by_role("button", name="Toggle").click()
        time.sleep(2)
    
    