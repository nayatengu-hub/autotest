import allure
from playwright.sync_api import expect
from pages.profile.account_page import AccountPage

@allure.feature("Профиль пользователя")
@allure.story("Настройки аккаунта")
@allure.title("Проверка вкладок на странице настроек аккаунта")
def test_account_page(account_page: AccountPage):
    with allure.step("Переход на страницу настроек аккаунта"):
        account_page.navigate()
    with allure.step("Проверка вкладки 'Детали аккаунта': Успешное обновление имени"):
        account_page.account_details.update_name_success()
    with allure.step("Проверка вкладки 'Детали аккаунта': Ошибка при обновлении имени"):
        account_page.account_details.update_name_with_error()
    with allure.step("Проверка вкладки 'Детали аккаунта': Успешная загрузка аватара"):
        account_page.account_details.upload_avatar_success()
    with allure.step("Проверка вкладки 'Детали аккаунта': Ошибка при загрузке аватара (не выбран)"):
        account_page.account_details.upload_avatar_missing_error()

    with allure.step("Проверка вкладки 'Безопасность'"):
        account_page.tab_security.tab_security()
    with allure.step("Проверка вкладки 'Пользователи и роли'"):
        account_page.tab_users_roles.tab_users_roles()
    

