from playwright.sync_api import Page
from utils.logger import get_logger
logger = get_logger(__name__)

class BasePagePlay(Page):
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_url(self, url):
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)
    
    def click_element(self, locator):
        """Click on element"""                                
        tag_name, element_name = self.get_tag_and_text(locator)
        logger.info(f"Clicking on {element_name} element: {tag_name}")
        locator.click()
    
    def enter_text(self, locator, text):
        """Enter text into input field"""      
        tag_name, element_name = self.get_tag_and_text(locator)  
        logger.info(f"Entering text '{text}' into {element_name} element: {tag_name}")
        locator.fill(text)
    
    def get_tag_and_text(self, locator):
        """Get tag name and text from locator"""
        # get the tag from locator: button, span, div, a, etc.
        tag_name = locator.evaluate("node => node.tagName")
        # get the text from locator | text_content | inner_text
        if locator.inner_text():
            element_name = locator.inner_text()
        else:
            element_name = tag_name
        return tag_name, element_name