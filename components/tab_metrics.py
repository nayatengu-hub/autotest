from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent
from playwright.sync_api import expect

class BlocksMetrics(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page
        self.metrics_tab = page.get_by_role('tab', name='Показатели')
        self.name_blocks = page.get_by_role('heading', name='Показатели', level=4)
        # self.dots_indicators = page.
        self.block_average_bill = page.get_by_text('Средний чек списания')
        self.block_average_number_users = page.get_by_text('Среднее число пользователей')
        self.block_account_balance = page.get_by_text('Баланс по аккаунтам')
        self.block_outflow_from_stands = page.get_by_text('Отток по стендам')
        self.block_deleted_new_accounts = page.get_by_text('Удаленные/новые аккаунты')

    def ckeck_block_elements(self):
        self.metrics_tab.click()
        expect(self.name_blocks).to_be_visible()
        expect(self.block_average_bill).to_be_visible()
        expect(self.block_average_number_users).to_be_visible()
        expect(self.block_account_balance).to_be_visible()
        expect(self.block_outflow_from_stands).to_be_visible()
        expect(self.block_deleted_new_accounts).to_be_visible()
