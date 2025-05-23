from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # IBKR Settings
    ibkr_host: str = "127.0.0.1"
    ibkr_port: int = 7496
    ibkr_client_id: int = 1
    
    # Telegram
    telegram_token: Optional[str]
    telegram_chat_id: Optional[str]
    
    # Webhook
    webhook_secret: Optional[str]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_settings():
    return Settings()