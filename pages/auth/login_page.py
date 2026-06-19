from playwright.sync_api import Page
from pages.base_page import BasePage
from components.auth.login_form_component import LoginFormComponent

class LoginPage(BasePage):
    path = "/auth/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self.login_form = LoginFormComponent(page)