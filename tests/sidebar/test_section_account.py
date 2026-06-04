from playwright.sync_api import Page
from pages.sidebar.section_account_page import SectionAccountsPage

def test_sidebar_page(auth_sidebar_page):
        sidebar_page = SectionAccountsPage(auth_sidebar_page)
        sidebar_page.navigate()
        sidebar_page.section_accounts.section_accounts()