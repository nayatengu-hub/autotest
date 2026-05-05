from playwright.sync_api import Page
from base_page import BasePage


class LoginPage(BasePage):
    path = "/auth/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.get_by_role('textbox', name = 'Телефон или почта')
        self.password_input = page.get_by_role('textbox', name = 'Пароль')
        self.login_button = page.get_by_role('button', name = 'Войти')
    
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        
        