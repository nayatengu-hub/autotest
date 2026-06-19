# Рекомендации по добавлению API фикстур в Playwright (Python)

Учитывая, что ваши автотесты должны быть изолированными, и у вас уже есть готовая архитектура Playwright с контекстами браузера, управляющими аутентификацией, лучшим подходом будет использование встроенного в Playwright **`APIRequestContext`**.

## Почему стоит использовать `APIRequestContext` из Playwright?

1. **Общее состояние аутентификации**: API контекст Playwright может использовать то же самое состояние (`storage_state` — cookies, local storage), что и ваши UI тесты. Это означает, что ваши API вызовы могут переиспользовать состояния аутентификации, которые вы уже создаете в `conftest.py` (например, `auth_user_state` и `auth_admin_state`), без необходимости повторной аутентификации или отдельного управления токенами.
2. **Изоляция**: Вы можете создавать отдельные API контексты для разных тестов, обеспечивая чистую изоляцию между запусками тестов.
3. **Отсутствие внешних зависимостей**: Вы избегаете добавления лишних библиотек, таких как `requests` или `httpx`, сохраняя ваш стек единым.
4. **Установка (Setup) и очистка (Teardown)**: Фикстуры Pytest с использованием `yield` идеально подходят для создания данных перед тестом и их последующего удаления.

## Рекомендуемая структура и реализация

Ниже приведен рекомендуемый подход для добавления API фикстур в ваш проект.

### 1. Создание API клиента или базового класса API
Создайте класс-обертку для API клиента, чтобы хранить общую логику API (например, базовые URL и заголовки). Вы можете разместить его в новой директории `api/` или внутри `fixtures/`.

```python
# api/client.py
from playwright.sync_api import APIRequestContext

class ApiClient:
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context

    def create_item(self, name: str, description: str):
        response = self.request.post(
            "/api/items",
            data={"name": name, "description": description}
        )
        assert response.ok, f"Не удалось создать элемент: {response.text()}"
        return response.json()

    def delete_item(self, item_id: str):
        response = self.request.delete(f"/api/items/{item_id}")
        assert response.ok, f"Не удалось удалить элемент: {response.text()}"
```

### 2. Определение API фикстур в `conftest.py` или `fixtures/api.py`

Вы можете использовать встроенную фикстуру Playwright `playwright`, чтобы создать изолированный `APIRequestContext`, который будет наполнен вашим существующим состоянием сессии.

```python
# fixtures/api.py или conftest.py
import pytest
from playwright.sync_api import Playwright
from api.client import ApiClient
import config

@pytest.fixture(scope="function")
def user_api_client(playwright: Playwright, auth_user_state: str) -> ApiClient:
    """
    Создает API клиент, аутентифицированный как обычный пользователь,
    используя сохраненное состояние из conftest.py.
    """
    # Создаем API контекст с базовым URL и состоянием хранилища пользователя
    api_request_context = playwright.request.new_context(
        base_url=config.base_url,
        storage_state=auth_user_state
    )

    # Инициализируем вашу обертку API
    client = ApiClient(api_request_context)

    yield client

    # Очищаем контекст после завершения теста
    api_request_context.dispose()

@pytest.fixture(scope="function")
def admin_api_client(playwright: Playwright, auth_admin_state: str) -> ApiClient:
    """
    Создает API клиент, аутентифицированный как администратор.
    """
    api_request_context = playwright.request.new_context(
        base_url=config.base_url,
        storage_state=auth_admin_state
    )

    client = ApiClient(api_request_context)
    yield client
    api_request_context.dispose()
```

### 3. Создание фикстур для подготовки и очистки данных (Setup/Teardown)

Теперь вы можете использовать ваши фикстуры `api_client` для создания специфичных фикстур подготовки/очистки данных для ваших тестов. Эти фикстуры создают данные до `yield` в тесте и удаляют их после.

```python
# fixtures/data.py или в conftest.py
import pytest

@pytest.fixture(scope="function")
def test_item(user_api_client):
    """
    Фикстура для создания элемента для тестирования и его удаления после завершения теста.
    """
    # 1. SETUP: Создание предварительных данных через API
    item_data = user_api_client.create_item(
        name="Тестовый элемент",
        description="Создан через API фикстуру"
    )

    # 2. YIELD: Передача созданных данных в тест
    yield item_data

    # 3. TEARDOWN: Очистка данных через API
    user_api_client.delete_item(item_data["id"])
```

### 4. Использование в тестах

Теперь в ваших тестах вы можете легко комбинировать страницы UI и тестовые данные, сгенерированные через API. Сам тест остается чистым и сфокусированным исключительно на проверке пользовательского интерфейса (UI), в то время как управление данными происходит быстро и надежно за кулисами.

```python
# tests/test_items.py
import allure

@allure.feature("Элементы")
@allure.story("Просмотр элементов")
@allure.title("Проверка отображения созданного элемента")
def test_item_is_visible(account_page, test_item):
    """
    Фикстура 'test_item' автоматически создает элемент через API перед запуском теста,
    и очищает его после.
    """
    with allure.step("Перейти в раздел аккаунта"):
        # account_page уже аутентифицирован
        account_page.navigate()

    with allure.step("Проверить, что тестовый элемент отображается"):
        # Мы можем использовать данные, возвращенные API фикстурой (test_item),
        # чтобы проверить их в UI.
        item_name = test_item["name"]
        account_page.verify_item_visible(item_name)
```

## Краткий обзор преимуществ данного подхода:
- **Скорость**: API вызовы выполняются намного быстрее, чем создание данных через UI.
- **Надежность**: Отделяет нестабильность UI тестов от процесса подготовки тестовых данных.
- **Поддерживаемость**: Сохраняет ваши тесты чистыми; логика абстрагирована в API клиентах и фикстурах Pytest.
- **Интеграция**: Использует уже созданную вами структуру `config.base_url` и `storage_state`.