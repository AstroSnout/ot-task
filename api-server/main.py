import flask
import time
import json
from flask import request
from datetime import date as dt
# Local imports
from validator import Validator
from etherscan import EtherscanAPI
from scraper import Scraper
from models.NormalTransactions import NormalTransaction

app = flask.Flask(__name__)
scraper = Scraper(
    '--disable-extensions',
    '--disable-gpu',
    '--headless',
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
)


def from_wei(amount):
    if type(amount) is str:
        amount = int(amount)
    return amount * 1/1000000000000000000


def send_error(error_msg):
    return flask.jsonify({
        'error': error_msg
    })


@app.route('/api/', methods=['GET'])
def api_home():
    return f"<h1>Some Basic API</h1><br>"


@app.route('/api/get_balance', methods=['GET'])
def api_get_balance():
    # args= address: hex + date: YYYY-MM-DD
    # Required argument -> wallet address
    if 'address' in request.args:
        try:
            assert Validator.is_hex_address(address := request.args['address'])
        except AssertionError:
            return send_error('Invalid address, please make sure you use a hexadecimal address.')
        if address == '':
            return send_error('No address input found. Please input a valid wallet address in hex format.')
    else:
        return send_error('Address value was not found.')
    # If date included, get historic balance
    if 'date' in request.args:
        try:
            assert Validator.is_date(date := request.args['date']), 'Invalid date, please use YYYY-MM-DD format.'
        except AssertionError:
            return send_error('Invalid date, please use YYYY-MM-DD format.')
        data = scraper.etherscan_historic_balance(address, date)
    # Otherwise get current balance
    else:
        balance = EtherscanAPI.get_balance(address)
        balance = from_wei(balance)
        # Get current time as UNIX timestamp
        timestamp = int(time.time())
        data = {
            'address': address,
            'ether_balance': balance,
            'block_number': int(EtherscanAPI.get_latest_block(), 16),  # Hex to int
            'timestamp': str(timestamp)  # int to str for consistency
        }
    # Return received data as JSON
    return flask.jsonify(data)


@app.route('/api/get_erc20_balance', methods=['GET'])
def api_get_erc20_balance():
    # args= address: hex + date: YYYY-MM-DD
    # Required argument -> wallet address
    if 'address' in request.args:
        try:
            assert Validator.is_hex_address(address := request.args['address'])
        except AssertionError:
            return send_error('Invalid address, please make sure you use a hexadecimal address.')
        if address == '':
            return send_error('No address input found. Please input a valid wallet address in hex format.')
    else:
        return send_error('Address value was not found.')
    # Required argument -> smart contract address
    if 'token' in request.args:
        try:
            assert Validator.is_hex_address(token := request.args['token'])
        except AssertionError:
            return send_error('Invalid smart contract address, please make sure you use a hexadecimal address.')
        if token == '':
            return send_error('No smart contract address input found. Please input a valid wallet address in hex format.')
    else:
        return send_error('Smart contract address value was not found.')

    # If date included, get historic balance
    if 'date' in request.args:
        try:
            assert Validator.is_date(date := request.args['date']), 'Invalid date, please use YYYY-MM-DD format.'
        except AssertionError:
            return send_error('Invalid date, please use YYYY-MM-DD format.')
    # Otherwise get current balance
    else:
        date = dt.today().isoformat()
    data = scraper.etherscan_erc20_historic_balance(address, date, token)
    # Return received data as JSON
    return flask.jsonify(data)


@app.route('/api/get_transactions', methods=['GET'])
def api_get_transactions():
    # args= address: hex + blocknumber: int
    # Required argument -> wallet address
    if 'address' in request.args:
        try:
            assert Validator.is_hex_address(address := request.args['address'])
        except AssertionError:
            return send_error('Invalid address, please make sure you use a hexadecimal address.')
        if address == '':
            return send_error('No address input found. Please input a valid wallet address in hex format.')
    else:
        return send_error('Address value was not found.')
    # If block number included, get transactions from that block to current
    blocknumber = request.args['blocknumber']
    if 'blocknumber' in request.args:
        if blocknumber == '':
            transactions = NormalTransaction.from_api(
                EtherscanAPI.get_normal_transactions(address)
            )[:200]
        else:
            try:
                assert blocknumber.isnumeric()
            except AssertionError:
                return send_error('Block number value is not a number.')
            transactions = NormalTransaction.from_api(
                EtherscanAPI.get_normal_transactions(address, start=blocknumber)
            )
    # Otherwise get up to the latest 200 transactions
    else:
        transactions = NormalTransaction.from_api(
            EtherscanAPI.get_normal_transactions(address)
        )[:200]

    # Return received data as JSON
    return json.dumps([tx.__dict__ for tx in transactions])
