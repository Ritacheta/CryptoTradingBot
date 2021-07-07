import pandas as pd
import os
from pandas._typing import FrameOrSeries
from pandas import DataFrame
from . import _dirpath
from typing import Tuple

def prepare_csv(data:dict) -> Tuple[DataFrame, str]:
    """
    If CMO_data.csv exists read the previous value stored and returns

    Returns:
    DataFrame : data stored in the csv file
    """
    path = os.path.join(_dirpath,"..", "..", "Data","Exchange","data.csv")
    if not os.path.exists(path):
        with open(path,"w") as f:
            f.write(",".join(data.keys()))
    df = pd.read_csv(path)
    return df,path

def prepare_to_store(time:int,symbol:str,opening_price:float,closing_price:float,high:float,low:float,indicators:dict):
    """
    To store and analyze the CMO values
    store upto 100 older data 

    Arguements:
    time : current server side time
    symbol - symbol of the coin-pair
    opening_price - opening price of the coin
    closing_price - closing price of the coin
    high - highest price
    low - lowest price
    indicators - dict("indicator_name",value)

    Returns:
    None
    """
    data={
        "time":time,
        "symbol":symbol,
        "opening_price":opening_price,
        "closing_price":closing_price,
        "high":high,
        "low":low,
    }
    data.update(indicators)
    df,path = prepare_csv(data)
    df = df.append(data,ignore_index=True)
    df.sort_values(["Timestamp","symbol"])
    df.to_csv(path)

def get_symbols_history() -> DataFrame:
    """
    To get history of all symbols stored in data.csv

    Returns:
    DataFrame - returns a DataFrame object with all history
    """
    path = os.path.join(_dirpath,"..", "..", "Data","Exchange","data.csv")
    df = pd.read_csv(path)
    return df

def get_symbol_history(symbol:str) -> DataFrame:
    """
    To get the history the specific symbol
    
    Returns:
    DataFrame - DataFrame object of the history of the symbol
    """
    path = os.path.join(_dirpath,"..", "..", "Data","Exchange","data.csv")
    df=pd.read_csv(path)
    df = df.loc[df["symbol"]==symbol]
    return df

def init_prev_orders_csv():
    """
    Initializes the prev_orders.csv 
    """
    columns = ["Symbol","Order_Volume","Order_Price","Buying_Timestamp","Buying_Price","Selling_Timestamp","Selling_Price"]
    path = os.path.join(_dirpath,"..", "..", "Data","Exchange","prev_orders.csv")
    with open(path) as f:
        f.columns = columns
        f.close()

def record_prev_orders(symbol:str,order_volume:float,order_price:float,buying_time:int,buying_price:float,selling_time:int,selling_price:float):
    """accuracies
    To store the order record in prev_orders.csv

    Arguements:
    symbol - exchange symbol,
    order_volume - total volume ordered
    order_price - price at which ordered
    buying_time - time at which bought
    buying_price - buying price
    selling_time - time at which sold
    selling_price - selling price
    """
    data = {
        "Symbol":symbol,
        "Order_Volume":order_volume,
        "Order_Price":order_price,
        "Buying_Timestamp":buying_time,
        "Buying_Price":buying_price,
        "Selling_Timestamp":selling_time,
        "Selling_Price":selling_price
    }
    path = os.path.join(_dirpath,"..", "..", "Data","Exchange","prev_orders.csv")
    df = pd.read_csv(path)
    df = df.append(data,ignore_index=True)
    df.sort_values(["Timestamp","symbol"])
    df.to_csv(path)