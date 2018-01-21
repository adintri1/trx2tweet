import requests
import json
from requests import Timeout, HTTPError


class TrxData:

    def __init__(self):
        """timeout: Slightly larger than a multiple of 3, which is the default TCP packet retransmission window."""
        self.timeout = 3.05
        self.base_url = "https://api.coinmarketcap.com/v1/ticker/"
        self.crypto_currency = "tron"
        self.url = f"{self.base_url}{self.crypto_currency}"

    def get_price(self):
        try:
            s = requests.Session()
            raw_info = s.get(self.url, timeout=self.timeout)
            raw_info.raise_for_status()
            json_info = json.loads(raw_info.text)
            s.close()
            price = json_info[0]["price_usd"]
            return price

        except Timeout as err:
            print("TimeoutError: {0}".format(err))
        except HTTPError as err:
            print("HTTPError: {0}".format(err))
        except:
            pass

