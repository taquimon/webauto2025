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
    
    def test_demoqa_landing_page(self):
        """
        Test that the demoqa landing page is displayed with all options
        """                
        
        # create the page object
        landing_page = LandingPage(self.driver)
        
        # verify the elements displayed
        logger.info("Verifying the elements displayed")
        logger.info("Elements option: " + landing_page.get_elements_option().text)
        logger.info("Forms option: " + landing_page.get_forms_option().text)
        logger.info("Alerts, Frame & Windows option: " + landing_page.get_alerts_frames_windows_option().text)
        assert landing_page.get_elements_option().text == "Elements", "Elements option is not displayed"
        assert landing_page.get_forms_option().text == "Forms", "Forms option is not displayed"
        assert landing_page.get_alerts_frames_windows_option().text == "Alerts, Frame & Windows", "Alerts, Frame & Windows option is not displayed"
                
        
    
    @classmethod
    def teardown_class(self):
        # Close the browser
        logger.info("Closing the browser")
        self.driver.quit()