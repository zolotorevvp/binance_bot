import os

from binance.client import Client
from dotenv import load_dotenv
load_dotenv()
os.system("w32tm/resync")


def main():
    api_key = os.environ.get('binance_api')
    api_secret = os.environ.get('binance_secret')

    client = Client(api_key, api_secret)

    client.API_URL = 'https://testnet.binance.vision/api'
    print(client.get_account())
    #print(client.get_asset_balance(asset='BTC'))


if __name__ == "__main__":
    main()
