from playwright.sync_api import Page
from pages.login_page import LoginPage
from config import username, password

def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_form.login(username=username, password=password)