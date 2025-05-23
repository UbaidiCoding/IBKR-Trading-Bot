from typing import Dict
from brokers.ibkr.client import IBKRClient
from core.models import TradeConfig, OrderResult
from core.exceptions import TradingError
import asyncio

class TradingEngine:
    def __init__(self):
        self.active_positions: Dict[str, float] = {}
        self.trade_configs: Dict[str, TradeConfig] = {}
        self.broker = None

    async def initialize(self, broker):
        self.broker = broker
        if not await self.broker.connect():
            raise TradingError("Failed to initialize broker connection")

    async def execute_order(self, ticker: str, action: str) -> OrderResult:
        if ticker not in self.trade_configs:
            return OrderResult(success=False, message="No config for ticker")
            
        config = self.trade_configs[ticker]
        
        # Implementation with proper error handling
        # ... (see full implementation below)