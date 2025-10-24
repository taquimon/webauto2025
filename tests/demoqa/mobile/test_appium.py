import time

import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from utils.logger import get_logger
# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# For W3C actions

logger = get_logger(__name__)


class TestAppium:
    def setup_class(self):
        options = AppiumOptions()
        options.load_capabilities(
            {
                "platformName": "android",
                "appium:deviceName": "Google Pixel 7",
                "appium:appiumVersion": "3.1.0",
                "appium:platformVersion": "14",
                "appium:automationName": "uiautomator2",
                "appium:ensureWebviewsHavePages": True,
                "appium:nativeWebScreenshot": True,
                "appium:newCommandTimeout": 3600,
                "appium:connectHardwareKeyboard": True,
                "appPackage": "com.android.settings",
            },
        )
        # create the driver
        self.driver = webdriver.Remote("http://192.168.0.12:4274", options=options)

    @pytest.mark.mobile
    def test_mobile_battery(self, log_test_name):
        # driver = webdriver.Remote("http://192.168.0.12:4274", options=options)
        battery_element = self.driver.find_element(
            AppiumBy.XPATH,
            '(//android.widget.RelativeLayout[@resource-id="com.android.settings:id/text_frame"])[5]',
        )
        logger.debug("Battery element: %s", battery_element.text)
        print(battery_element.text)
        battery_element.click()
        logger.debug("Battery element clicked")

        time.sleep(5)

    def teardown_class(self):
        self.driver.quit()
