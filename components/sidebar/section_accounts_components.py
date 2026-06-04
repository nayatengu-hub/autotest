from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent
from playwright.sync_api import expect

class SectionAccounts(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page 
        self.sidebar_accounts = page.get_by_role('button', name='Аккаунты')
        self.button_add = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-outlined")
        self.page_title_accounts = page.get_by_role('heading', name='Аккаунты', level=1)
        self.page_heading_accounts = page.get_by_role('heading', name='Аккаунты', level=2)
        self.column_header_no = page.get_by_role("heading", name="п/п")
        self.column_header_account = page.get_by_test_id("uniTable.header.row").get_by_role("heading", name="Аккаунт")
        self.column_header_registrationdate = page.get_by_role("heading", name="Дата регистрации")
        self.column_header_balance = page.get_by_role("heading", name="Баланс ₽")
        self.column_header_stands = page.get_by_role("heading", name="Стенды")
        self.column_header_invoices = page.get_by_role('heading', name='Счета')
        self.column_header_upd = page.get_by_role('heading', name='УПД')
        self.column_header_refunds = page.get_by_role('heading', name='Возвраты')
        self.dott_menu = page.get_by_role("row", name="1 Аккаунт-11 07.05.2026 18:19").get_by_test_id("menuViaDots.trigger")
        self.button_open = page.get_by_test_id("menuViaDots.menu.item-0")
        self.sidebar_accounts = page.get_by_role('button', name='Аккаунты')
        self.name_acc_link = page.get_by_role("link", name="Аккаунт-11")
    
    def section_accounts(self):
        self.sidebar_accounts.click()
        self.page_title_accounts.is_visible()
        self.page_heading_accounts.is_visible()
        self.column_header_no.is_visible()
        self.column_header_account.is_visible()
        self.column_header_registrationdate.is_visible()
        self.column_header_balance.is_visible()
        self.column_header_stands.is_visible()
        self.column_header_invoices.is_visible()
        self.column_header_upd.is_visible()
        self.column_header_refunds.is_visible()
        self.dott_menu.click()
        self.button_open.click()
        self.sidebar_accounts.click()
        self.name_acc_link.click()
        
