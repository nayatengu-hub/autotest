from playwright.sync_api import Page
from pages.base_page import BasePage
from components.account_card.info_stand import InfoStand
from components.account_card.statistics_tab import StatisticsTab


class AccountCardPage(BasePage):
    path = "/accounts/6b122b3f-a0cd-4a5e-94cd-07ba842323e4/stands"

    def __init__(self, page: Page):
        super().__init__(page)
        self.info_stand = InfoStand(page)
        self.statistics_tab = StatisticsTab(page)

        