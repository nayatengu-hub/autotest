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

        # Click the exact button next to H1
        btn = page.locator("h1").first.locator("..").locator("button").first
        if btn.is_visible():
            btn.click()
            page.wait_for_timeout(2000)
            print(f"URL after clicking + button: {page.url}")
            print("Modal or page text:")
            print(page.get_by_role("heading").all_inner_texts())

        # Also check dot menu delete button logic
        print("Checking delete from dot menu...")
        row = page.locator("tbody tr").first
        if row.is_visible():
            dot = row.locator("[data-testid='menuViaDots.trigger']")
            dot.click()
            page.wait_for_timeout(500)
            page.get_by_role("menuitem", name="Удалить").click()
            page.wait_for_timeout(500)
            print("Bottom bar visible:", page.get_by_text("Хотите удалить уведомление?").is_visible())

        browser.close()

debug()
