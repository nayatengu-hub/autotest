from pathlib import Path
from typing import Optional
from playwright.sync_api import Page, Locator, expect
from components.base_component import BaseComponent

class AccountDetails(BaseComponent):
    def __init__(self, page: Page, root_locator: Optional[Locator] = None):
        super().__init__(page, root_locator)
        self.page = page 
        
        # --- ОБЪЯВЛЕНИЕ ЛОКАТОРОВ ---
        self.save_button = page.get_by_role('button', name='Сохранить')
        self.edit_name = page.get_by_role('textbox')
        self.cancel_button = page.get_by_role('button', name='Отмена')
        
        # Динамический путь к файлу
        self.project_root = Path(__file__).resolve().parents[2]
        self.avatar_file_path = str(self.project_root / "data" / "avatar.jpg")
        
        # Элементы работы с аватаром
        self.delete_avatar = page.locator(".MuiButtonBase-root.MuiIconButton-root")
        self.confirm_deletion = page.get_by_role("button", name="Удалить")
        self.select_avatar = page.get_by_role("main").get_by_test_id("avatar")
        
        # --- ЛОКАТОРЫ ДЛЯ АЛЕРТОВ (СТРОГО ПО ТЗ) ---
        self.alert_missing_avatar = page.get_by_text("Выберите аватар для сохранения", exact=True)
        self.alert_invalid_name = page.get_by_text("Поле может содержать только кириллицу, пробелы и дефисы", exact=True)
        self.alert_profile_updated = page.get_by_text("Профиль успешно обновлён", exact=True)
        self.alert_avatar_changed = page.get_by_text("Аватар успешно изменён", exact=True)
        
        # Длинный класс кнопки подтверждения
        self.confirm_button = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorPrimary.MuiButton-disableElevation.bp-18dguzg")

    def update_name_success(self, new_name: str = 'Анастасия Тестовая'):
        """Изменение имени с успешным сохранением"""
        self.edit_name.wait_for(state="visible")
        self.edit_name.focus()
        self.page.keyboard.press('Control+A')
        self.page.keyboard.press('Backspace')
        self.edit_name.type(new_name, delay=10)
        
        self.page.locator('body').click()
        self.save_button.wait_for(state="visible")
        self.save_button.click(force=True)
        
        expect(self.alert_profile_updated).to_be_visible(timeout=10000)
        self.page.wait_for_timeout(3000)
        
        # Возвращаем имя обратно
        self.edit_name.focus()
        self.page.keyboard.press('Control+A')
        self.page.keyboard.press('Backspace')
        self.edit_name.type('Анастасия', delay=10)

        self.page.locator('body').click()
        self.save_button.wait_for(state="visible")
        self.save_button.click(force=True)

        expect(self.alert_profile_updated).to_be_visible(timeout=10000)
        self.page.wait_for_timeout(3000)

    def update_name_with_error(self, invalid_name: str = 'Latin'):
        """Изменение имени с ошибкой валидации"""
        # Обновляем страницу перед негативным тестом, чтобы очистить состояние (например, зависшие нотификации)
        self.page.reload()
        self.edit_name.wait_for(state="visible")

        self.edit_name.focus()
        self.page.keyboard.press('Control+A')
        self.page.keyboard.press('Backspace')
        self.edit_name.type(invalid_name, delay=10)

        self.page.locator('body').click()
        self.save_button.wait_for(state="visible")
        self.page.wait_for_timeout(500)
        self.save_button.click(force=True)

        # Ждем немного перед проверкой, чтобы UI обновился
        self.page.wait_for_timeout(1000)
        expect(self.alert_invalid_name).to_be_visible(timeout=10000)
        self.cancel_button.click(force=True)

    def upload_avatar_success(self):
        """Успешная загрузка и сохранение аватара"""
        self.page.locator("input[type='file']").set_input_files(self.avatar_file_path)
        self.page.wait_for_load_state("networkidle")
        expect(self.alert_avatar_changed).to_be_visible()
        
        # Удаление аватара для чистоты тестов
        self.delete_avatar.click()
        self.confirm_deletion.click()
        self.page.wait_for_load_state("networkidle")

    def upload_avatar_missing_error(self):
        """Негативный тест аватара: попытка сохранить без выбора файла"""
        self.select_avatar.click()
        self.confirm_button.click()
        expect(self.alert_missing_avatar).to_be_visible()