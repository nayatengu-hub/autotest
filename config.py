import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "dev").lower()

if ENV == "prod":
    base_url = os.getenv("BASE_URL")
    username = os.getenv("APP_USERNAME")
    password = os.getenv("PASSWORD")
    admin_username = os.getenv("ADMIN_USERNAME_PROD")
    admin_password = os.getenv("ADMIN_PASSWORD_PROD")

elif ENV == "dev":
    base_url = os.getenv("DEV_URL")
    username = os.getenv("APP_USERNAME")
    password = os.getenv("PASSWORD")

    admin_username = os.getenv("ADMIN_USERNAME_DEV")
    admin_password = os.getenv("ADMIN_PASSWORD_DEV")

else:
    raise ValueError(f"Неизвестный стенд: {ENV}. Выберите 'dev' или 'prod'.")
