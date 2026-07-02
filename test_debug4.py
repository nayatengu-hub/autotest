import pytest
from playwright.sync_api import sync_playwright
import config

def debug():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            base_url=config.base_url,
            storage_state="data/auth_admin_state.json"
        )
        page = context.new_page()
        page.goto("/notifications/received")
        page.wait_for_timeout(3000)

        print("Finding links:")
        for link in page.locator("a").all():
            try:
                href = link.get_attribute("href")
                if href and "create" in href or "add" in href:
                    print(f"Link: {href}")
            except:
                pass

        print("Trying click + button icon")
        # In the screenshot, it's an orange circle with + icon.
        # Usually MUI AddIcon is used.
        try:
            svg = page.locator("svg[data-testid='AddIcon']")
            if svg.is_visible():
                print("Found AddIcon SVG")
                btn = svg.locator("..")
                print(btn.evaluate("node => node.tagName"))
                btn.click()
                page.wait_for_timeout(2000)
                print(f"URL is now: {page.url}")
        except:
            pass

        browser.close()

debug()
