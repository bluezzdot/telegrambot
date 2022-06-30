from web3.middleware import geth_poa_middleware
from web3 import Web3, HTTPProvider
import json



w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/843baebcf3dc4e4fbcdabd291459e01c"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.isConnected()

# Create a test_account
# When implementing a real faucet, we'll use a real account with address and private key and use it to faucet tokens
my_account = w3.eth.account.create('Đây chỉ là account test !')

# Just test_account
# You shouldn't send any ether to this account
print(my_account._address)
print(my_account._private_key.hex())


abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'
abi = json.loads(abi)


address = '0x7af963cF6D228E564e2A0aA0DdBF06210B38615D' # Address of the goerli eth contract address
goerli_eth = w3.eth.contract(address=address, abi=abi)
# goerli_eth.functions.totalSupply().call()

transaction = goerli_eth.functions.transfer(my_account._address, 0x10).buildTransaction({'chainId': 6284, 
                   'gas': 200000, 
                   'nonce': w3.eth.getTransactionCount("0x3c3abcB8648b7661F3697d5C0C62D4a7c1EdF452")})

signed_txn = w3.eth.account.signTransaction(transaction, '0xa1b1fd0ec299e0f6b7e4b198496cab117116366cd0586333c0884a0b4972c948')
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(txn_hash.hex())

# def send_ether(to, value):
#     nonce = w3.eth.getTransactionCount(my_account._address)
#     txn = {
#         'nonce': nonce,
#         'to': to,
#         'value': w3.toWei(value, 'ether'),
#         'gas': 200000,
#         'gasPrice': w3.toWei('50', 'gwei'),
#         'chainId': 6284 # goerli
#     }
#     signed_txn = my_account.signTransaction(txn)
#     tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
#     return tx_hash

# Send ether from test_account to my_account
# tx_hash = send_ether("0x3c3abcB8648b7661F3697d5C0C62D4a7c1EdF452", 0.1)
# print(tx_hash)
