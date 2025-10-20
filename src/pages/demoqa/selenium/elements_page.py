import time 
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from pages.demoqa.selenium.base_page import BasePage

logger = get_logger(__name__)
class ElementsPage(BasePage):
    
    text_box_menu_item = (By.ID, "item-0")
    check_box_menu_item = (By.ID, "item-1")     
    links_option = (By.ID, "item-5")

    check_box_title = (By.CSS_SELECTOR, "h1[class='text-center']")

    def click_text_box_menu_item(self):
        self.click_element(self.text_box_menu_item)
        return ElementsTextBoxPage(self.driver)
        
    def get_text_box_menu_item(self):
        return self.find_element(self.text_box_menu_item)        

    def click_check_box_menu_item(self):
        self.click_element(self.check_box_menu_item)

    def get_check_box_title(self):
        return self.find_element(self.check_box_title)      

    def click_links_option(self):        
        self.click_element(self.links_option)
        return ElementsLinksPage(self.driver)                  

# page Fragement
class ElementsTextBoxPage(BasePage):

    # locators
    # text box menu item
    
    user_name_input = (By.ID, "userName")
    email_input = (By.ID, "email")
    current_address_input = (By.ID, "currentAddress")
    permanent_address_input = (By.ID, "permanentAddress")
    submit_button = (By.ID, "submit")
    user_name_paragraph = (By.ID, "name")
    


    def __init__(self, driver):
        super().__init__(driver)                
        
    def enter_user_name(self, user_name):
        self.enter_text(self.user_name_input, user_name)
    
    def click_submit_button(self):
        self.scroll_to_element(self.submit_button)
        self.click_element(self.submit_button)
    
    def get_user_name(self):
        return self.find_element(self.user_name_paragraph)
        
        

class ElementsCheckBoxPage(BasePage):
    # check_box menu item    
    check_box_title = (By.CSS_SELECTOR, "h1[class='text-center']")

# class ElementsRadioButtonPage(BasePage):
#     passed

# class ElementsWebTablesPage(BasePage):    
#     passed

class ElementsLinksPage(BasePage): 
    
    created_link = (By.ID, "created")
    no_content_link = (By.ID, "no-content")
    moved_link = (By.ID, "moved")
    bad_request_link = (By.ID, "bad-request")
    unauthorized_link = (By.ID, "unauthorized")
    forbidden_link = (By.ID, "forbidden")    
    not_found_link = (By.ID, "invalid-url")
    response_message = (By.ID, "linkResponse")

    locators_link = {
        "created": created_link,
        "no-content": no_content_link,
        "moved": moved_link,
        "bad-request": bad_request_link,
        "unauthorized": unauthorized_link,
        "forbidden": forbidden_link,
        "not-found": not_found_link
    }

    def click_created_link(self):
        self.click_element(self.created_link)        
    
    def click_no_content_link(self):
        self.click_element(self.no_content_link)
    
    def click_moved_link(self):
        self.click_element(self.moved_link)
    
    def click_bad_request_link(self):
        self.click_element(self.bad_request_link)
    
    def click_unauthorized_link(self):
        self.click_element(self.unauthorized_link)
    
    def click_forbidden_link(self):
        self.click_element(self.forbidden_link)
    
    def click_not_found_link(self):
        self.click_element(self.not_found_link)

    def get_response_message(self):
        time.sleep(2)
        return self.find_element(self.response_message).text
    
    def click_link_option(self, link):
        self.scroll_to_element(self.locators_link[link])
        self.click_element(self.locators_link[link])   
        