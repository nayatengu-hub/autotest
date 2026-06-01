from pages.auth.login_page import LoginPage
import config
from playwright.sync_api import expect

def test_login(guest_page):
    login_page = LoginPage(guest_page)
    login_page.navigate() # Перейдет на /auth/login текущего стенда (благодаря base_url)
    login_page.login_form.login(username=config.username, password=config.password)
    

    guest_page.wait_for_url("**/home/accounts")