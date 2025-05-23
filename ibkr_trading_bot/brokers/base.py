from abc import ABC, abstractmethod
from core.models import OrderResult, AccountBalance
from core.exceptions import BrokerError
from core.exceptions import BrokerError

class BaseBroker(ABC):
    """Abstract base class for all broker implementations"""
    
    @abstractmethod
    async def connect(self) -> bool:
        """Connect to the broker"""
        pass
    
    @abstractmethod
    async def get_balance(self) -> AccountBalance:
        """Get account balance information"""
        pass
    
    @abstractmethod
    async def place_order(self, contract, action: str, 
                         quantity: int, price: float) -> OrderResult:
        """Place an order with the broker"""
        pass