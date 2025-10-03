from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.demoqa.landing_page import LandingPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestDemoQALandingPage:
    
    @classmethod
    def setup_class(self):
        # start the session
        self.driver = webdriver.Chrome()
        logger.info("Starting the session")
        self.driver.implicitly_wait(10)
    
    def test_elements_text_box_page(self):
        """
        Test that the elements text box page is displayed with all options
        """        
        
        # create the page object
        landing_page = LandingPage(self.driver)
        
        # click on the elements option
        elements_page = landing_page.click_elements_option()
        
        elements_page.click_text_box_menu_item()
        elements_page.enter_user_name("Edwin Taquichiri")
        
        # TODO: scroll or make visible button
        elements_page.click_submit_button()
                
                # assert that the text box page is displayed
        assert "Edwin Taquichiri" in elements_page.get_user_name().text, "User name paragraph is not displayed"        
    
    def test_elements_check_box_page(self):
        """
        Test that the elements check box page is displayed with all options
        """        
        
        # create the page object
        landing_page = LandingPage(self.driver)
        
        # click on the elements option
        elements_page = landing_page.click_elements_option()
        
        elements_page.click_check_box_menu_item()
        
        # assert that the check box page is displayed
        assert "Check Box" in elements_page.get_check_box_title().text, "Check Box title is not displayed"
    
    @classmethod
    def teardown_class(self):
        # Close the browser
        logger.info("Closing the browser")
        self.driver.quit()
        