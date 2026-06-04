import allure
from playwright.sync_api import Page
from pages.home.home_page import HomePage


@allure.feature("Главная страница")
@allure.story("Отображение элементов главной страницы")
@allure.title("Проверка элементов на главной странице администратора")
def test_home(auth_admin_page):
    home_page = HomePage(auth_admin_page)
    with allure.step("Переход на главную страницу"):
        home_page.navigate()
    with allure.step("Проверка элементов блока метрик"):
        home_page.block_metrics.ckeck_block_elements()
    with allure.step("Проверка элементов таблицы аккаунтов"):
        home_page.table_accounts.table_elements()
    with allure.step("Переключение вкладок в заголовке"):
        home_page.page_header_admin.switch_to_tab()
    with allure.step("Проверка элементов макета страницы"):
        home_page.page_layout.checking_elements()
    with allure.step("Переход в настройки профиля"):
        home_page.set_profile.go_to_settings(fullname='Ошибка Суперадмин')