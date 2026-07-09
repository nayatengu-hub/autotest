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
        self.column_header_stands = page.get_by_test_id("uniTable.header.row").locator("div").filter(has_text="Стенды")
        self.column_header_invoices = page.get_by_test_id("uniTable.header.row").locator("div").filter(has_text="Счета")
        self.column_header_upd = page.get_by_test_id("uniTable.header.row").locator("div").filter(has_text="УПД")
        self.column_header_refunds = page.get_by_test_id("uniTable.header.row").locator("div").filter(has_text="Возвраты")
        # Улучшенный локатор без привязки к жесткой дате/времени и индексу "1 "
        self.dott_menu = page.get_by_role("row").filter(has_text="anroska25@gmail.com").get_by_test_id("menuViaDots.trigger").first
        self.button_open = page.get_by_test_id("menuViaDots.menu.item-0")
        self.sidebar_accounts = page.get_by_role('button', name='Аккаунты')
        # Улучшенный локатор - Аккаунт-11 может быть изменен
        self.name_acc_link = page.get_by_role("link").filter(has_text="Аккаунт").first
    
    def section_accounts(self):
        self.sidebar_accounts.click()
        expect(self.page_title_accounts).to_be_visible()
        expect(self.page_heading_accounts).to_be_visible()
        expect(self.column_header_no).to_be_visible()
        expect(self.column_header_account).to_be_visible()
        expect(self.column_header_registrationdate).to_be_visible()
        expect(self.column_header_balance).to_be_visible()
        expect(self.column_header_stands).to_be_visible()
        expect(self.column_header_invoices).to_be_visible()
        expect(self.column_header_upd).to_be_visible()
        expect(self.column_header_refunds).to_be_visible()

        # Ожидаем появления меню
        self.dott_menu.click()
        self.button_open.wait_for(state="visible", timeout=10000)
        self.button_open.click(force=True)
        # В сайдбаре может быть скрыто/открыто, клик по ссылке аккаунта.
        # force=True нужно, так как открытое меню может перекрывать клик
        self.name_acc_link.click(force=True)
        
