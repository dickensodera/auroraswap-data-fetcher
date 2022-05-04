import json
from web3 import Web3,HTTPProvider
from flask import Flask
import requests
import aiohttp

app = Flask(__name__)

infura_app_url = 'https://mainnet.infura.io/v3/bd8ced3c5d54459d9090ba85fb625c85'
web3 = Web3(HTTPProvider(infura_app_url))
assert True is web3.isConnected()
print('Network connected')

def get_contract():
    brl_contract_address = '0x35CC71888DBb9FfB777337324a4A60fdBAA19DDE'
    with open('./BRLToken.json', encoding='utf-8') as abi_file:
        brl_contract_abi = json.load(abi_file)
    
    contract = web3.eth.contract(address=brl_contract_address,abi=brl_contract_abi)
    return contract

@app.route('/')
def say_hello():
    return "Hello World"


@app.route('/data')
def fetch_pool_length():
    contract = get_contract()
    pool_lengh = contract.functions.poolLength().call()
    return pool_lengh

    #url = 'https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=0x35CC71888DBb9FfB777337324a4A60fdBAA19DDE&vs_currencies=usd'
    #data = requests.get(url).json()



if __name__ == '__main__':
    app.run(debug=True)
