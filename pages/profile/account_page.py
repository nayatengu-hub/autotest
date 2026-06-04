from playwright.sync_api import Page
from pages.base_page import BasePage
from components.profile.tab_account_details import AccountDetails
from components.profile.tab_security import TabSecurity
from components.profile.tab_users_and_roles import UsersRoles


class AccountPage(BasePage):
    path = "/account"

    def __init__(self, page: Page):
        super().__init__(page)
        self.account_details = AccountDetails(page)
        self.tab_security = TabSecurity(page)
        self.tab_users_roles = UsersRoles(page)

    
