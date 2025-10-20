from screenpy import Actor
from screenpy_selenium.actions import Click
from screenpy_selenium.target import Target
from selenium.webdriver.common.by import By

from utils.logger import get_logger
logger = get_logger(__name__)

class ElementsPageScreenPlay:
    def __init__(self, actor):
        self.actor = actor
        self.text_box_menu_item = Target.the("text box menu item").located_by((By.ID, "item-0"))
        self.text_box_title = Target.the("text box title").located_by((By.CSS_SELECTOR, "h1[class='text-center']"))
        
    
    def click_text_box_menu_item(self):
        self.actor.attempts_to(Click.on_the(self.text_box_menu_item))
        logger.info("Clicking on the text box menu item")
        # return ElemenstTextBoxScreenPlay(self.actor)
        
    def get_text_box_title(self):
        logger.info("Getting the text box title")
        return self.text_box_title
        