from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")
username = os.getenv("APP_USERNAME")
password = os.getenv("PASSWORD")


print(username)