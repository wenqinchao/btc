# btc 
A simple python package interacts with the btcoin node

```
from btc.bitcoin import BitCoin

btc = BitCoin(BitCoin.HttpProvider("your rpc username", "your rpc password"))

block_count = btc.chain.get_block_count()
print(block_count)
```
