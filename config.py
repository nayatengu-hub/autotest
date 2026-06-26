import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "prod").lower()

if ENV == "prod":
    base_url = os.getenv("BASE_URL")
    api_url = None # Авторизация через API на проде не поддерживается
    username = os.getenv("APP_USERNAME")
    password = os.getenv("PASSWORD")
    admin_username = os.getenv("APP_USERNAME")
    admin_password = os.getenv("PASSWORD")

elif ENV == "dev":
    base_url = os.getenv("DEV_URL")
    api_url = "https://billing-back-test.business-pad.com"
    username = os.getenv("APP_USERNAME")
    password = os.getenv("PASSWORD")

    admin_username = os.getenv("ADMIN_USERNAME_DEV")
    admin_password = os.getenv("ADMIN_PASSWORD_DEV")

else:
    raise ValueError(f"Неизвестный стенд: {ENV}. Выберите 'dev' или 'prod'.")
