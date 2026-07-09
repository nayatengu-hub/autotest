from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent

class UsersRoles(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page
        self.open_tab = page.locator("p").filter(has_text="Пользователи и роли")
        self.heading_users = page.get_by_role("heading", name="Пользователи и роли")
        self.column_header_no = page.get_by_role("heading", name="п/п")
        self.column_header_name = page.get_by_role("heading", name="Имя пользователя")
        self.column_header_email = page.get_by_role("heading", name="Почта")
        self.column_header_role = page.get_by_role("heading", name="Текущая роль")
        self.column_header_registration = page.get_by_role("heading", name="Дата регистрации")
        self.column_header_status = page.get_by_role("heading", name="Статус")
        self.column_actions = page.get_by_role("row").filter(has_text="anroska25@gmail.com").get_by_test_id("menuViaDots.trigger").first
        self.edit_user = page.get_by_test_id("menuViaDots.menu.item-0")
        self.button_cancel = page.get_by_role("button", name="Отмена")
    
    def tab_users_roles(self):
        self.open_tab.click()
        self.heading_users.is_visible()
        self.column_header_no.is_visible()
        self.column_header_name.is_visible()
        self.column_header_email.is_visible()
        self.column_header_role.is_visible()
        self.column_header_registration.is_visible()
        self.column_header_status.is_visible()
        self.column_actions.click()
        self.edit_user.click()
        self.button_cancel.click()


    


        








        