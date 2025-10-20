from utils.logger import get_logger
from seleniumpagefactory.Pagefactory import PageFactory
from config.config import BASE_URL
from pages.demoqa.pagefactory.elements_page_factory import ElementsPageFactory

logger = get_logger(__name__)

class LandingPageFactory(PageFactory):

    locators = {
        "elements_option" : ('XPATH', "//h5[text()='Elements']"),
        "forms_option" : ('XPATH', "//h5[text()='Forms']"),
        "alerts_frames_windows_option" : ('XPATH', "//h5[text()='Alerts, Frame & Windows']")    
    }
    
    def __init__(self, driver, environment):        
        self.driver = driver    	# Required
        self.timeout = 15      		#(Optional - Customise your explicit wait for every webElement,Default 10sec)
        self.highlight = True   	#(Optional - To highlight every webElement in PageClass)
        self.mobile_test = False
        self.url = BASE_URL[environment]
        self.driver.get(self.url)
        logger.info("Navigating to the page: " + self.url)

    # elements option
    def click_elements_option(self):        
        self.elements_option.click()
        return ElementsPageFactory(self.driver)
    
    def get_elements_option(self):
        return self.elements_option
    
    # forms option
    # def click_forms_option(self):        
    #     self.click_element(self.forms_option)
    
    # def get_forms_option(self):
    #     return self.find_element(self.forms_option)
        
    # Alerts, Frame & Windows option
    # def click_alerts_frames_windows_option(self):        
    #     self.click_element(self.alerts_frames_windows_option)
    
    # def get_alerts_frames_windows_option(self):
    #     return self.find_element(self.alerts_frames_windows_option)
        