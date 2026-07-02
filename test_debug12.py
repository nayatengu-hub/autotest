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
        page.goto("/notifications/add")
        page.wait_for_timeout(3000)

        # We found two textboxes with no name/label. Let's see what happens if we type in the second one.
        inputs = page.get_by_role("textbox")
        if inputs.count() >= 2:
            print("Typing in second textbox...")
            inputs.nth(1).fill("test description")
            print("Successfully typed in second textbox.")
        else:
            print("Not enough textboxes found.")

        browser.close()

debug()
