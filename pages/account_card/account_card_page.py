from playwright.sync_api import Page
from pages.base_page import BasePage
from components.account_card.info_stand_component import InfoStand
from components.account_card.statistics_tab_component import StatisticsTab
from components.account_card.info_user_component import InfoUser


class AccountCardPage(BasePage):
    path = "/accounts/6b122b3f-a0cd-4a5e-94cd-07ba842323e4/stands"

    def __init__(self, page: Page):
        super().__init__(page)
        self.info_stand = InfoStand(page)


        