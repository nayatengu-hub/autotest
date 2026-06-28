import allure
from pages.account_card.account_card_page import AccountCardPage


@allure.feature("Стенды")
@allure.story("Просмотр параметров")
@allure.title("Проверка соответствия информационных полей в карточке стенда")
def test_account_card(account_card_page: AccountCardPage):
    # Тестовые данные на основе карточки "test-1"
    expected_stand_data = {
        "name": "test-1",
        "created_date": "26.06.2026 13:55",  # Обновлено
        "users_count": 1,
        "cluster": "production",
        "status": "Создание",
        "charge_per_day": 630,
        "free_period": 30,
        "available_until": "26.07.2026",     # Обновлено
        "block_period": 15
    }
    
    with allure.step("Переход на страницу аккаунта"):
        account_card_page.navigate()
        account_card_page.info_stand.dott.click()
        account_card_page.info_stand.card_card.click()
    
    # Шаг 2: Проверяем поля прямо через объект фикстуры account_card_page
    with allure.step("Убедиться, что карточка параметров загрузилась и все поля верны"):
        account_card_page.info_stand.verify_all_informational_fields(expected_stand_data)