from selenium.webdriver.common.by import By
import time
import logging
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger(__name__)


class BasePage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 10)
	
	def find_element(self, by_locator):
		logger.info(f"Finding element:  {by_locator}")
		return self.wait.until(EC.visibility_of_element_located(by_locator))
		
	def click_element(self, by_locator):        
		self.highlight(self.driver, self.find_element(by_locator))
		self.find_element(by_locator).click()		
		logger.info(f"Clicking element:  {by_locator}")
	
	def enter_text(self, by_locator, text):         
		self.find_element(by_locator).send_keys(text)
		logger.info(f"Entering text:  {text} on {by_locator}")
	
	def highlight(self, driver, element, effect_time=2, color="blue", border=5):
		"""
		Highlights (blinks) a Selenium Webdriver element
		"""
		def apply_style(s):
			driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
		
		original_style = element.get_attribute('style')
		apply_style("border: {0}px solid {1};".format(border, color))
		time.sleep(effect_time)
		apply_style(original_style)
		
	def scroll_to_element(self, by_locator):
		element = self.find_element(by_locator)
		self.driver.execute_script("arguments[0].scrollIntoView();", element)
		