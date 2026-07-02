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

        # In component the button is: page.get_by_test_id("iconButton").first
        button = page.get_by_test_id("iconButton").first
        print(f"Clicking button: {button.inner_text()}")
        button.click()
        page.wait_for_timeout(2000)

        print(f"Current URL after click: {page.url}")

        # Let's see if the modal is open or if we are on a new page.
        # Let's print headings
        print("Headings after click:")
        for heading in page.get_by_role("heading").all():
            print(heading.inner_text())

        browser.close()

debug()
