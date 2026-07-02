import allure
import pytest
from playwright.sync_api import expect
import os

@allure.feature("Уведомления")
@allure.story("Управление уведомлениями администратором")
class TestAdminNotifications:

    @allure.title("Проверка вкладки 'Мои' и действий с уведомлением")
    def test_admin_my_notifications_tab(self, auth_admin_page, test_notification):
        from pages.notifications.notifications_page import NotificationsPage
        page = NotificationsPage(auth_admin_page)

        with allure.step("Перейти в раздел Уведомления"):
            page.navigate()

        with allure.step("Проверить наличие вкладок и таблицы 'Мои'"):
            expect(page.notifications.tab_my_notifications).to_be_visible()
            expect(page.notifications.tab_sent_notifications).to_be_visible()
            expect(page.notifications.tab_my_notifications).to_have_attribute("aria-selected", "true")
            expect(page.notifications.column_header_header).to_be_visible()

        with allure.step("Проверка контекстного меню (dot menu)"):
            first_row = auth_admin_page.locator("tbody tr").first
            dot_trigger = first_row.locator("[data-testid='menuViaDots.trigger']")
            dot_trigger.click()
            auth_admin_page.wait_for_timeout(1000)
            # Find in document body because it might be teleported by MUI Popover
            read_btn = auth_admin_page.locator("body").locator("[role='menuitem']", has_text="Прочитать")
            delete_btn = auth_admin_page.locator("body").locator("[role='menuitem']", has_text="Удалить")
            expect(read_btn).to_be_visible()
            expect(delete_btn).to_be_visible()

        with allure.step("Открыть модальное окно уведомления через 'Прочитать'"):
            read_btn.click()
            # Проверяем, что открылось модальное окно (кнопка закрытия/крестик в футере)
            close_btn = auth_admin_page.get_by_test_id("modalFooter").get_by_test_id("button").first
            expect(close_btn).to_be_visible()
            close_btn.click()
            auth_admin_page.wait_for_timeout(500)

        with allure.step("Проверка удаления уведомления (появление bottom bar)"):
            dot_trigger.click()
            auth_admin_page.wait_for_timeout(1000)
            delete_btn = auth_admin_page.locator("body").locator("[role='menuitem']", has_text="Удалить")
            delete_btn.click()
            expect(page.notifications.bottom_bar_delete_text).to_be_visible()
            expect(page.notifications.button_cancel).to_be_visible()
            page.notifications.button_cancel.click()

    @allure.title("Проверка вкладки 'Отправленные'")
    def test_admin_sent_notifications_tab(self, auth_admin_page):
        from pages.notifications.notifications_page import NotificationsPage
        page = NotificationsPage(auth_admin_page)

        with allure.step("Перейти в раздел Уведомления"):
            page.navigate()

        with allure.step("Переключиться на вкладку 'Отправленные'"):
            page.notifications.tab_sent_notifications.click()
            expect(page.notifications.tab_sent_notifications).to_have_attribute("aria-selected", "true")
            expect(page.notifications.column_header_header).to_be_visible()

    @allure.title("Проверка создания нового уведомления")
    def test_admin_create_notification(self, auth_admin_page):
        from pages.notifications.notifications_page import NotificationsPage
        page = NotificationsPage(auth_admin_page)

        with allure.step("Перейти в раздел Уведомления"):
            page.navigate()

        with allure.step("Найти и нажать кнопку 'Отправить сообщение' (плюс)"):
            page.notifications.button_send_notifications.click()
            auth_admin_page.wait_for_url("**/notifications/add", timeout=5000)
            expect(auth_admin_page.get_by_role("heading", name="Добавление уведомления")).to_be_visible(timeout=10000)

        with allure.step("Выбрать получателей через выпадающий список"):
            recipient_input = auth_admin_page.get_by_test_id("outlinedInput").first
            expect(recipient_input).to_be_visible()
            recipient_input.click()
            auth_admin_page.locator("[role='presentation'] li").nth(7).click()
            auth_admin_page.keyboard.press("Escape")
            auth_admin_page.wait_for_timeout(500)

        with allure.step("Заполнить форму уведомления"):
            expect(page.notifications.select_menu).to_be_visible()
            page.notifications.select_menu.click()
            page.notifications.select_menu_system.click()

            title_input = auth_admin_page.get_by_role("textbox", name="Заголовок")
            if not title_input.is_visible():
                title_input = auth_admin_page.locator("input[name='title']")
            title_input.fill("Тестовое уведомление из автотестов")

            desc_input = auth_admin_page.get_by_role("textbox").nth(1)
            expect(desc_input).to_be_visible()
            desc_input.fill("Текст тестового сообщения с <b>разметкой</b>.")

        with allure.step("Прикрепить файл"):
            file_input = auth_admin_page.locator("input[type='file']").first
            if file_input.is_visible():
                file_path = os.path.abspath("data/avatar.jpg")
                if os.path.exists(file_path):
                    file_input.set_input_files(file_path)

        with allure.step("Проверить кнопку и отменить/отправить"):
            send_btn = auth_admin_page.get_by_role("button", name="Отправить")
            expect(send_btn).to_be_visible()
