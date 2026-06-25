pytest_plugins = [
    "fixtures.pages",
    "fixtures.api",
]
import pytest
import os
from pages.auth.login_page import LoginPage
import config  # Импортируем весь модуль конфига
from playwright.sync_api import Playwright, APIRequestContext
from pages.account_card.account_card_page import AccountCardPage




@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "extra_http_headers": {"Accept-Language": "ru-RU,ru;q=0.9"},
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "args": ["--disable-blink-features=AutomationControlled"],
    }

@pytest.fixture(scope="session")
def auth_user_state(playwright: Playwright):
    # Авторизация пользователя через API (Обход UI-капчи)
    request_context = playwright.request.new_context()
    response = request_context.post(
        f"{config.api_url}/control/api/v1/auth/login",
        data={
            "identity": config.username,
            "password": config.password
        }
    )
    assert response.ok, f"Ошибка авторизации пользователя через API: {response.text()}"
    
    state_path = "data/auth_state.json"
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    request_context.storage_state(path=state_path)
    request_context.dispose()

    return state_path

@pytest.fixture(scope="function")
def auth_user_page(browser, auth_user_state):
    # Передаем base_url и для тестов
    context = browser.new_context(
        storage_state=auth_user_state, 
        base_url=config.base_url
    )
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def guest_page(browser):
    # Гостевая страница тоже должна знать, на каком мы стенде
    context = browser.new_context(base_url=config.base_url, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", extra_http_headers={"Accept-Language": "ru-RU,ru;q=0.9"})
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def auth_admin_state(playwright: Playwright):
    # Авторизация администратора через API (Обход UI-капчи)
    request_context = playwright.request.new_context()
    response = request_context.post(
        f"{config.api_url}/control/api/v1/auth/login",
        data={
            "identity": config.admin_username,
            "password": config.admin_password
        }
    )
    assert response.ok, f"Ошибка авторизации администратора через API: {response.text()}"
    
    state_path = "data/auth_admin_state.json"
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    request_context.storage_state(path=state_path)
    request_context.dispose()

    return state_path

@pytest.fixture(scope="function")
def auth_admin_page(browser, auth_admin_state):
    context = browser.new_context(
        storage_state=auth_admin_state,
        base_url=config.base_url
    )
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def account_card_page(auth_admin_page):
    """Фикстура для инициализации карточки аккаунта"""
    return AccountCardPage(auth_admin_page)

    