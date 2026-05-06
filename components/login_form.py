from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent

class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        root = self.root_locator if self.root_locator else self.page
        self.username_input = root.get_by_role('textbox', name='Телефон или почта')
        self.password_input = root.get_by_role('textbox', name='Пароль')
        self.login_button = root.get_by_role('button', name='Войти')

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()