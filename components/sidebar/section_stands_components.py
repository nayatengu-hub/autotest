from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent
from playwright.sync_api import expect

class SectionStands(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page
        self.sidebar_stands = page.get_by_role('button', name='Стенды') 
        self.button_add = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-outlined").first
        self.page_title_stands = page.get_by_role('heading', name='Стенды', level=1)
        self.page_heading_stands = page.get_by_role('heading', name='Стенды', level=2) 
        self.column_header_no = page.get_by_role("heading", name="п/п")
        # Исправлен strict mode: находит заголовок колонки
        self.column_header_accounts = page.get_by_test_id("uniTable.header.row").get_by_role("heading", name="Аккаунт")
        self.column_header_name_stands = page.get_by_test_id("uniTable.header.row").get_by_role("heading", name="Название стенда")
        self.column_header_created_date = page.get_by_role("heading", name="Дата создания")
        self.column_header_users = page.get_by_role("heading", name="Пользователей")
        self.column_header_presets = page.get_by_role("heading", name="Пресеты")
        self.column_header_status = page.get_by_role("heading", name="Статус")
        self.column_header_tariff = page.get_by_role("heading", name="Тариф")
        self.column_header_days_left = page.get_by_role("heading", name="Осталось дней")
        self.column_header_charge_per_day = page.get_by_role("heading", name="Списание ₽/сутки")
        self.date_from_input = page.locator(".MuiButtonBase-root.MuiIconButton-root").first
        self.date_to_input = page.locator("div:nth-child(2) > .MuiFormControl-root > .MuiInputBase-root > .MuiInputAdornment-root > .MuiButtonBase-root")
        self.status_dropdown = page.get_by_role("button", name="Все")
        self.sort_dropdown = page.get_by_role("button", name="По умолчанию")
        
        

    def open(self):
        self.sidebar_stands.click()

    def verify_ui_elements(self):
        self.button_add.click()
        self.page_title_stands.is_visible()
        self.page_heading_stands.is_visible()
        self.column_header_no.is_visible()
        self.column_header_accounts.is_visible()
        self.column_header_name_stands.is_visible()
        self.column_header_created_date.is_visible()
        self.column_header_users.is_visible()
        self.column_header_presets.is_visible()
        self.column_header_status.is_visible()
        self.column_header_tariff.is_visible()
        self.column_header_days_left.is_visible()
        self.column_header_charge_per_day.is_visible()
        self.sidebar_stands.click()
        self.date_from_input.click()
        self.date_to_input.click()
        self.status_dropdown.click()
        self.sort_dropdown.click()