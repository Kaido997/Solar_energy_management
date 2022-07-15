import requests
from web3 import Web3
from energy.secret import ADDRESS, KEY, ROPSTEN
import random

def get_data_from_endpoint(endpointurl):
    '''request data from endpoint and random it just for testing'''
    s = requests.request("GET", endpointurl).json()
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)
    new_random_values = dict(produced_energy_in_watt = s['produced_energy_in_watt'] + num1 , consumed_energy_in_watt = s['consumed_energy_in_watt'] + num2)
    return new_random_values 


def makeTransaction(values):
    WEB3 = Web3(Web3.HTTPProvider(ROPSTEN))
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






