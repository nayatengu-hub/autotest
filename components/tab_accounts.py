from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent
from playwright.sync_api import expect

class TableAccounts(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page     
        self.accounts_tab = page.get_by_role('tab', name='Аккаунты')  
        self.name_table = page.get_by_role('heading', name='Аккаунты', level=2)
        self.column_header_no = page.get_by_role('columnheader', name='п/п')
        self.column_header_account = page.get_by_role('columnheader', name='Аккаунт')
        self.column_header_registrationdate = page.get_by_role('columnheader', name='Дата регистрации')
        self.column_header_balance = page.get_by_role('columnheader', name='Баланс ₽')
        self.column_header_stands = page.get_by_role('columnheader', name='Стенды')
        self.column_header_invoices = page.get_by_role('columnheader', name='Счета')
        self.column_header_upd = page.get_by_role('columnheader', name='УПД')
        self.column_header_refunds = page.get_by_role('columnheader', name='Возвраты')

    def table_elements(self):
        self.accounts_tab.click()
        expect(self.name_table).to_be_visible()
        expect(self.column_header_no).to_be_visible()
        expect(self.column_header_account).to_be_visible()
        expect(self.column_header_registrationdate).to_be_visible()
        expect(self.column_header_balance).to_be_visible()
        expect(self.column_header_stands).to_be_visible()
        expect(self.column_header_invoices).to_be_visible()
        expect(self.column_header_upd).to_be_visible()
        expect(self.column_header_refunds).to_be_visible()


