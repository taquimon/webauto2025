import allure
import pytest
import time    
from pages.demoqa.pagefactory.landing_page_factory import LandingPageFactory
from pages.demoqa.pagefactory.elements_page_factory import ElementsPageFactory
from utils.logger import get_logger


logger = get_logger(__name__)
class TestDemoQAElementsPageFactory:
    
    def test_elements_page_factory(self, driver, env):
        """
        Test that the elements page factory is displayed with all options
        """        
        
        # create the page object
        landing_page = LandingPageFactory(driver, env)
        
        # click on the elements option
        elements_page = landing_page.click_elements_option()
        
        elements_page.click_text_box_item()

        elements_page.enter_user_name("Edwin Taquichiri")
                                
        time.sleep(5)
        # elements_page.click_submit_button()
                
        # assert that the text box page is displayed
        # assert "Edwin Taquichiri" in elements_text_box_page.get_user_name().text, "User name paragraph is not displayed"    