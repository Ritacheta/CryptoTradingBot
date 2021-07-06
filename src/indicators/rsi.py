import numpy as np
from typing import Union


def get_rsi(close: Union[np.ndarray, list], period: int) -> float:
    """
    Calculate the RSI for a given period. 
    Refer - https://www.fmlabs.com/reference/default.htm?url=CMO.htm

    Arguments:
    close - list or numpy array of close prices, latest last (highest index)
    period - period for which RSI has to be calculated

    Returns:
    RSI of the given close values
    """
    assert len(close) > period
    current_close = np.array(close[-period:])
    prev_close = np.array(close[-period-1:-1])
    diff = current_close-prev_close

    num = np.sum(np.clip(diff, 0, np.Inf))
    denum = np.sum(np.abs(diff))

    rsi = 100*num/denum
    return rsi
