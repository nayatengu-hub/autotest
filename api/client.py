from playwright.sync_api import APIRequestContext

class ApiClient:
    """
    Базовый класс-обертка для API клиента с использованием Playwright APIRequestContext.
    """
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context

    # Здесь можно добавить общие методы для работы с API,
    # например, методы для создания, чтения, обновления и удаления тестовых данных.

    # Пример:
    # def create_something(self, data: dict):
    #     response = self.request.post("/api/endpoint", data=data)
    #     assert response.ok, f"Ошибка при создании: {response.text()}"
    #     return response.json()
