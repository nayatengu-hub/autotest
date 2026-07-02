from playwright.sync_api import Page
import allure
from pages.base_page import BasePage
from components.notifications.notifications_component import SectionNotifications

class NotificationsPage(BasePage):
    path = "/notifications/received"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.notifications = SectionNotifications(page)

    @allure.step("Перейти на страницу уведомлений")
    def navigate(self):
        super().navigate()
        # self.page.wait_for_load_state("networkidle")
        # Ensure we are on the page by checking title or tabs
        self.notifications.page_title_notifications.wait_for(state="visible")
