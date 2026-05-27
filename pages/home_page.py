from playwright.sync_api import Page
from pages.base_page import BasePage
from components.page_layout import PageLayout
from components.tab_accounts import TableAccounts
from components.tab_metrics import BlocksMetrics
from components.page_header_admin import PageHeaderAdmin
from components.settings_profile import SettingsProfile


class HomePage(BasePage):
    path = "/home/accounts"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_layout = PageLayout(page)
        self.table_accounts = TableAccounts(page)
        self.block_metrics = BlocksMetrics(page)
        self.page_header_admin = PageHeaderAdmin(page)
        self.set_profile = SettingsProfile(page)
        
