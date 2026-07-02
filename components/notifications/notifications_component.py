from playwright.sync_api import Page, Locator
from typing import Optional
from components.base_component import BaseComponent
from playwright.sync_api import expect


class SectionNotifications(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page 

        # Sidebar
        self.sidebar_notifications = page.get_by_role('button', name='Уведомления')

        # Заголовок страницы и действия
        self.page_title_notifications = page.get_by_role('heading', name='Уведомления', level=1)
        self.button_send_notifications = page.get_by_test_id("iconButton").first
        self.dott_menu = page.get_by_test_id("menuViaDots.trigger").first
        self.button_read_all = page.get_by_test_id("menuViaDots.menu.item-0")
        self.button_cancel = page.get_by_role("button", name="Отменить")
        self.button_read = page.get_by_role("button", name="Прочитать")

        # Вкладки
        self.tab_my_notifications = page.get_by_test_id("tabList.tab-mui-p-_r_7j_-Tab-/notifications/received")
        self.tab_sent_notifications = page.get_by_test_id("tabList.tab-mui-p-_r_7j_-Tab-/notifications/sent")

        # Вкладка 'Мои'
        # Таблица данных
        self.column_header_no = page.get_by_role("heading", name="п/п")
        self.column_header_header = page.get_by_role("heading", name="Заголовок")
        self.column_header_notification_type = page.get_by_role("heading", name="Тип уведомления") 
        self.column_header_date = page.get_by_role("heading", name="Дата")
        self.column_header_text = page.get_by_role("heading", name="Текст") 
        self.column_header_actions = page.get_by_role("row", name="1 Новый стенд Системное 30.06").get_by_test_id("menuViaDots.trigger")
        self.dott_menu_read = page.get_by_test_id("menuViaDots.menu.item-0")
        self.dott_menu_delete = page.get_by_test_id("menuViaDots.menu.item-1")

        # Модальное окно уведомления
        self.modal_window_title = page.get_by_role("heading", name="Новый стенд")
        self.notification_type = page.get_by_text("Тип уведомления:")
        self.date = page.get_by_text("Дата:")
        self.text = page.get_by_text("Текст:")
        self.button_x = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-outlined.MuiButton-outlinedSecondary.MuiButton-sizeMedium.MuiButton-outlinedSizeMedium.MuiButton-colorSecondary.MuiButton-disableElevation.bp-1pjj1z7")
        self.button_close = page.get_by_test_id("modalFooter").get_by_test_id("button")

        # Botton bar удалить уведомление
        self.button_delete = page.get_by_role("button", name="Удалить")

        # Вкладка 'Отправленные'
        # Доп. меню
        self.dott_menu_repeat = self.get_by_test_id("menuViaDots.menu.item-1")

        # Модальное окно уведомления "прочитанные"
        self.recipients = page.get_by_text("Получатели:")

        # Добавление уведомления
        self.page_title = page.get_by_role("heading", name="Добавление уведомления")
        self.window_title = page.get_by_role("heading", name="Основная информация")
        self.field_title = page.locator("[id=\"_r_ku_-label\"]").get_by_text("Заголовок *")
        self.field_description = page.get_by_text("Описание *")
        self.field_select_recipient = page.get_by_text("Получатель *Выберите из спискаChip")
        self.field_category_notification = page.get_by_text("Категория уведомления *")

        # Select menu 'Категория уведомления'
        self.select_menu = page.get_by_test_id("select")
        self.select_menu_system = page.get_by_role("option", name="Системное")
        self.select_menu_finance = page.get_by_role("option", name="Финансы")
        self.select_menu_documents = page.get_by_role("option", name="Документы")
        self.select_menu_announcements = page.get_by_role("option", name="Объявления")

         # Botton bar отправить уведомление
        self.button_send = page.get_by_role("button", name="Отправить")














        



        


        


        
