from playwright.async_api import Page, Locator, async_playwright, expect
import asyncio
import time

class AsyncLandingPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "http://demoqa.com/"

        # locators
        self.elements : Locator = page.get_by_role("heading").get_by_text("Elements")
        self.forms : Locator = page.get_by_role("heading").get_by_text("Forms")
        self.alerts_frames_windows : Locator = page.get_by_role("heading").get_by_text("Alerts, Frame & Windows")
        self.widgets : Locator = page.get_by_role("heading").get_by_text("Widgets")
        self.interactions : Locator = page.get_by_role("heading").get_by_text("Interactions")
        self.book_store : Locator = page.get_by_role("heading").get_by_text("Book Store Application")
    
    async def navigate(self):
        await self.page.goto(self.url)
    
    async def click_on_elements(self):
        await self.elements.click()
    
    async def click_on_forms(self):
        await self.forms.click()
        


async def main():
    start_time = time.time()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        landing_page = AsyncLandingPage(page)
        await landing_page.navigate()
        await expect(landing_page.elements).to_be_visible()
        await expect(landing_page.elements).to_contain_text("Elements")        
        await expect(landing_page.forms).to_contain_text("Forms")
        await expect(landing_page.alerts_frames_windows).to_contain_text("Alerts, Frame & Windows")
        await expect(landing_page.widgets).to_contain_text("Widgets")
        await expect(landing_page.interactions).to_contain_text("Interactions")
        await expect(landing_page.book_store).to_contain_text("Book Store Application")

        await browser.close()
    
    end_time = time.time()
    print(f"Test completed in {end_time - start_time:.2f} seconds")
    

if __name__ == "__main__":
    asyncio.run(main())
