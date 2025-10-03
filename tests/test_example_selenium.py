import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver (ensure you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.google.com")



# Find an element by its name attribute (e.g., the search bar)
search_box = driver.find_element(By.NAME, "q")

# Enter text into the search bar
search_box.send_keys("Selenium Python")

# Submit the form (or press Enter)
search_box.submit()
# time.sleep(5)

# Verify the page title after the search
# assert "Selenium Python - Google Search" in driver.title

# Close the browser
driver.quit()
