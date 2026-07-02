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

        # Check dot menu delete button logic again
        print("Checking delete from dot menu...")
        row = page.locator("tbody tr").first
        if row.is_visible():
            dot = row.locator("[data-testid='menuViaDots.trigger']")
            dot.click()
            page.wait_for_timeout(500)
            print("Menu items:")
            for item in page.locator("[role='menuitem']").all():
                print(item.inner_text())

            del_btn = page.locator("[role='menuitem']", has_text="Удалить")
            if del_btn.is_visible():
                 del_btn.click()
                 page.wait_for_timeout(500)
                 print("Bottom bar visible after click:", page.get_by_text("Хотите удалить уведомление?").is_visible())
                 print("Bottom bar cancel button:", page.get_by_role("button", name="Отменить").is_visible())

        browser.close()

debug()
