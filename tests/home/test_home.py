from playwright.sync_api import Page
from pages.home.home_page import HomePage


def test_home(auth_admin_page):
    home_page = HomePage(auth_admin_page)
    home_page.navigate()
    home_page.block_metrics.ckeck_block_elements()
    home_page.table_accounts.table_elements()
    home_page.page_header_admin.switch_to_tab()
    home_page.page_layout.checking_elements()
    home_page.set_profile.go_to_settings(fullname='Ошибка Суперадмин')