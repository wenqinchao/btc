# btc-cj
A simple python package interacts with the bitcoin node, python version >=3.6 is recommend
## install
```
pip3 install btc-cj
```
## Docs
Reference: https://developer.bitcoin.org/reference/rpc/
## Groups
* [connect](#connect)
* [chain](#chain)
    * [get_block_count](#get_block_count)
    
### connect 
```
from btc.bitcoin import BitCoin
bitcoin = BitCoin(BitCoin.HttpProvider("your rpc username", "your rpc password"))
# The default provider is "http://127.0.0.1:8332", You can use other providers 
bitcoin = BitCoin(BitCoin.HttpProvider("your rpc username", "your rpc password", "your provider "))
```
### chain
#### get_block_count
Inputs:
```none```
Outputs:
``````
```
block_count = bitcoin.chain.get_block_count()
print(block_count)
```
