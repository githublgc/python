from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import P2PKH_scriptPubKey
from ex3a import ex3a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0001
txid_to_spend = 'e76662023e62da84018fc5ef699e3f2e8133669a92e34cfda7d16f686cc4e335'
utxo_index = 0
#思路：在a的脚本实现后，将会得到目标hash地址，将其填入这里，由于第一次使用，所以index为0
######################################################################

txin_scriptPubKey = ex3a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 3a.
txin_scriptSig = [339,-148]
#思路：这里sig就是计算的结果，它用来验证前面的计算结果是否匹配。只需要把算出来的x,y值填入即可。
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey)
print(response.status_code, response.reason)
print(response.text)
#交易号1：e76662023e62da84018fc5ef699e3f2e8133669a92e34cfda7d16f686cc4e335。
#交易号2：5e3907ad277b7243406644468583cfc3332c9b9b8be749c7a1961728dc1858b1。
