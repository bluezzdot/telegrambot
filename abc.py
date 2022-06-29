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