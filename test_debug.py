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
        page.wait_for_timeout(5000)

        # 1. Print dot menu items for the first row
        first_row_menu = page.locator("tbody tr").first.locator("[data-testid='menuViaDots.trigger']")
        if first_row_menu.is_visible():
            first_row_menu.click()
            page.wait_for_timeout(1000)
            print("Dot menu items:")
            for item in page.locator("[role='menuitem']").all():
                print(item.inner_text())
            page.keyboard.press("Escape")
        else:
            print("No rows found for dot menu")

        # 2. Try to trigger bottom bar (e.g. by clicking "Delete" or something?)
        # Let's find out how the bottom bar appears. It says "Хотите удалить уведомление?"
        # So it probably appears when you click "Удалить" in the dot menu.

        # 3. Try to open the create notification page
        send_btn = page.locator("button, a").filter(has_text="+").first
        if not send_btn.is_visible():
            # In the screenshot it's an orange circle with a plus sign, which might just be an SVG inside a button.
            # Let's find the button by color or position, or next to "Уведомления" heading
            heading = page.get_by_role("heading", name="Уведомления")
            send_btn = page.locator("button").filter(has=page.locator("svg")).nth(1) # Just guessing

        print("Finding send button...")
        # Print all buttons with svg
        for btn in page.locator("button:has(svg)").all():
             print(f"Button with SVG: {btn.get_attribute('aria-label')} | {btn.get_attribute('data-testid')}")

        browser.close()

debug()
