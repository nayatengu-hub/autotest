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

            print("Finding all tables in the page:")
            for table in page.locator("table").all():
                print("Table found. First row HTML:")
                try:
                    print(table.locator("tr").nth(1).evaluate("node => node.outerHTML"))
                except:
                    print("No rows")

        browser.close()

debug()
