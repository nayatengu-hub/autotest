import allure
from pages.auth.login_page import LoginPage
import config
from playwright.sync_api import expect

import pytest

@allure.feature("Авторизация")
@allure.story("Вход в систему")
@allure.title("Успешная авторизация пользователя")
def test_login(login_page: LoginPage):
    with allure.step("Переход на страницу авторизации"):
        login_page.navigate() # Перейдет на /auth/login текущего стенда (благодаря base_url)
    with allure.step("Ввод учетных данных и вход"):
        login_page.login_form.login(username=config.username, password=config.password)
    
    with allure.step("Ожидание перехода на домашнюю страницу"):
        login_page.page.wait_for_url("**/home/accounts")