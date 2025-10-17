from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.demoqa.selenium.base_page import BasePage
from pages.demoqa.selenium.elements_page import ElementsPage
from pages.demoqa.selenium.elements_page import ElementsLinksPage
from config.config import BASE_URL

logger = get_logger(__name__)

class LandingPage(BasePage):

    elements_option = (By.XPATH, "//h5[text()='Elements']")
    forms_option = (By.XPATH, "//h5[text()='Forms']")    
    alerts_frames_windows_option = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")    
    
    def __init__(self, driver, environment):
        super().__init__(driver)        
        self.url = BASE_URL[environment]
        self.driver.get(self.url)
        logger.info("Navigating to the page: " + self.url)

    # elements option
    def click_elements_option(self):        
        self.click_element(self.elements_option)
        return ElementsPage(self.driver)
    
    def get_elements_option(self):
        return self.find_element(self.elements_option)
    
    # forms option
    def click_forms_option(self):        
        self.click_element(self.forms_option)
    
    def get_forms_option(self):
        return self.find_element(self.forms_option)
        
    # Alerts, Frame & Windows option
    def click_alerts_frames_windows_option(self):        
        self.click_element(self.alerts_frames_windows_option)
    
    def get_alerts_frames_windows_option(self):
        return self.find_element(self.alerts_frames_windows_option)
        