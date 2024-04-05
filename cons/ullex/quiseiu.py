>>> from web3 import Web3
>>> w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
>>> address_wallet = "0x0000000000000000000000000000000000000000"
>>> nonce = w3.eth.get_transaction_count(address_wallet)
