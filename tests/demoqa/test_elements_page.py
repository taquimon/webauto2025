import allure
import pytest
from pages.demoqa.selenium.landing_page import LandingPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestDemoQAElementsPage:

    @allure.title("Test Smoke for Landing page")
    @allure.description("This test verifies landing page for demoqa.")
    @allure.tag("Landing", "Smoke", "Functional")
    @pytest.mark.functional
    @pytest.mark.smoke
    def test_elements_text_box_page(self, driver, env):
        """
        Test that the elements text box page is displayed with all options
        """        
        
        # create the page object
        landing_page = LandingPage(driver, env)
        
        # click on the elements option
        elements_page = landing_page.click_elements_option()
        
        elements_text_box_page = elements_page.click_text_box_menu_item()

        elements_text_box_page.enter_user_name("Edwin Taquichiri")
                                
        elements_text_box_page.click_submit_button()
                
        # assert that the text box page is displayed
        assert "Edwin Taquichiri" in elements_text_box_page.get_user_name().text, "User name paragraph is not displayed"

    @allure.title("Test Smoke for Elements page")
    @allure.description("This test verifies Elements page for demoqa.")
    @allure.tag("Elements", "Functional")
    @pytest.mark.functional
    def test_elements_check_box_page(self, driver, env):
        """
        Test that the elements check box page is displayed with all options
        """        
        
        # create the page object
        landing_page = LandingPage(driver, env)
        
        # click on the elements option
        elements_page = landing_page.click_elements_option()
        
        elements_page.click_check_box_menu_item()        
        
        # assert that the check box page is displayed
        assert "Check Box" in elements_page.get_check_box_title().text, "Check Box title is not displayed"    
        