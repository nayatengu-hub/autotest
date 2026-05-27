from playwright.sync_api import Page
from config import base_url

class BasePage:
    path = ""
    
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{base_url}{self.path}")

    def check_url(self, expected_url: str):
        assert self.page.url == expected_url

