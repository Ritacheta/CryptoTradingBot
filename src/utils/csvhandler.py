import datetime
import time
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

def prepare_to_store(symbol:str,opening_price:float,closing_price:float,high:float,low:float,indicators:dict):
    """
    To store and analyze the CMO values
    store upto 100 older data 

    Arguements:
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
        "symbol":symbol,
        "opening_price":opening_price,
        "closing_price":closing_price,
        "high":high,
        "low":low,
        "date":datetime.date.today(),
        "time":time.time()
    }
    data.update(indicators)
    df,path = prepare_csv(data)
    df.append(data)
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
    path = path = os.path.join(_dirpath,"..", "..", "Data","Exchange","data.csv")
    df=pd.read_csv(path)
    df = df.loc[df["symbol"]==symbol]
    return df