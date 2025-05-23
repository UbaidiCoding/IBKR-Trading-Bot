import asyncio
from core.engine import TradingEngine
from brokers.ibkr.client import IBKRClient
from interfaces.telegram.bot import TelegramBot
from interfaces.webhooks.server import WebhookServer
from services.config import get_settings
from services.logger import setup_logging

async def main():
    setup_logging()
    settings = get_settings()
    
    # Initialize components
    broker = IBKRClient(
        host=settings.ibkr_host,
        port=settings.ibkr_port,
        client_id=settings.ibkr_client_id
    )
    
    engine = TradingEngine()
    await engine.initialize(broker)
    
    telegram_bot = TelegramBot(engine, settings)
    webhook_server = WebhookServer(engine)
    
    # Start services
    await asyncio.gather(
        telegram_bot.start(),
        webhook_server.start(),
        engine.monitor()
    )

if __name__ == "__main__":
    asyncio.run(main())