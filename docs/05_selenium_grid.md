## Selenium Grid

1. Prerequisites
   - Java 11 or higher installed
   - Browser(s) installed
   - Browser driver(s)
   - Download the Selenium Server jar file from the latest release

2. Start the Grid
    Start the grid hub/standalone
    ```bash
    java -jar selenium-server-<version>.jar standalone
    ```
    Detect drivers

    ```bash
    java -jar selenium-server-4.35.0.jar node --detect-drivers true
    ```
1. Point* your WebDriver tests to http://localhost:4444

Grid Roles
- Standalone
- Hub
- Hub and Node
- Node

Example

```python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Define the URL of your Selenium Grid Hub
grid_url = "http://localhost:4444/wd/hub"  # Replace with your Hub's address if different

# Set desired capabilities for the test
# This specifies that you want to run the test on a Chrome browser
# You can customize these options based on your Grid's capabilities and testing needs
options = ChromeOptions()
options.browser_version = 'latest'  # Request the latest available Chrome version
options.platform_name = 'linux'    # Or 'windows', 'mac' depending on your node OS

# Create a RemoteWebDriver instance, connecting to the Grid Hub
driver = webdriver.Remote(
    command_executor=grid_url,
    options=options
)

try:
    print(f"Session started. Session ID: {driver.session_id}")

    # Navigate to a website
    driver.get("https://www.google.com")
    print(f"Page title: {driver.title}")

    # Perform some actions on the page
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Grid Python Example")
    search_box.submit()
    print("Search performed.")    
    # You can add further assertions or interactions here
    # For example, verifying search results

finally:
    # Always quit the driver to release the session on the grid
    driver.quit()
    print("Session closed.")
```
