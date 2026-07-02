from playwright.sync_api import APIRequestContext

class ApiClient:
    """
    Базовый класс-обертка для API клиента с использованием Playwright APIRequestContext.
    """
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context

    def send_notification(self, payload: dict):
        """Отправка уведомления"""
        response = self.request.post("/control/api/v1/notifications/sent", data=payload)
        assert response.ok, f"Ошибка при отправке уведомления: {response.text()}"
        return response.json()

    def get_received_notifications(self, page: int = 1, size: int = 20):
        """Получение списка полученных уведомлений"""
        response = self.request.get(f"/control/api/v1/notifications/received?page={page}&size={size}")
        assert response.ok, f"Ошибка при получении уведомлений: {response.text()}"
        return response.json()

    def get_sent_notifications(self, page: int = 1, size: int = 20):
        """Получение списка отправленных уведомлений"""
        response = self.request.get(f"/control/api/v1/notifications/sent?page={page}&size={size}")
        assert response.ok, f"Ошибка при получении отправленных уведомлений: {response.text()}"
        return response.json()
