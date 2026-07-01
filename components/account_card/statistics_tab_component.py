from typing import Optional
from playwright.sync_api import Page, Locator, expect
from components.base_component import BaseComponent


class StatisticsTab(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page

        # Заголовок вкладки (внутри области контента)
        self.title = page.get_by_role("heading", name="Список показателей")

        # Заголовки колонок таблицы
        self.column_indicator = page.get_by_role("columnheader", name="Показатель")
        self.column_total = page.get_by_role("columnheader", name="Всего")
        self.column_dynamics = page.get_by_role("columnheader", name="Динамика %")

    def verify_opened(self):
        expect(self.title).to_be_visible()
        expect(self.column_indicator).to_be_visible()
        expect(self.column_total).to_be_visible()
        expect(self.column_dynamics).to_be_visible()
