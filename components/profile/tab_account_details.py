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
        
        # --- ПРОВЕРКА ТЕКСТА ПО ТЗ ---
        # Используем get_by_text с точной строкой из ТЗ. Это гарантирует уникальность 
        # и защищает от Strict Mode Violation, игнорируя другие заголовки на странице.
        self.alert_heading = page.get_by_text("Выберите аватар для сохранения")
        
        # Длинный класс кнопки подтверждения (сохраняем как у вас)
        self.confirm_button = page.locator(".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButton-colorPrimary.MuiButton-disableElevation.bp-18dguzg")

    def tab_account_details(self):
        """Метод выполняет последовательность действий на вкладке 'Детали аккаунта'"""
        
        # 1. Изменение имени и сохранение (УБРАЛИ ЦИФРЫ, чтобы пройти валидацию!)
        self.edit_name.fill('Анастасия')
        self.save_button.click()
        
        # 2. Изменение имени и отмена (УБРАЛИ ЦИФРЫ)
        self.edit_name.fill('анастасия')
        self.cancel_button.click()
        
        # 3. ЗАГРУЗКА АВАТАРА
        self.page.locator("input[type='file']").set_input_files(self.avatar_file_path)
        
        # 4. УДАЛЕНИЕ АВАТАРА
        self.delete_avatar.click()
        self.confirm_deletion.click()

        # 5. ПРОВЕРКА АЛЕРТА НА КОРРЕКТНОСТЬ НАПИСАНИЯ ПО ТЗ
        # Если текст на сайте будет отличаться от указанного в self.alert_heading, 
        # элемент не станет видимым, и тест упадет с ошибкой.
        expect(self.alert_heading).to_be_visible()

        # 6. Финальные шаги сценария
        self.select_avatar.click()
        self.confirm_button.click()