from ib_insync import IB, Contract, LimitOrder
from ..base import BaseBroker
from core.models import OrderResult, AccountBalance
from core.exceptions import BrokerError
import logging
import IBKRClient

class IBKRClient(BaseBroker):
    """Interactive Brokers API client implementation"""
    
    def __init__(self, host: str, port: int, client_id: int):
        self.ib = IB()
        self.host = host
        self.port = port
        self.client_id = client_id
        self.logger = logging.getLogger(__name__)
        self._connected = False

    async def connect(self) -> bool:
        """Connect to TWS/IB Gateway"""
        if self._connected:
            return True
            
        try:
            await self.ib.connectAsync(
                host=self.host,
                port=self.port,
                clientId=self.client_id
            )
            self._connected = True
            self.logger.info("Connected to IBKR API")
            return True
        except Exception as e:
            self.logger.error(f"Connection failed: {str(e)}")
            self._connected = False
            raise BrokerError(f"IBKR connection failed: {str(e)}")

    async def get_balance(self) -> AccountBalance:
        """Get current account balance"""
        if not self._connected:
            raise BrokerError("Not connected to IBKR")
            
        try:
            account = self.ib.managedAccounts()[0]
            values = {v.tag: float(v.value) for v in self.ib.accountValues(account)}
            return AccountBalance(
                net_liquidation=values.get('NetLiquidation', 0),
                buying_power=values.get('BuyingPower', 0),
                available_funds=values.get('AvailableFunds', 0)
            )
        except Exception as e:
            raise BrokerError(f"Failed to get balance: {str(e)}")

    async def place_order(self, contract, action: str, 
                         quantity: int, price: float) -> OrderResult:
        """Place an order with IBKR"""
        if not self._connected:
            raise BrokerError("Not connected to IBKR")
            
        try:
            order = LimitOrder(
                action=action,
                totalQuantity=quantity,
                lmtPrice=round(price, 2),
                tif='GTC',
                outsideRth=True
            )
            
            trade = await self.ib.placeOrderAsync(contract, order)
            return OrderResult(
                success=True,
                order_id=trade.order.orderId
            )
        except Exception as e:
            return OrderResult(
                success=False,
                message=str(e)
            )