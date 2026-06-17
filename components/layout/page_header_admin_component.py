from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent
from playwright.sync_api import expect

class PageHeaderAdmin(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page
        self.page_title_admin = page.get_by_role('heading', name='Рабочее место администратора')
        self.accounts_tab = page.get_by_role('tab', name='Аккаунты')
        self.metrics_tab = page.get_by_role('tab', name='Показатели')
        self.stands_tab = page.get_by_role("tab", name="Стенды")
        self.invoices_tab = page.get_by_role("tab", name="Счета")
        self.upd_tab = page.get_by_role("tab", name="УПД")
        self.refunds_tab = page.get_by_role("tab", name="Заявки на возврат")

    def switch_to_tab(self):
        expect(self.accounts_tab).to_be_visible()
        self.accounts_tab.click()
        self.metrics_tab.click()
        self.stands_tab.click()
        self.invoices_tab.click()
        self.upd_tab.click()
        self.refunds_tab.click()