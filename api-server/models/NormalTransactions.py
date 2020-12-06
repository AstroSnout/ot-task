class NormalTransaction:
    def __init__(self, sender, receiver, value, timestamp, contract_address, has_receipt, has_error, gas_used, gas_price, tx_hash, block_number):
        self.sender = sender
        self.receiver = receiver
        self.value = int(value)
        self.timestamp = int(timestamp)
        self.contract = contract_address if contract_address != '' else None
        self.has_receipt = True if has_receipt == '1' else False
        self.has_error = True if has_error == '1' else False
        self.gas_used = int(gas_used)
        self.gas_price = int(gas_price)
        self.hash = tx_hash
        self.block_number = int(block_number)
        self.fee = int(gas_used) * int(gas_price)

    def __repr__(self):
        return f'{type(self).__name__}(' \
               f'{", ".join([f"{k}={self.__dict__[k]}" for k in self.__dict__])}' \
               f')'

    @staticmethod
    def from_api(list_of_data_dicts):
        return [
            NormalTransaction(
                tx['from'],
                tx['to'],
                tx['value'],
                tx['timeStamp'],
                tx['contractAddress'],
                tx['txreceipt_status'],
                tx['isError'],
                tx['gasUsed'],
                tx['gasPrice'],
                tx['hash'],
                tx['blockNumber']
            ) for tx in list_of_data_dicts
        ]
