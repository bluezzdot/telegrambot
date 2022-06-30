from web3.middleware import geth_poa_middleware
from eth_utils import to_wei
from web3 import Web3
import os
import json

def send(address: str):
    # w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/843baebcf3dc4e4fbcdabd291459e01c")) # Goerli TESTNET
    # w3.middleware_onion.inject(geth_poa_middleware, layer=0) 

    w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org")) # bsc MAINNET
    print(f"Connect Status: {w3.isConnected()}")

    my_address = '0x6e143f784Cb160f10966096AB2aC4207D633d5d7'
    private_key = os.getenv('PRIVATE_KEY')
    receiver_address = '0x3c3abcB8648b7661F3697d5C0C62D4a7c1EdF452'
    add1 = Web3.toChecksumAddress(my_address)
    add2 = Web3.toChecksumAddress(receiver_address)

    nonce = w3.eth.getTransactionCount(add1)
    ### CHECK INFORMATION ###
    print(f"Nonce: {nonce}")
    print(f"Wei: {w3.eth.get_balance(add1)}")
    print(f"$: {w3.fromWei(w3.eth.get_balance(add1), 'ether')} BNB")

    transaction = {
        'nonce': nonce,
        'to': add2,
        # value send in bsc chain
        'value': Web3.toWei(0.0001, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei('50', 'gwei'),
    }

    # MẤT TIỀN
    signed_tx = w3.eth.account.signTransaction(transaction, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction hash: {w3.toHex(tx_hash)}")

# print(f'{goerli_eth.functions.name().call()}: {goerli_eth.functions.totalSupply().call()}')

# transaction = goerli_eth.functions.transfer(add2, to_wei(0.01, 'ether')).buildTransaction({
#         'nonce': nonce,
#         'gas': 21000,
#         'chainId': 1337,
# })

# transaction = {
#     'nonce': nonce,
#     'to': add2,
#     'value': w3.toWei(.001, 'ether'),
#     'gas': 21000,
#     'gasPrice': w3.toWei('50', 'gwei'),
# }

# signed_tx = w3.eth.account.signTransaction(transaction, private_key)
# tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

# print(tx_hash)




# receiver = w3.eth.account.create('Đây chỉ là account test !')
# print(receiver._address) # 0xAd0B477d834839c1205a93E8Bb6d00C15F5BDc1B
# print(receiver._private_key.hex()) # 0x3b256fbc8bdd97aa2c7125db7f7df9d53e583c78735c9ac6dd2c34a168d2e635
# # read an account to eth_account.signers.local.LocalAccount
# privatekey = '0xa1b1fd0ec299e0f6b7e4b198496cab117116366cd0586333c0884a0b4972c948'
# my_account = w3.eth.account.from_key(privatekey)

# abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'
# abi = json.loads(abi)

# address = '0x7af963cF6D228E564e2A0aA0DdBF06210B38615D' # Address of the goerli eth contract address
# goerli_eth = w3.eth.contract(address=address, abi=abi)

# transaction = goerli_eth.functions.transfer('0xAd0B477d834839c1205a93E8Bb6d00C15F5BDc1B', 0x10).buildTransaction({'chainId': 6284, 'gas':70000, 'nonce': w3.eth.getTransactionCount(my_account._address)})
# signed_txn = w3.eth.account.signTransaction(transaction, privatekey)
# txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
# print(txn_hash)

# Send goerli eth from an account to another account
# tx_hash = goerli_eth.functions.transfer(my_account.address, 100).transact({'from': my_account.address})
# w3.eth.waitForTransactionReceipt(tx_hash)
# print(w3.eth.getBalance(my_account.address))
# print(w3.eth.getBalance(address))


