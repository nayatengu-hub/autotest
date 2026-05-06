from playwright.sync_api import Page, Locator
from typing import Optional

class BaseComponent:
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        self.page = page
        self.root_locator = root_locator