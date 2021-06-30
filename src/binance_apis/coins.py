from binance.spot import Spot
def coins_prices(client:Spot,symbol:str=None) -> list:
    """
    Get the current prices of each coin

    Arguements:
    client : Spot object
    symbol : exchange pair symbol

    Returns:
    list -> current prices of coins
    """
    return client.ticker_price(symbol)

