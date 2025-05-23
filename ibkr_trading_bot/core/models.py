from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class TradingMode(str, Enum):
    PAPER = "paper"
    LIVE = "live"

class TradeConfig(BaseModel):
    ticker: str = Field(..., min_length=1, max_length=10)
    order_size_usd: float = Field(..., gt=0)
    min_profit_pct: float = Field(..., gt=0)
    allow_partial: bool = False

class AccountBalance(BaseModel):
    net_liquidation: float
    buying_power: float
    available_funds: float

class OrderResult(BaseModel):
    success: bool
    order_id: Optional[str] = None
    message: Optional[str] = None