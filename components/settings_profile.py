from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent

class SettingsProfile(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page
        self.button_profile = page.get_by_role('button', name='superadmin')
        self.set_up_profile = page.get_by_role('menuitem', name='Настроить профиль')

    def go_to_settings(self):
        self.button_profile.click()
        self.set_up_profile.click()