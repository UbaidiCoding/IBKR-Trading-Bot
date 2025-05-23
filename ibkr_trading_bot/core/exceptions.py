# core/exceptions.py
class TradingError(Exception):
    """Base class for all trading-related exceptions"""
    pass

class BrokerError(TradingError):
    """Exception raised for broker-related errors"""
    pass

class ConfigurationError(TradingError):
    """Exception raised for configuration errors"""
    pass

class BrokerError(Exception):
    """Custom exception for broker-related errors."""
    pass
