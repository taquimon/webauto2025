from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class ElementsPageFactory(PageFactory):
    def __init__(self, driver):
        self.driver = driver    	# Required
        self.timeout = 15      		#(Optional - Customise your explicit wait for every webElement,Default 10sec)
        self.highlight = True   	#(Optional - To highlight every webElement in PageClass)
        self.mobile_test = False

    locators = {
        "text_box_item": ('id', 'item-0'),
        "username_text_box": ('id', 'userName'),
        "email_text_box": ('id', 'userEmail'),
        "current_address_text_box": ('id', 'currentAddress'),
        "permanent_address_text_box": ('id', 'permanentAddress'),
        "submit_button": ('id', 'submit')
    }

    def click_text_box_item(self):
        self.text_box_item.click()

    def enter_user_name(self, username):
        self.username_text_box.send_keys(username)