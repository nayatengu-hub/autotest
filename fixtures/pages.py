import pytest
from pages.auth.login_page import LoginPage
from pages.home.home_page import HomePage
from pages.profile.account_page import AccountPage
from pages.sidebar.section_account_page import SectionPage


@pytest.fixture
def login_page(guest_page) -> LoginPage:
    return LoginPage(guest_page)

@pytest.fixture
def home_page(auth_admin_page) -> HomePage:
    return HomePage(auth_admin_page)

@pytest.fixture
def account_page(auth_user_page) -> AccountPage:
    return AccountPage(auth_user_page)

@pytest.fixture
def sidebar_page(auth_admin_page) -> SectionPage:
    return SectionPage(auth_admin_page)
