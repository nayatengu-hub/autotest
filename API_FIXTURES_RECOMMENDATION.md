# Recommendations for Adding API Fixtures in Playwright (Python)

Given that your automated tests will be isolated and you already have an established Playwright architecture with browser contexts managing authentication, the best approach is to use Playwright's built-in **`APIRequestContext`**.

## Why use Playwright's `APIRequestContext`?

1. **Shared Authentication State**: Playwright's API context can share the same `storage_state` (cookies, local storage) as your UI tests. This means your API calls can reuse the authentication states you already create in `conftest.py` (like `auth_user_state` and `auth_admin_state`), without needing to re-authenticate or manage tokens separately.
2. **Isolation**: You can create separate API contexts for different test scopes, ensuring clean isolation between test runs.
3. **No External Dependencies**: You avoid adding extra libraries like `requests` or `httpx`, keeping your stack unified.
4. **Setup & Teardown**: Pytest fixtures using `yield` are perfect for creating data before the test and cleaning it up after.

## Recommended Structure & Implementation

Here is a recommended approach for adding API fixtures to your project.

### 1. Create an API Client or API Base Class
Create an API client wrapper to hold common API logic (like base URLs and headers). You could place this in a new directory `api/` or within `fixtures/`.

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
        assert response.ok, f"Failed to create item: {response.text()}"
        return response.json()

    def delete_item(self, item_id: str):
        response = self.request.delete(f"/api/items/{item_id}")
        assert response.ok, f"Failed to delete item: {response.text()}"
```

### 2. Define API Fixtures in `conftest.py` or `fixtures/api.py`

You can use the built-in Playwright `playwright` fixture to create an isolated `APIRequestContext` that is hydrated with your existing session state.

```python
# fixtures/api.py or conftest.py
import pytest
from playwright.sync_api import Playwright
from api.client import ApiClient
import config

@pytest.fixture(scope="function")
def user_api_client(playwright: Playwright, auth_user_state: str) -> ApiClient:
    """
    Creates an API client authenticated as a regular user,
    using the storage state saved in conftest.py.
    """
    # Create an API context with the base_url and the user's storage state
    api_request_context = playwright.request.new_context(
        base_url=config.base_url,
        storage_state=auth_user_state
    )

    # Initialize your API wrapper
    client = ApiClient(api_request_context)

    yield client

    # Clean up the context after the test
    api_request_context.dispose()

@pytest.fixture(scope="function")
def admin_api_client(playwright: Playwright, auth_admin_state: str) -> ApiClient:
    """
    Creates an API client authenticated as an admin.
    """
    api_request_context = playwright.request.new_context(
        base_url=config.base_url,
        storage_state=auth_admin_state
    )

    client = ApiClient(api_request_context)
    yield client
    api_request_context.dispose()
```

### 3. Create Setup/Teardown Data Fixtures

Now, you can use your `api_client` fixtures to build specific setup/teardown fixtures for your tests. These fixtures create the data before the test yields, and delete it afterward.

```python
# fixtures/data.py or in conftest.py
import pytest

@pytest.fixture(scope="function")
def test_item(user_api_client):
    """
    Fixture to create an item for testing, and delete it after the test finishes.
    """
    # 1. SETUP: Create the pre-condition data via API
    item_data = user_api_client.create_item(
        name="Test Item",
        description="Created via API fixture"
    )

    # 2. YIELD: Pass the created data to the test
    yield item_data

    # 3. TEARDOWN: Clean up the data via API
    user_api_client.delete_item(item_data["id"])
```

### 4. Use in Tests

In your tests, you can now seamlessly combine the UI pages and the API-generated test data. The test itself remains clean and focused solely on UI verification, while the data management happens quickly and reliably behind the scenes.

```python
# tests/test_items.py
import allure

@allure.feature("Items")
@allure.story("View Items")
@allure.title("Проверка отображения созданного элемента")
def test_item_is_visible(account_page, test_item):
    """
    The 'test_item' fixture automatically creates the item via API before this runs,
    and cleans it up afterward.
    """
    with allure.step("Перейти в раздел аккаунта"):
        # account_page is already authenticated
        account_page.navigate()

    with allure.step("Проверить, что тестовый элемент отображается"):
        # We can use the data returned by the API fixture (test_item)
        # to verify it in the UI.
        item_name = test_item["name"]
        account_page.verify_item_visible(item_name)
```

## Summary of Benefits for this Approach:
- **Speed**: API calls are much faster than setting up data via the UI.
- **Reliability**: Decouples UI test flakiness from test data setup.
- **Maintainability**: Keeps your tests clean; logic is abstracted away in API clients and Pytest fixtures.
- **Integration**: Leverages the existing `config.base_url` and `storage_state` structure you have already built.
