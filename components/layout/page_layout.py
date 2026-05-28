from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent
from playwright.sync_api import expect

class PageLayout(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page
        self.breadcrumbs_home = page.get_by_role('button', name='Главная')
        self.sidebar_home = page.get_by_role('button', name='Панель управления')
        self.sidebar_accounts = page.get_by_role('button', name='Аккаунты')
        self.stands = page.get_by_role('button', name='Стенды')
        self.finances = page.get_by_role('button', name='Финансы')
        self.documents = page.get_by_role('button', name='Документы')
        self.notifications = page.get_by_role('button', name='Уведомления')
        self.account = page.get_by_role('button', name='Мой аккаунт')
        self.presets = page.get_by_role('button', name='Пресеты')


    def checking_elements(self):
        expect(self.breadcrumbs_home).to_be_visible()
        expect(self.sidebar_home).to_be_visible()
        expect(self.sidebar_accounts).to_be_visible()
        expect(self.stands).to_be_visible()
        expect(self.documents).to_be_visible()
        expect(self.notifications).to_be_visible()
        expect(self.account).to_be_visible()
        expect(self.presets).to_be_visible()

        
      

