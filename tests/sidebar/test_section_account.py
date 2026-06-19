import allure
from playwright.sync_api import Page
from pages.sidebar.section_account_page import SectionPage








@allure.feature("Боковая панель")
@allure.story("Раздел аккаунтов")
@allure.title("Проверка перехода в раздел аккаунтов через боковую панель")
def test_sidebar_page(sidebar_page: SectionPage):
        with allure.step("Переход на страницу с боковой панелью"):
                sidebar_page.navigate()
        with allure.step("Взаимодействие с разделом аккаунтов в боковой панели"):
                sidebar_page.section_accounts.section_accounts()
                sidebar_page.section_stands.open()                 # Открываем вкладку
                sidebar_page.section_stands.verify_ui_elements()



