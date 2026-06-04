from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent

class AccountDetails(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page
        self.edit_name = page.get_by_role('textbox')
        self.save_button = page.get_by_role('button', name='Сохранить')
        self.edit_name = page.get_by_role('textbox')
        self.cancel_button = page.get_by_role('button', name='Отмена')
        self.edit_avatar = page.get_by_role("main").get_by_test_id("avatar")

    def tab_account_details(self):
        self.edit_name.fill('Ошибка Суперадмин1')
        self.save_button.click()
        self.edit_name.fill('Ошибка Суперадмин12')
        self.cancel_button.click()
        self.edit_avatar.click()