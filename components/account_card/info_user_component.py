from typing import Optional
from playwright.sync_api import Page, Locator, expect
from components.base_component import BaseComponent


class InfoUser(BaseComponent):
   def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page

        # Данные пользователя (верхняя панель)
        self.user_name = page.locator("h2") 
        self.balance = page.get_by_text("Текущий баланс, RUB")
        self.active_stands = page.get_by_text("Активно стендов")
        self.daily_charge = page.get_by_text("Списание в сутки, RUB")
        self.days_left = page.get_by_role("paragraph").filter(has_text="Осталось дней")
        self.payer = page.get_by_text("Плательщик:")
