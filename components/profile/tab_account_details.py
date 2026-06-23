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
        self.edit_name = page.get_by_role('textbox').first
        self.cancel_button = page.get_by_role('button', name='Отмена')
        
        # Динамический путь к файлу
        self.project_root = Path(__file__).resolve().parents[2]
        self.avatar_file_path = str(self.project_root / "data" / "avatar.jpg")
        
        # Элементы работы с аватаром
        self.delete_avatar = page.locator(".MuiButtonBase-root.MuiIconButton-root")
        self.confirm_deletion = page.get_by_role("button", name="Удалить")
        self.select_avatar = page.get_by_role("main").get_by_test_id("avatar")
        
        # --- ЛОКАТОРЫ ДЛЯ АЛЕРТОВ ---
        self.alert_missing_avatar = page.get_by_text("Выберите аватар для сохранения", exact=True)
        self.alert_invalid_name = page.get_by_text("Имя может содержать только кириллицу, пробелы и дефисы", exact=True)
        self.alert_profile_updated = page.get_by_text("Профиль успешно обновлён", exact=True)
        self.alert_avatar_changed = page.get_by_text("Аватар успешно изменён", exact=True)
        
        # Кнопка закрытия алерта 
        self.close_alert_button = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-colorPrimary.MuiButton-disableElevation.bp-1dgbx2w")
        
        # Длинный класс кнопки подтверждения
        self.confirm_button = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorPrimary.MuiButton-disableElevation.bp-18dguzg")

        # Кнопка подтверждения сохранения аватара
        self.confirm_button_avatar = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorPrimary.MuiButton-disableElevation.bp-18dguzg")
    
    # --- Вспомогательный метод для закрытия алертов ---
    def close_alert(self, alert_locator: Locator):
        """Кликает по кнопке закрытия алерта и ждет его полного исчезновения"""
        self.close_alert_button.click()
        # Обязательно ждем, пока алерт скроется, чтобы он не перекрывал другие элементы
        expect(alert_locator).to_be_hidden(timeout=5000)

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
        # Закрываем алерт после появления
        self.close_alert(self.alert_profile_updated)
        
        # Возвращаем имя обратно
        self.edit_name.focus()
        self.page.keyboard.press('Control+A')
        self.page.keyboard.press('Backspace')
        self.edit_name.type('Анастасия', delay=10)

        self.page.locator('body').click()
        self.save_button.wait_for(state="visible")
        self.save_button.click(force=True)

        expect(self.alert_profile_updated).to_be_visible(timeout=10000)
        # Снова закрываем алерт, чтобы оставить страницу чистой
        self.close_alert(self.alert_profile_updated)

    def update_name_with_error(self, invalid_name: str = 'Latin'):
        """Изменение имени с ошибкой валидации"""
        self.page.reload()
        self.edit_name.wait_for(state="visible")

        self.edit_name.focus()
        self.page.keyboard.press('Control+A')
        self.page.keyboard.press('Backspace')
        self.edit_name.type(invalid_name, delay=10)

        self.page.locator('body').click()
        self.save_button.wait_for(state="visible")
        self.save_button.click(force=True)

        expect(self.alert_invalid_name).to_be_visible(timeout=10000)
        
        # Если алерт с ошибкой тоже имеет кнопку закрытия, закрываем его
        if self.close_alert_button.is_visible():
            self.close_alert(self.alert_invalid_name)
            
        self.cancel_button.click(force=True)

    def upload_avatar_success(self):
        """Успешная загрузка и сохранение аватара"""
        # Кликаем по области выбора аватара
        self.select_avatar.click()
        
        # Загружаем файл через указанный текстовый элемент
        self.page.locator("input[type='file']").set_input_files(self.avatar_file_path)
        
        # Подтверждаем загрузку
        self.confirm_button_avatar.click()
        
        # Ждем появления алерта об успехе
        # expect(self.alert_avatar_changed).to_be_visible(timeout=60000)
        
        # Обязательно закрываем алерт перед удалением аватара
        self.close_alert(self.alert_avatar_changed)
        
        # Удаление аватара для чистоты тестов
        self.delete_avatar.click()
        self.confirm_deletion.click()

    def upload_avatar_missing_error(self):
        """Негативный тест аватара: попытка сохранить без выбора файла"""
        self.select_avatar.click()
        self.confirm_button.click()
        expect(self.alert_missing_avatar).to_be_visible()