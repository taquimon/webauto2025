import time
from screenpy.actor import Actor
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy_selenium.actions import Open
from screenpy_selenium.questions import BrowserTitle
from screenpy.resolutions import Equals
from screenpy import See
from screenpy_selenium.target import Target
from screenpy_selenium.actions import Click
from selenium.webdriver.common.by import By
from screenpy_selenium.questions import Text
from pages.demoqa.screenplay.landing_page_screen_play import LandingPageScreenPlay

class TestDemoQALandingPageScreenPlay:
    def test_google_title(self):
        """
        Test that the demoqa landing page is displayed with all options
        """    
        # 1. Instantiate an Actor and give them the ability to browse the web
        #    (using Selenium WebDriver, which ScreenPy Selenium handles).
        actor = Actor.named("Edwin").who_can(BrowseTheWeb.using_chrome()) 
        # You can also use .using_firefox() or provide a specific WebDriver instance.

        # 2. The Actor performs an action: opening a URL.
        actor.attempts_to(
            Open.their_browser_on("https://demoqa.com/")
        )

        # 3. The Actor asks a question and asserts the answer.
        actor.should(See.the(BrowserTitle(), Equals("DEMOQA")))

        elements_link = Target.the("elements option").located_by("//h5[text()='Elements']")
        actor.attempts_to(Click.on_the(elements_link))

        text_box_menu_item = Target.the("text box menu item").located_by((By.ID, "item-0"))
        actor.attempts_to(Click.on_the(text_box_menu_item))
        
        textbox_title = Target.the("text box title").located_by((By.CSS_SELECTOR, "h1[class='text-center']"))
        actor.should(See.the(Text.of(textbox_title), Equals("Text Box")))

        time.sleep(5)
        # 4. Clean up: the Actor quits their browser.
        actor.exit()


    def test_elements_option(self, actor):
        """
        Test that the elements option is displayed
        """            
        # act
        landing_page = LandingPageScreenPlay(actor)
        landing_page.open_browser()
        elements_page = landing_page.click_elements_option()
        elements_page.click_text_box_menu_item()
        #assert
        actor.should(See.the(Text.of(elements_page.get_text_box_title()), Equals("Text Box")))
        time.sleep(5)        
    