import requests
from web3 import Web3
from .secret import ADDRESS, KEY

def get_data_from_endpoint(endpointurl):
    s = requests.request("GET", endpointurl)
    return s.json()


def makeTransaction(values):
    WEB3 = Web3(Web3.HTTPProvider(
        ''))
    nonce = WEB3.eth.getTransactionCount(ADDRESS)
    gasPrice = WEB3.eth.gasPrice
    value = WEB3.toWei(0, 'ether')
    signedTx = WEB3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=values.encode('utf-8')), KEY)
    tx = WEB3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = WEB3.toHex(tx)
    return txId






