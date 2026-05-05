from playwright.sync_api import Page
from login_page import LoginPage
from config import username, password

def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username=username, password=password)