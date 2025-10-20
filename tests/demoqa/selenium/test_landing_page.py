from pages.demoqa.selenium.landing_page import LandingPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestDemoQALandingPage:
        
    
    def test_demoqa_landing_page(self, driver, env):
        """
        Test that the demoqa landing page is displayed with all options
        """                
        logger.info("Environment: %s", env)
        # create the page object
        landing_page = LandingPage(driver, env)
        
        # verify the elements displayed
        logger.info("Verifying the elements displayed")
        logger.info("Elements option: " + landing_page.get_elements_option().text)
        logger.info("Forms option: " + landing_page.get_forms_option().text)
        logger.info("Alerts, Frame & Windows option: " + landing_page.get_alerts_frames_windows_option().text)
        assert landing_page.get_elements_option().text == "Elements", "Elements option is not displayed"
        assert landing_page.get_forms_option().text == "Forms", "Forms option is not displayed"
        assert landing_page.get_alerts_frames_windows_option().text == "Alerts, Frame & Windows", "Alerts, Frame & Windows option is not displayed"
                            