from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Config(BaseSettings):
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    ADMIN_ID: str = os.getenv("ADMIN_ID")

config = Config()