from typing import Optional
from playwright.sync_api import Page, Locator, expect
from components.base_component import BaseComponent
import re


class InfoStand(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page 

        # Открытие вкладки
        self.dott = page.get_by_role("row", name="3 test-1 26.06.2026 13:55").get_by_test_id("menuViaDots.trigger")
        self.card_card = page.get_by_test_id("menuViaDots.menu.item-0")
        self.menu_list = page.locator("ul[role='menu']")
        
        # Проверка наличие вкладок
        self.open_tab_stand_parameters = page.get_by_role("button", name="Параметры стенда")
        # self.open_tab_statistics = page.get_by_role("button", name="Статистика")

        #  Вкладка "Параметры стенда"
        # Проверка полей
        self.page_title = page.get_by_role("heading", name="Параметры стенда")
 

        self.free_period_input = page.locator("div").filter(has_text=re.compile(r"^Бесплатный период \(в днях\)")).locator("input[inputmode='numeric']").first
        self.block_period_input = page.locator("div").filter(has_text=re.compile(r"^Период блокировки \(в днях\)")).locator("input[inputmode='numeric']").last

    #     # Кнопки увеличения/уменьшения (исходя из сгенерированного кода локаторов Playwright: `.MuiGrid-root > button:nth-child(2)`)
    #     # Чтобы точно попасть в нужные кнопки для "Бесплатного периода" (это первая группа кнопок на форме)
        self.free_period_increment_btn = page.locator(".MuiGrid-root > button:nth-child(2)").first
        self.free_period_decrement_btn = page.locator(".MuiGrid-root > button:nth-child(1)").first

        # Для периода блокировки
        self.block_period_increment_btn = page.locator(".MuiGrid-root > button:nth-child(2)").last
        self.block_period_decrement_btn = page.locator(".MuiGrid-root > button:nth-child(1)").last

        self.save_btn = page.get_by_role("button", name="Сохранить")
        self.cancel_btn = page.get_by_role("button", name="Отмена")

        # Алерт и крестик
        self.success_alert = page.get_by_role("heading", name="Периоды стенда обновлены")
        self.close_alert_btn = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-outlined").first

    def increment_free_period(self, times: int = 1):
        for _ in range(times):
            self.free_period_increment_btn.click()

    def decrement_free_period(self, times: int = 1):
        for _ in range(times):
            self.free_period_decrement_btn.click()

    def increment_block_period(self, times: int = 1):
        for _ in range(times):
            self.block_period_increment_btn.click()

    def decrement_block_period(self, times: int = 1):
        for _ in range(times):
            self.block_period_decrement_btn.click()

    # def save_changes(self):
    #     # Убедимся, что попап не мешает.
    #     if self.success_alert.is_visible():
    #         self.close_alert_btn.click()
    #         expect(self.success_alert).not_to_be_visible()

    #     # В MUI кнопка "Сохранить" может быть отключена или не видна, если значение инпута не было зафиксировано.
    #     # Просто кликнем в пустую область (body), чтобы сбросить фокус
    #     self.page.locator("body").click()

    #     # Находим кнопку Сохранить. Используем or_ для объединения локаторов
    #     save_btn = self.page.locator("button:has-text('Сохранить')").or_(
    #         self.page.get_by_role("button", name="Сохранить")
    #     ).first

    #     expect(save_btn).to_be_visible(timeout=5000)
    #     expect(save_btn).to_be_enabled(timeout=5000)
    #     save_btn.click()

    #     # Дадим немного времени API на ответ, алерт может появиться не сразу
    #     self.page.wait_for_timeout(500)
    #     expect(self.success_alert).to_be_visible

    #     # Закрываем алерт. При втором проходе алерт может мешать.
    #     if self.success_alert.is_visible():
    #         self.close_alert_btn.click()
    #         expect(self.success_alert).not_to_be_visible

    # def verify_all_informational_fields(self, expected: dict):
    #     # Проверяем, что заголовок страницы на месте
    #     expect(self.page_title).to_be_visible()
        
    #     # 2. Проверка заполненных значений внутри инпутов (полей ввода)
    #     # Поскольку тест на обновление меняет эти значения, мы не можем строго проверять их
    #     # на точное совпадение с начальными, если только не сбрасываем их гарантированно.
    #     # Поэтому просто проверим, что они отображаются (имеют какие-то значения).
    #     expect(self.free_period_input).to_be_visible()
    #     expect(self.block_period_input).to_be_visible()
