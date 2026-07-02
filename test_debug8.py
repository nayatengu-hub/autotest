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

        # Click recipient input
        recipient_input = page.get_by_test_id("outlinedInput").first
        if recipient_input.is_visible():
            recipient_input.click()
            page.wait_for_timeout(1000)
            print("Modal opened for recipients. Finding checkboxes...")

            # Print checkboxes and text inside modal
            for row in page.locator("[role='dialog'], [role='presentation']").locator("tbody tr").all():
                print("Row text:", row.inner_text().replace('\n', ' | '))

            for cb in page.get_by_role("checkbox").all():
                 print("Checkbox found")

        browser.close()

debug()
