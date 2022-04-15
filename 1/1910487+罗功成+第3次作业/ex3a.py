from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3
ex3a_txout_scriptPubKey = [OP_2DUP,OP_ADD,191,OP_EQUALVERIFY,OP_SUB,487,OP_EQUAL]
#实现思路：首先用OP_2DUP确定有两个操作数，并将它们压入栈顶，然后用OP_ADD和OP_SUB来实现将两个元素弹出，并计算他们的和或差，
#将运算的结果保存到OP_EQUALVERIFY，并用OP_EQUAL来验证是否和计算结果一致，若一致则会返回true

######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0003
    txid_to_spend = (
        '75988613a832385a4be56c032e0659419e04e04731437248d9fdd424b3419c8a')
    utxo_index = 2
    #实现思路：注意要使用还没被花费的index，这里要比账户的钱少一点，留一点作为交易费用，txid就是第一次分币操作的hash.
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
    

