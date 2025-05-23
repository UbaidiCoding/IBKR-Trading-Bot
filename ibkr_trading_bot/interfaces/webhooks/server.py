from fastapi import FastAPI
from core.engine import TradingEngine
from .routes import router
import logging

class WebhookServer:
    def __init__(self, engine: TradingEngine):
        self.app = FastAPI()
        self.engine = engine
        self.logger = logging.getLogger(__name__)
        self._setup_routes()

    def _setup_routes(self):
        self.app.include_router(router)

    async def start(self, host: str = "0.0.0.0", port: int = 8080):
        import uvicorn
        config = uvicorn.Config(
            self.app,
            host=host,
            port=port,
            log_level="info"
        )
        server = uvicorn.Server(config)
        await server.serve()