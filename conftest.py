import pytest
from pages.login_page import LoginPage
import config  # Импортируем весь модуль конфига

@pytest.fixture(scope="session")
def auth_user_state(browser):
    # Передаем base_url в контекст!
    context = browser.new_context(base_url=config.base_url)
    page = context.new_page()
    
    login_page = LoginPage(page)
    # Если в login_page.navigate() у вас page.goto(self.path), 
    # то благодаря base_url выше, он перейдет на правильный стенд
    login_page.navigate() 
    
    # Берем креды из конфига (они уже соответствуют нужному стенду)
    login_page.login_form.login(username=config.username, password=config.password)
    page.wait_for_url("**/stands")
    
    state_path = "data/auth_state.json"
    context.storage_state(path=state_path)
    context.close()
    return state_path

@pytest.fixture(scope="function")
def auth_user_page(browser, auth_user_state): # Исправлена опечатка в имени фикстуры
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
    context = browser.new_context(base_url=config.base_url)
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def auth_admin_state(browser):
    context = browser.new_context(base_url=config.base_url)
    page = context.new_page()
    
    login_page = LoginPage(page)
    login_page.navigate()
    
    # Используем админские креды из конфига
    login_page.login_form.login(username=config.admin_username, password=config.admin_password)
    
    state_path = "data/auth_admin_state.json"
    context.storage_state(path=state_path)
    context.close()
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