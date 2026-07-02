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

        # Let's find the correct "+" button. It should be right after the <h1> Уведомления
        h1 = page.get_by_role("heading", name="Уведомления")
        # In MUI, buttons are often siblings or near the h1
        print("Finding all buttons...")
        for btn in page.get_by_role("button").all():
            try:
                html = btn.evaluate("node => node.outerHTML")
                if "Icon" in html or "svg" in html:
                    print(f"Button HTML: {html[:150]}...")
            except:
                pass

        browser.close()

debug()
