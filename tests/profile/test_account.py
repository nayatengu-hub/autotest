from playwright.sync_api import expect
from pages.profile.account_page import AccountPage

def test_account_page(auth_user_page):
    account_page = AccountPage(auth_user_page)
    account_page.navigate()

    auth_user_page.wait_for_url("**/account")
