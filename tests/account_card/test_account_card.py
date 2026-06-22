import allure
from pages.account_card.account_card_page import AccountCardPage


@allure.feature("Стенды")
@allure.story("Просмотр параметров")
@allure.title("Проверка соответствия информационных полей в карточке стенда")
def test_account_card(account_card_page: AccountCardPage):
    # Тестовые данные на основе карточки "test-1"
    expected_stand_data = {
        "name": "test-1",
        "created_date": "19.06.2026 14:20",
        "users_count": 1,
        "cluster": "production",
        "status": "Создание",
        "charge_per_day": 630,
        "free_period": 30,
        "available_until": "19.07.2026",
        "block_period": 14
    }
    
    # Шаг 1: Если info_stand — это метод клика/перехода на вкладку параметров, 
    # оборачиваем его в шаг Allure:
    with allure.step("Перейти в параметры стенда"):
        account_card_page.info_stand()  # Вызываем как метод (со скобками)
    
    # Шаг 2: Проверяем поля прямо через объект фикстуры account_card_page
    with allure.step("Убедиться, что карточка параметров загрузилась и все поля верны"):
        account_card_page.verify_all_informational_fields(expected_stand_data)