import time
import pytest
from playwright.sync_api import Page

class TestBookStorePlay:

    def test_example(self, page: Page) -> None:
        page.goto("https://demoqa.com/")
        page.get_by_role("heading", name="Book Store Application").click()
        page.get_by_role("list").get_by_text("Login").click()
        page.get_by_role("button", name="New User").click()
        page.get_by_role("textbox", name="First Name").click()
        page.get_by_role("textbox", name="First Name").fill("John2")
        page.get_by_role("textbox", name="First Name").press("Tab")
        page.get_by_role("textbox", name="Last Name").fill("Wick2")
        page.get_by_role("textbox", name="UserName").click()
        page.get_by_role("textbox", name="UserName").fill("jwick2")
        # page.get_by_role("textbox", name="Password").click()
        # page.get_by_role("textbox", name="Password").fill("password")        
        # page.get_by_role("button", name="Register").click()
        # page.get_by_role("textbox", name="Password").click()
        # page.get_by_role("textbox", name="Password").press("Shift+Home")
        # page.get_by_role("textbox", name="Password").fill("Password!")
        #page.locator("iframe[name='a-mo7ob6qvg1t8']").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
        # page.get_by_role("button", name="Register").click()
        # page.get_by_role("textbox", name="Password").click()
        # page.get_by_role("textbox", name="Password").press("Shift+Home")
        page.get_by_role("textbox", name="Password").fill("Password!2025")
        page.locator("iframe[name*='a-']").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
        
        # imagen captcha
        
        #page.locator("iframe[name=\"a-13qx1a-ofm7yu\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name="Register").click()
        time.sleep(10)
        page.get_by_text("Login", exact=True).click()
        page.get_by_role("textbox", name="UserName").click()
        page.get_by_role("textbox", name="UserName").fill("jwick")
        page.get_by_role("textbox", name="UserName").press("Tab")
        page.get_by_role("textbox", name="Password").fill("Password!2025")
        page.get_by_role("button", name="Login").click()
        page.get_by_text("jwick").click()
        
