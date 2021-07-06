from typing import Tuple, Union
from binance.spot import Spot
import config

def get_current_coins(acc_details:dict) -> Tuple[list,list]:
    """
    From account details get the non zero valued coins

    Arguments:
    acc_details - account details from Spot().account()
    
    Returns:
    list -> Non-zero free coins
    list -> Non-zero locked coins
    """
    balances = acc_details["balances"]
    free_balances = []
    locked_balances = []
    for balance in balances:
        asset, free, locked = balance.values()
        if float(locked) != 0.0:
            locked_balances.append(balance)
        if float(free) != 0.0:
            free_balances.append(balance)   
    return free_balances,locked_balances

def cancel_locked_orders(client:Spot,locked_coins:list):
    """
    Cancel all the open orders
    
    Arguments:
    client : Spot Object
    locked_coins : coins with non-zero locked balance
    """
    for coin in locked_coins:
        try:
            client.cancel_open_orders(coin["asset"]+config.BASE_COIN)
        except Exception as e:
            print(e)

def hold_or_sell_coins(client:Spot, coins:list):
    """
    makes the decision whether to sell or hold the current purchased coins
    
    Arguments:
    client : Spot object
    coins : free coins
    """
    # 1. Check loss - if current_price < LOSS_RATIO * selling_price
    # 2. Indicators values - overbought condition