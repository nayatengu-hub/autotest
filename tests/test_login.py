from pages.login_page import LoginPage
import config

def test_login(guest_page):
    login_page = LoginPage(guest_page)
    login_page.navigate() # Перейдет на /auth/login текущего стенда (благодаря base_url)
    login_page.login_form.login(username=config.username, password=config.password)
    

# expect: (guest_page).to_have_url("**/stands")