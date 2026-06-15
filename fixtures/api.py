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
    api_request_context = playwright.request.new_context(
        base_url=config.base_url,
        storage_state=auth_user_state
    )

    client = ApiClient(api_request_context)
    yield client
    api_request_context.dispose()

@pytest.fixture(scope="function")
def admin_api_client(playwright: Playwright, auth_admin_state: str) -> ApiClient:
    """
    Создает API клиент, аутентифицированный как администратор,
    используя сохраненное состояние из conftest.py.
    """
    api_request_context = playwright.request.new_context(
        base_url=config.base_url,
        storage_state=auth_admin_state
    )

    client = ApiClient(api_request_context)
    yield client
    api_request_context.dispose()
