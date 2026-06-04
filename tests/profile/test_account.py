import allure
from playwright.sync_api import expect
from pages.profile.account_page import AccountPage

@allure.feature("Профиль пользователя")
@allure.story("Настройки аккаунта")
@allure.title("Проверка вкладок на странице настроек аккаунта")
def test_account_page(auth_user_page):
    account_page = AccountPage(auth_user_page)
    with allure.step("Переход на страницу настроек аккаунта"):
        account_page.navigate()
    with allure.step("Проверка вкладки 'Детали аккаунта'"):
        account_page.account_details.tab_account_details()
    with allure.step("Проверка вкладки 'Безопасность'"):
        account_page.tab_security.tab_security()
    with allure.step("Проверка вкладки 'Пользователи и роли'"):
        account_page.tab_users_roles.tab_users_roles()
    
    with allure.step("Ожидание загрузки страницы аккаунта"):
        auth_user_page.wait_for_url("**/account")
