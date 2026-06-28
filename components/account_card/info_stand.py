from typing import Optional
from playwright.sync_api import Page, Locator, expect
from components.base_component import BaseComponent
import re


class InfoStand(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page 

        # Открытие вкладки
        self.dott = page.get_by_role("row", name="1 test-1 26.06.2026 13:55").get_by_test_id("menuViaDots.trigger")
        self.card_card = page.get_by_test_id("menuViaDots.menu.item-0")
        
        # Проверка наличие вкладок
        self.open_tab_stand_parameters = page.get_by_role("button", name="Параметры стенда")
        self.open_tab_statistics = page.get_by_role("button", name="Статистика")

        #  Вкладка "Параметры стенда"
        # Проверка полей
        self.page_title = page.get_by_role("heading", name="Параметры стенда")
        self.free_period_input = page.locator("div").filter(has_text=re.compile(r"Бесплатный период \(в днях\)")).locator("input")
        self.block_period_input = page.locator("div").filter(has_text=re.compile(r"^Период блокировки \(в днях\)$")).locator("input")

    def verify_all_informational_fields(self, expected: dict):
        # Проверяем, что заголовок страницы на месте
        expect(self.page_title).to_be_visible()

        # 1. Проверка статических текстовых полей (значений)
        expect(self.page.get_by_text(expected["name"], exact=True)).to_be_visible()
        expect(self.page.get_by_text(expected["created_date"])).to_be_visible()
        expect(self.page.get_by_text(str(expected["users_count"]), exact=True)).to_be_visible()
        expect(self.page.get_by_text(expected["cluster"], exact=True)).to_be_visible()
        expect(self.page.get_by_text(expected["status"], exact=True)).to_be_visible()
        expect(self.page.get_by_text(str(expected["charge_per_day"]), exact=True)).to_be_visible()
        expect(self.page.get_by_text(expected["available_until"])).to_be_visible()
        
        # 2. Проверка заполненных значений внутри инпутов (полей ввода)
        expect(self.free_period_input).to_have_value(str(expected["free_period"]))
        expect(self.block_period_input).to_have_value(str(expected["block_period"]))
