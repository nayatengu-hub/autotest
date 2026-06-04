from playwright.sync_api import Page
from pages.base_page import BasePage
from components.sidebar.section_accounts_components import SectionAccounts



class SectionAccountsPage(BasePage):
    path = "/home/accounts"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.section_accounts = SectionAccounts(page)