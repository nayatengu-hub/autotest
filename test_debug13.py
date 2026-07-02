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

        row = page.locator("tbody tr").first
        dot = row.locator("[data-testid='menuViaDots.trigger']")
        dot.click()
        page.wait_for_timeout(1000)
        print("Menu items text content:")
        for mi in page.locator("[role='menuitem']").all():
            print("MI:", mi.inner_text().strip())

        browser.close()

debug()
