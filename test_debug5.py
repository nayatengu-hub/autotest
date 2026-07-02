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

        print("Page HTML around 'Уведомления':")
        # Find the h1 and print its parent HTML
        h1 = page.locator("h1").first
        if h1.is_visible():
            print(h1.locator("..").evaluate("node => node.outerHTML"))

        browser.close()

debug()
