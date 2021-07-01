import datetime
import time
import pandas as pd
import os
from . import _dirpath

def prepare_to_store(symbol:str,opening_price:float,closing_price:float,cmo_value:float) -> dict:
    """
    To store and analyze the CMO values
    store upto 100 older data 

    """
    data={
        "symbol":symbol,
        "opening_price":opening_price,
        "closing_price":closing_price,
        "cmo_value":cmo_value,
        "date":datetime.date.today(),
        "time":time.time()
    }
    return data

def prepare_csv() -> pd.DataFrame:
    """
    If CMO_data.csv exists read the previous value stored and returns

    Returns:
    DataFrame : data stored in the csv file
    """
    path = os.path.join(_dirpath,"..", "..", "Data", "CMO_data.csv")
    if not os.path.exists(path):
        open(path,"w").close
    return path

def store_data_in_csv(data:dict):
    """
    Store the data in the CMO_data.csv

    Arguements:
    data:data with all required info about cmo and the prices
    """
    path = prepare_csv()
    with open(path) as f:
        df = pd.read_csv(f)
        df.append(data)