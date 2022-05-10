import requests
from web3 import Web3

URL = "https://955cf8ae-5a74-4e4d-85d4-e8095a57862a.mock.pstmn.io"


def get_data_from_endpoint(URL):
    s = requests.request("GET", URL)
    return s.json()


def makeTransaction(values):
    ADDRESS = "0x227C6160b14E531c43Be4CB3f7d7dC75a1F6a471"
    KEY = "0x743d867cee41c4c33d1f98514396d52822034bf7dfc1fe1e30fc671e0850535a"
    WEB3 = Web3(Web3.HTTPProvider(
        'https://ropsten.infura.io/v3/cecd52cfb8614b9ba5b06c12167ce00f'))
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






