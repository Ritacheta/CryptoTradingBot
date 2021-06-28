from utils.creds import get_credentials
from binance.spot import Spot


def get_spot_client() -> Spot:
    """
    Get the Spot Client using credentials

    Returns:
    Spot Client object
    """
    try:
        return Spot(**get_credentials())
    except Exception as e:
        print(e)
        print(
            "credentials.json format must be {'key':<your-api-key>, 'secret':<your-secret-key>}")
        exit()
