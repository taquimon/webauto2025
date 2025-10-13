import re
import time

from playwright.sync_api import Page, expect
from pages.demoqa.play.landing_page_play import LandingPagePlay

class TestLandingPagePlay:

    def test_landing_page(self, page: Page) -> None:
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        
        # assertions playwright
        expect(landing_page.elements).to_be_visible()
        expect(landing_page.elements).to_contain_text("Elements")        
        expect(landing_page.forms).to_contain_text("Forms")
        expect(landing_page.alerts_frames_windows).to_contain_text("Alerts, Frame & Windows")
        expect(landing_page.widgets).to_contain_text("Widgets")
        expect(landing_page.interactions).to_contain_text("Interactions")
        expect(landing_page.book_store).to_contain_text("Book Store Application")
        
        
    
    
    