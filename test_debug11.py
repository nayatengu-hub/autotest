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

        print("Finding inputs for message body")
        # Text areas, rich text editors
        for textbox in page.get_by_role("textbox").all():
            print(f"Textbox name/aria-label: {textbox.get_attribute('name')} / {textbox.get_attribute('aria-label')}")

        print("Finding Quill or similar editors")
        try:
             print(page.locator(".ql-editor").count())
             print(page.locator("textarea").count())
        except:
             pass

        browser.close()

debug()
