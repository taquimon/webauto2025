import os

from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


BASE_URL = {
    "development": "http://demoqa.com",
    "staging": "http://staging.demoqa.com",
    "production": "http://production.demoqa.com"
}