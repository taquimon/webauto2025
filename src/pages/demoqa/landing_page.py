from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from pages.demoqa.base_page import BasePage

logger = get_logger(__name__)

class LandingPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)        
        self.elements_option = (By.XPATH, "//h5[text()='Elements']")
        self.forms_option = (By.XPATH, "//h5[text()='Forms']")

    def click_elements_option(self):        
        self.click_element(self.elements_option)
    
    def click_forms_option(self):        
        self.click_element(self.forms_option)