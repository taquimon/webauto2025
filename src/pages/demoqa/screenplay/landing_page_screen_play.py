from screenpy import Actor
from screenpy_selenium.actions import Click, Open
from screenpy_selenium.target import Target
from pages.demoqa.screenplay.elements_page_screen_play import ElementsPageScreenPlay
from utils.logger import get_logger

logger = get_logger(__name__)

class LandingPageScreenPlay:
    
    def __init__(self, actor):
        self.actor = actor
    
        self.elements_link = Target.the("elements option").located_by("//h5[text()='Elements']")
        self.url = "https://demoqa.com/"

    def open_browser(self):
        self.actor.attempts_to(Open.their_browser_on(self.url))        
        logger.info("Navigating to the page: %s", self.url)

    def click_elements_option(self):        
        self.actor.attempts_to(Click.on_the(self.elements_link))
        logger.info("Clicking on the elements option")
        return ElementsPageScreenPlay(self.actor)
    
    def get_elements_option(self):
        logger.info("Getting the elements option")
        return self.elements_link
        

    
    