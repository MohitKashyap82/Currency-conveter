from fastmcp import FastMCP

# Create FastMCP instance
mcp = FastMCP(name="CurrencyConverter")

# Constants for conversion rates
USD_TO_GBP_RATE = 0.76
GBP_TO_USD_RATE = 1 / USD_TO_GBP_RATE

@mcp.tool()
def usd_to_gbp(amount: float) -> dict:
    """Convert USD to GBP using current exchange rate.
    
    Args:
        amount: Amount in USD to convert
    Returns:
        Dictionary containing the converted amount in GBP and the exchange rate used
    """
    if amount < 0:
        return {"error": "Amount cannot be negative"}
    
    converted_amount = round(amount * USD_TO_GBP_RATE, 2)
    return {
        "original_amount": amount,
        "original_currency": "USD",
        "converted_amount": converted_amount,
        "target_currency": "GBP",
        "exchange_rate": USD_TO_GBP_RATE
    }

@mcp.tool()
def gbp_to_usd(amount: float) -> dict:
    """Convert GBP to USD using current exchange rate.
    
    Args:
        amount: Amount in GBP to convert
    Returns:
        Dictionary containing the converted amount in USD and the exchange rate used
    """
    if amount < 0:
        return {"error": "Amount cannot be negative"}
    
    converted_amount = round(amount * GBP_TO_USD_RATE, 2)
    return {
        "original_amount": amount,
        "original_currency": "GBP",
        "converted_amount": converted_amount,
        "target_currency": "USD",
        "exchange_rate": GBP_TO_USD_RATE
    }

@mcp.tool()
def get_exchange_rates() -> dict:
    """Get current exchange rates for USD/GBP pair.
    
    Returns:
        Dictionary containing current exchange rates
    """
    return {
        "USD_TO_GBP": USD_TO_GBP_RATE,
        "GBP_TO_USD": GBP_TO_USD_RATE,
        "last_updated": "2025-10-31"
    }

if __name__ == "__main__":
    mcp.run()
