from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent

class TabSecurity(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page
        self.open_tab = page.get_by_role("button", name="Безопасность")
        self.heading_contact = page.get_by_role("heading", name="Контакты")
        self.field_phone_number = page.get_by_role("textbox", name="Номер телефона")
        self.field_email = page.get_by_role("textbox", name="Электронная почта")
        self.heading_password = page.get_by_text("Пароль", exact=True)
        self.change_password = page.get_by_role("button", name="Изменить")
        self.field_current_password = page.get_by_role("textbox", name="Текущий пароль")
        self.field_new_password = page.get_by_role("textbox", name="Новый пароль")
        self.field_confirm_password = page.get_by_role("textbox", name="Повтор пароля *")

    def tab_security(self):
        self.open_tab.click()
        self.heading_contact.is_visible()
        self.field_phone_number.is_visible()
        self.field_email.is_visible()
        self.heading_password.is_visible()
        self.change_password.click()
        self.field_current_password.is_visible()
        self.field_new_password.is_visible()
        self.field_confirm_password.is_visible()