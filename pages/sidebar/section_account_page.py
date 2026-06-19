from playwright.sync_api import Page
from pages.base_page import BasePage
from components.sidebar.section_accounts_components import SectionAccounts
from components.sidebar.section_stands_components import SectionStands




class SectionPage(BasePage):
    path = "/home/accounts"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.section_accounts = SectionAccounts(page) 
        self.section_stands = SectionStands(page)