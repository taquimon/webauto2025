from playwright.sync_api import Page, Locator
from pages.demoqa.play.base_page_play import BasePagePlay

class FormsPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.practice_form_menu : Locator = page.get_by_role("listitem").get_by_text("Practice Form")
        self.first_name : Locator = page.get_by_role("textbox", name="First Name")
        self.last_name : Locator = page.get_by_role("textbox", name="Last Name")
        self.email : Locator = page.get_by_role("textbox", name="name@example.com")
        self.gender : Locator = page.get_by_text("Male", exact=True)
        self.mobile_number : Locator = page.get_by_role("textbox", name="Mobile Number")
        self.hobbies : Locator = page.get_by_text("Sports")
        self.hobbies_2 : Locator = page.get_by_text("Reading")
        self.hobbies_3 : Locator = page.get_by_text("Music")
        self.state : Locator = page.locator("#state svg")
        options = {
            "NCR" : ["Delhi", "Gurgaon", "Noida", "Other"], 
            "Uttar Pradesh" : ["Agra", "Lucknow", "Other"], 
            "Haryana" : ["Delhi", "Gurgaon", "Noida", "Other"], 
            "Rajasthan" : ["Delhi", "Gurgaon", "Noida", "Other"]
        }
        self.city : Locator = page.locator("#city svg")
        options = ["Delhi", "Gurgaon", "Noida", "Other"]
        self.submit_button : Locator = page.get_by_role("button", name="Submit")

        
    def navigate(self):
        self.navigate_url(url="http://demoqa.com/forms")

    def click_on_practice_form_menu(self):
        self.click_element(self.practice_form_menu)
    
    def click_on_first_name(self):
        self.click_element(self.first_name)
    
    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)
    
    def click_on_last_name(self):
        self.click_element(self.last_name)
    
    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)
    
    def click_on_email(self):
        self.click_element(self.email)
    
    def enter_email(self, email):
        self.enter_text(self.email, email)
    
    def click_on_gender(self):
        self.click_element(self.gender)
    
    def click_on_mobile_number(self):
        self.click_element(self.mobile_number)
    
    def enter_mobile_number(self, mobile_number):
        self.enter_text(self.mobile_number, mobile_number)
    
    def click_on_hobbies(self):
        self.click_element(self.hobbies)
    
    def click_on_hobbies_2(self):
        self.click_element(self.hobbies_2)
    
    def click_on_hobbies_3(self):
        self.click_element(self.hobbies_3)
    
    def click_on_state(self):
        self.click_element(self.state)
    
    def click_on_city(self):
        self.click_element(self.city)
    
    def click_on_submit_button(self):
        self.click_element(self.submit_button)
    
    def click_on_submit_button(self):
        self.click_element(self.submit_button)
    #     self.click_element(self.text_box)
        
    # def enter_username(self, username):
    #     self.enter_text(self.username, username)
    
    # def click_submit_button(self):
    #     self.click_element(self.submit_button)