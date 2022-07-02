from web3.middleware import geth_poa_middleware
from eth_utils import to_wei
from web3 import Web3
import os

def send(receiver_address: str = '0x3c3abcB8648b7661F3697d5C0C62D4a7c1EdF452', sender_address: str = '0x6e143f784Cb160f10966096AB2aC4207D633d5d7') -> str:
    
    """
        Send BNB testnet to receiver_address
        
        INPUT:
        sender_address: address of sender, default is 0x6e143f784Cb160f10966096AB2aC4207D633d5d7
        receiver_address: address of receiver, default is 0x3c3abcB8648b7661F3697d5C0C62D4a7c1EdF452

        RETURN:
        tx_hash: transaction hash. You can check on https://testnet.bscscan.com/
    """

    w3 = Web3(Web3.HTTPProvider("https://data-seed-prebsc-1-s1.binance.org:8545/")) # BSC TESTNET
    print(f"[i] Connect Status: {w3.isConnected()}")

    private_key = os.getenv('PRIVATE_KEY')
    add1 = Web3.toChecksumAddress(sender_address)
    add2 = Web3.toChecksumAddress(receiver_address)
    nonce = w3.eth.getTransactionCount(add1)

    ### CHECK INFORMATION ###
    print(f"Sender: {add1}")
    print(f"Reiver: {add2}")
    print(f"Nonce: {nonce}")
    print(f"Wei: {w3.eth.get_balance(add1)}")
    print(f"$BNB: {w3.fromWei(w3.eth.get_balance(add1), 'ether')} BNB testnet")

    # Configurate transaction
    transaction = {
        'nonce': nonce,
        'to': add2,
        # value send in bsc chain
        'value': Web3.toWei(0.0001, 'ether'),
        'gas': 21005,
        'gasPrice': w3.toWei('50', 'gwei'),
    }

    # Sign the transaction with the private key
    signed_tx = w3.eth.account.signTransaction(transaction, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"[i] Transaction hash: {w3.toHex(tx_hash)}")
