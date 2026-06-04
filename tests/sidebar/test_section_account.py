import allure
from playwright.sync_api import Page
from pages.sidebar.section_account_page import SectionAccountsPage

@allure.feature("Боковая панель")
@allure.story("Раздел аккаунтов")
@allure.title("Проверка перехода в раздел аккаунтов через боковую панель")
def test_sidebar_page(auth_admin_page):
        sidebar_page = SectionAccountsPage(auth_admin_page)
        with allure.step("Переход на страницу с боковой панелью"):
                sidebar_page.navigate()
        with allure.step("Взаимодействие с разделом аккаунтов в боковой панели"):
                sidebar_page.section_accounts.section_accounts()