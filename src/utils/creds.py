import json
import os
from . import _dirpath


def get_credentials() -> dict:
    """
    Get the credentials from Data/credentials.json

    Returns:
    dict -> key, secret
    """
    with open(os.path.join(_dirpath, "..", "..", "Data", "credentials.json")) as jsonf:
        creds = json.load(jsonf)

    return creds
