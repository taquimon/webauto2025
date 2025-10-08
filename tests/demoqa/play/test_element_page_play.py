import re
import time

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/")
    page.get_by_role("heading", name="Elements").click()
    page.get_by_text("Text Box").click()
    #page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Edwin Taquichiri")
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("Name:Edwin Taquichiri").click()

def test_example_checkbox(page: Page) -> None:
    page.goto("https://demoqa.com/")
    page.get_by_role("heading", name="Elements").click()
    page.get_by_text("Check Box").click()
    page.locator("#tree-node").get_by_role("img").nth(3).click()
    page.get_by_role("button", name="Toggle").click()
    time.sleep(10)