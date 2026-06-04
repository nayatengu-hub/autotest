from playwright.sync_api import expect
from pages.profile.account_page import AccountPage

def test_account_page(auth_user_page):
    account_page = AccountPage(auth_user_page)
    account_page.navigate()
    account_page.account_details.tab_account_details()
    account_page.tab_security.tab_security()
    account_page.tab_users_roles.tab_users_roles()
    

    auth_user_page.wait_for_url("**/account")
