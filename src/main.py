import time
from binance_apis.client import get_spot_client
from utils.handler import get_current_coins,cancel_locked_orders,hold_or_sell_coins
from binance_apis.coins import coins_prices


client = get_spot_client()
acc_details=client.account()
if acc_details["canTrade"] and acc_details["accountType"] == "SPOT":
    free_coins, locked_coins = get_current_coins(acc_details)
    # Cancel all open orders
    count = 0
    while len(locked_coins) and count<10:
        cancel_locked_orders(client,locked_coins)
        count+=1
        time.sleep(2)
        acc_details = client.account()
        free_coins, locked_coins = get_current_coins(acc_details)
    # To decide whether to hold or sell the free coins
    hold_or_sell_coins(client,free_coins)