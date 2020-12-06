import requests
from decouple import config


class EtherscanAPI:
    key = config('ETHERSCAN_API_KEY')
    url = 'https://api.etherscan.io/api'

    @staticmethod
    def get_normal_transactions(address, start=0, end=99999999, sort='asc'):
        data = requests.get(
            f'{EtherscanAPI.url}'
            f'?module=account'
            f'&action=txlist'
            f'&address={address}'
            f'&startblock={start}'
            f'&endblock={end}'
            f'&sort={sort}'
            f'&apikey={EtherscanAPI.key}'
        )
        return data.json()['result']

    @staticmethod
    def get_internal_transactions(address, start=0, end=99999999, sort='asc'):
        data = requests.get(
            f'{EtherscanAPI.url}'
            f'?module=account'
            f'&action=txlistinternal'
            f'&address={address}'
            f'&startblock={start}'
            f'&endblock={end}'
            f'&sort={sort}'
            f'&apikey={EtherscanAPI.key}'
        )
        return data.json()['result']

    @staticmethod
    def get_balance(address):
        data = requests.get(
            f'{EtherscanAPI.url}'
            f'?module=account'
            f'&action=balance'
            f'&address={address}'
            f'&tag=latest'
            f'&apikey={EtherscanAPI.key}'
        )
        return data.json()['result']

    @staticmethod
    def get_latest_block():
        data = requests.get(
            f'{EtherscanAPI.url}'
            f'?module=proxy'
            f'&action=eth_blockNumber'
            f'&apikey={EtherscanAPI.key}'
        )
        return data.json()['result']
