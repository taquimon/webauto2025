from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.demoqa.selenium.base_page import BasePage

logger = get_logger(__name__)

class ElementsPage(BasePage):

    # locators
    # text box menu item
    text_box_menu_item = (By.ID, "item-0")
    user_name_input = (By.ID, "userName")
    email_input = (By.ID, "email")
    current_address_input = (By.ID, "currentAddress")
    permanent_address_input = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")
    user_name_paragraph = (By.ID, "name")

    # check_box menu item
    check_box_menu_item = (By.ID, "item-1")    
    check_box_title = (By.CSS_SELECTOR, "h1[class='text-center']")


    def __init__(self, driver):
        super().__init__(driver)
        
    
    def click_text_box_menu_item(self):
        self.click_element(self.text_box_menu_item)
        
    def get_text_box_menu_item(self):
        return self.find_element(self.text_box_menu_item)
        
    def enter_user_name(self, user_name):
        self.enter_text(self.user_name_input, user_name)
    
    def click_submit_button(self):
        self.scroll_to_element(self.submit_button)
        self.click_element(self.submit_button)
    
    def get_user_name(self):
        return self.find_element(self.user_name_paragraph)
        
    def get_check_box_title(self):
        return self.find_element(self.check_box_title)
        
    def click_check_box_menu_item(self):
        self.click_element(self.check_box_menu_item)
        