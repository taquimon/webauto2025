from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.demoqa.landing_page import LandingPage

class TestDemoQALandingPage:
    
    @classmethod
    def setup_class(self):
        # start the session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def test_demoqa_show_elements_page(self):
        """
        Test that the demoqa landing page is displayed
        """
        
        # navigate to the page
        self.driver.get("http://demoqa.com")
        
        landing_page = LandingPage(self.driver)
        landing_page.click_elements_option()

        # text_box_option = self.driver.find_element(By.ID, "item-0")
        # text_box_option.click()

        # text_box_title = self.driver.find_element(By.CLASS_NAME, "text-center")
        
        # assert text_box_title.text == "Text Box"         
        time.sleep(5)
        
    
    @classmethod
    def teardown_class(self):
        # Close the browser
        self.driver.quit()