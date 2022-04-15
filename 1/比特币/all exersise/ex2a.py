from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cU5mpRfWCBtM6QAwK7ApTw9bQdWFSxkx5urZ3TPiBY4SbyDMaVSY')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cR18rUvxgwLejYRHpHUZGXncTUMecVDpdYX9sgpoySnN34xieyjX')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cSC7ikwvRYhfayBiYjrwz2KXzp6Tq5JVzfgGT1AZBDtmr6KS7RpC')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

ex2a_txout_scriptPubKey = [OP_3,my_public_key,cust1_public_key,cust2_public_key,cust3_public_key,OP_4,OP_CHECKMULTISIG]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0004
    txid_to_spend = (
        '75988613a832385a4be56c032e0659419e04e04731437248d9fdd424b3419c8a')
    utxo_index = 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
