# btc-cj
A simple python package interacts with the bitcoin node, python version >=3.6 is recommend
# Install
```
pip3 install btc-cj
```
# Docs
Reference: https://developer.bitcoin.org/reference/rpc/
# Groups
* [connect](#connect)
* [chain](#chain)
    * [get_block_chain_info](#get_block_chain_info)
    * [get_block_count](#get_block_count)
    * [get_latest_block_hash](#get_latest_block_hash)
    * [get_block_hash](#get_block_hash)
    * [get_block](#get_block)
* [raw](#raw)
    * [get_raw_transaction](#get_raw_transaction)
    * [decode_raw_transaction](#decode_raw_transaction)
* [wallet](#wallet)
    * [create_wallet](#create_wallet)
    * [load_wallet](#load_wallet)
    * [list_wallets](#list_wallets)
    * [encrypt_wallet](#encrypt_wallet)
    * [wallet_pass_phrase](#wallet_pass_phrase)
    * [wallet_lock](#wallet_lock)
    * [get_new_address](#get_new_address)
    * [get_balance](#get_balance)
    * [list_received_by_address](#list_received_by_address)
    * [list_received_by_label](#list_received_by_label)
* [utils](#utils)
    * [validate_address](#validate_address)

# connect 
```
from btc.bitcoin import BitCoin
bitcoin = BitCoin(BitCoin.HttpProvider("your rpc username", "your rpc password"))
# The default provider is "http://127.0.0.1:8332", You can use other providers 
bitcoin = BitCoin(BitCoin.HttpProvider("your rpc username", "your rpc password", "your provider "))
```
# chain

## get_block_chain_info
**Inputs**:
```None```
**Example**
```
chain_info = bitcoin.chain.get_block_chain_info()
print(chain_info)
```
**Outputs**:
```
{
  'chain': 'main',
  'blocks': 676489,
  'headers': 676489,
  'bestblockhash': '00000000000000000001568e72a26b2bed6507a2ad59a3693c1df544298aa290',
  'difficulty': 21865558044610.55,
  'mediantime': 1616822714,
  'verificationprogress': 0.9999993635662282,
  'initialblockdownload': False,
  'chainwork': '00000000000000000000000000000000000000001b3249afd4bde69d3038e35a',
  'size_on_disk': 381107213760,
  'pruned': False,
  'softforks': {
    'bip34': {
      'type': 'buried',
      'active': True,
      'height': 227931
    },
    'bip66': {
      'type': 'buried',
      'active': True,
      'height': 363725
    },
    'bip65': {
      'type': 'buried',
      'active': True,
      'height': 388381
    },
    'csv': {
      'type': 'buried',
      'active': True,
      'height': 419328
    },
    'segwit': {
      'type': 'buried',
      'active': True,
      'height': 481824
    }
  },
  'warnings': ''
}
```

## get_block_count
**Inputs**:
```None```
**Example**
```
block_count = bitcoin.chain.get_block_count()
print(block_count)
```
**Outputs**:
```676487```

## get_latest_block_hash
**Inputs**:
```None```
```
**Example**
block_hash = bitcoin.chain.get_latest_block_hash()
print(block_hash)
```
**Outputs**:
```
"00000000000000000001568e72a26b2bed6507a2ad59a3693c1df544298aa290"
```

## get_block_hash
**Inputs**:
```
{"height":676486}
```
**Example**
```
block_hash = bitcoin.chain.get_block_hash(676486)
print(block_hash)
```
**Outputs**:
```
"00000000000000000004194093f23783768d7904234c0dbba53e85bce6ecd8b4"
```

## get_block
**Inputs**:
```
{
    "block_hash":"00000000000000000004194093f23783768d7904234c0dbba53e85bce6ecd8b4",
    "verbosity":(1 or 2)
}
```
**Example**
```
block = bitcoin.chain.get_block("00000000000000000004194093f23783768d7904234c0dbba53e85bce6ecd8b4",1)
print(block)
```
**Outputs**:
```
{
  'hash': '00000000000000000004194093f23783768d7904234c0dbba53e85bce6ecd8b4',
  'confirmations': 6,
  'strippedsize': 785759,
  'size': 1635717,
  'weight': 3992994,
  'height': 676486,
  'version': 805298176,
  'versionHex': '2fffe000',
  'merkleroot': 'a459aa15500bb7329048c3a6de618f6246331afb7da52a9b4d8d3f644dbd9b2a',
  'tx': [
    'f68394a5fa08907fbdd049401a4da25b10bd57f9301822747a23830fe328de6e',
    '758068faf8d7595a9947aa12c4a5eef345b019249cf356641092675bc47ccbb1',
    ...
    '19ba0de5b052b1681175b4a03ff5e253596f45d0b383c4d28d69e9514cbf2358',
    '59d30eb97e67114b17f6844f894ef1a7c2f6857fad233c79895d350631b0df70'
  ],
  'time': 1616823172,
  'mediantime': 1616820760,
  'nonce': 721999411,
  'bits': '170cdf6f',
  'difficulty': 21865558044610.55,
  'chainwork': '00000000000000000000000000000000000000001b320e06ae9ef1369631a55f',
  'nTx': 819,
  'previousblockhash': '000000000000000000017405ac02f1d4189edb4fda1d22b23336aa2c5941aa0c',
  'nextblockhash': '000000000000000000042264a471acdf4b9b3cbd98e585072f1505f092b7d3d3'
}
```
**Example**
```
# verbosity = 2
block = bitcoin.chain.get_block("00000000000000000004194093f23783768d7904234c0dbba53e85bce6ecd8b4",2)
print(block)
```
**Outputs**:
```
{
  "hash": "00000000000000000005dab6d9ad630d162b9912d211bac7eff372da3ab9fb5d",
  "confirmations": 3085,
  "strippedsize": 881548,
  "size": 1348604,
  "weight": 3993248,
  "height": 669720,
  "version": 541065216,
  "versionHex": "20400000",
  "merkleroot": "eeab6aa0784b444ad1996dbe9c9f2ca99a9ab55986c834e013491fff67b4cc33",
  "tx": [
    {
      "txid": "7315436d4514d09e9920cd713926c06787a6b3482f8447024553387296e37139",
      "hash": "79385437cb24518284dcefa937608c1c9f0c6af582d84d7cbdf8dff73dd3706c",
      "version": 1,
      "size": 351,
      "vsize": 324,
      "weight": 1296,
      "locktime": 0,
      "vin": [
        {
          "coinbase": "0318380a1b4d696e656420627920416e74506f6f6c37313718001502e4062246fabe6d6db12f2886437ab2653bb68931b5064e4504431a62f9249aaac5055b8689a61ded0200000000000000d74200001b1f0000",
          "txinwitness": [
            "0000000000000000000000000000000000000000000000000000000000000000"
          ],
          "sequence": 4294967295
        }
      ],
      "vout": [
        {
          "value": 7.91767516,
          "n": 0,
          "scriptPubKey": {
            "asm": "OP_DUP OP_HASH160 11dbe48cc6b617f9c6adaf4d9ed5f625b1c7cb59 OP_EQUALVERIFY OP_CHECKSIG",
            "hex": "76a91411dbe48cc6b617f9c6adaf4d9ed5f625b1c7cb5988ac",
            "reqSigs": 1,
            "type": "pubkeyhash",
            "addresses": [
              "12dRugNcdxK39288NjcDV4GX7rMsKCGn6B"
            ]
          }
        },
        {
          "value": 0.00000000,
          "n": 1,
          "scriptPubKey": {
            "asm": "OP_RETURN aa21a9ed847cecd8d19a2b273e9ed719712fb52c673ccf7c8c486298fa674ac8471b2ecc",
            "hex": "6a24aa21a9ed847cecd8d19a2b273e9ed719712fb52c673ccf7c8c486298fa674ac8471b2ecc",
            "type": "nulldata"
          }
        },
        {
          "value": 0.00000000,
          "n": 2,
          "scriptPubKey": {
            "asm": "OP_RETURN b9e11b6d5edc611765152f7bc839ccc42f8fde51b16f98dc5d90d67ad5ab9401e3bf8caa",
            "hex": "6a24b9e11b6d5edc611765152f7bc839ccc42f8fde51b16f98dc5d90d67ad5ab9401e3bf8caa",
            "type": "nulldata"
          }
        },
        {
          "value": 0.00000000,
          "n": 3,
          "scriptPubKey": {
            "asm": "OP_RETURN 52534b424c4f434b3a901e65f5f1903c005f31b41a63e7d648e405f808e9d5627a4eae8229002f25ac",
            "hex": "6a2952534b424c4f434b3a901e65f5f1903c005f31b41a63e7d648e405f808e9d5627a4eae8229002f25ac",
            "type": "nulldata"
          }
        }
      ],
      "hex": "010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff540318380a1b4d696e656420627920416e74506f6f6c37313718001502e4062246fabe6d6db12f2886437ab2653bb68931b5064e4504431a62f9249aaac5055b8689a61ded0200000000000000d74200001b1f0000ffffffff04dc69312f000000001976a91411dbe48cc6b617f9c6adaf4d9ed5f625b1c7cb5988ac0000000000000000266a24aa21a9ed847cecd8d19a2b273e9ed719712fb52c673ccf7c8c486298fa674ac8471b2ecc0000000000000000266a24b9e11b6d5edc611765152f7bc839ccc42f8fde51b16f98dc5d90d67ad5ab9401e3bf8caa00000000000000002b6a2952534b424c4f434b3a901e65f5f1903c005f31b41a63e7d648e405f808e9d5627a4eae8229002f25ac0120000000000000000000000000000000000000000000000000000000000000000000000000"
    },
    {
      "txid": "3ca26fe995a6c53e2c8b2457e068cc0321eccedfa4e0ea60627e03c86f4305d8",
      "hash": "3ca26fe995a6c53e2c8b2457e068cc0321eccedfa4e0ea60627e03c86f4305d8",
      "version": 1,
      "size": 387,
      "vsize": 387,
      "weight": 1548,
      "locktime": 0,
      "vin": [
        {
          "txid": "8296fb964bd6dbcbc8567e8b731d964fcd5c481b26669a7faaf675f7eb91dc94",
          "vout": 10,
          "scriptSig": {
            "asm": "304402200f39c3128648123c3e97b1609499bb9cb75f28c7e51110fdfe09b5e9c07fd19d02204ce16e193980969bb90feb80fae3b5d0ad0453416aeb97a01edc4e128895565f[ALL] 04c4b7a7f7bb2c899f4aeab75b41567c040ae79506d43ee72f650c95b6319e47402f0ba88d1c5a294d075885442679dc24882ea37c31e0dbc82cfd51ed185d7e94",
            "hex": "47304402200f39c3128648123c3e97b1609499bb9cb75f28c7e51110fdfe09b5e9c07fd19d02204ce16e193980969bb90feb80fae3b5d0ad0453416aeb97a01edc4e128895565f014104c4b7a7f7bb2c899f4aeab75b41567c040ae79506d43ee72f650c95b6319e47402f0ba88d1c5a294d075885442679dc24882ea37c31e0dbc82cfd51ed185d7e94"
          },
          "sequence": 4294967295
        }
      ],
      "vout": [
        {
          "value": 0.00864000,
          "n": 0,
          "scriptPubKey": {
            "asm": "OP_HASH160 241b7ad339c2f3c43bd5f34db630d69fa914848d OP_EQUAL",
            "hex": "a914241b7ad339c2f3c43bd5f34db630d69fa914848d87",
            "reqSigs": 1,
            "type": "scripthash",
            "addresses": [
              "34ywAn7Y4YEZBk34XAmMBo1YqsqXRra8DR"
            ]
          }
        },
        {
          "value": 0.03261804,
          "n": 1,
          "scriptPubKey": {
            "asm": "OP_DUP OP_HASH160 344921df9da453f9b9de4590302c5702e5dd8656 OP_EQUALVERIFY OP_CHECKSIG",
            "hex": "76a914344921df9da453f9b9de4590302c5702e5dd865688ac",
            "reqSigs": 1,
            "type": "pubkeyhash",
            "addresses": [
              "15mTkJGcBvQGARkYBzT9QVzWxJZSbjSKVB"
            ]
          }
        },
        {
          "value": 0.00525000,
          "n": 2,
          "scriptPubKey": {
            "asm": "OP_DUP OP_HASH160 1558f83af264835ff900488a6d239be4a31be1ed OP_EQUALVERIFY OP_CHECKSIG",
            "hex": "76a9141558f83af264835ff900488a6d239be4a31be1ed88ac",
            "reqSigs": 1,
            "type": "pubkeyhash",
            "addresses": [
              "12wsmkPTh6SFYySAmbXabnftVykecHfrch"
            ]
          }
        },
        {
          "value": 0.00022593,
          "n": 3,
          "scriptPubKey": {
            "asm": "OP_HASH160 eff0ce59b1fd8a5d942b1bad7e8d85c8029b7624 OP_EQUAL",
            "hex": "a914eff0ce59b1fd8a5d942b1bad7e8d85c8029b762487",
            "reqSigs": 1,
            "type": "scripthash",
            "addresses": [
              "3PZhttXxA3ZZWzC3q66WNr8GeqXNutA1To"
            ]
          }
        },
        {
          "value": 0.00230000,
          "n": 4,
          "scriptPubKey": {
            "asm": "OP_HASH160 4e375344ad7839cec1dbc783609310b22634ac4c OP_EQUAL",
            "hex": "a9144e375344ad7839cec1dbc783609310b22634ac4c87",
            "reqSigs": 1,
            "type": "scripthash",
            "addresses": [
              "38pauaDL3gDL5sFZH8xPoodYvVGoagq1B6"
            ]
          }
        },
        {
          "value": 4.29053835,
          "n": 5,
          "scriptPubKey": {
            "asm": "OP_DUP OP_HASH160 7ddb236e7877d5040e2a59e4be544c65934e573a OP_EQUALVERIFY OP_CHECKSIG",
            "hex": "76a9147ddb236e7877d5040e2a59e4be544c65934e573a88ac",
            "reqSigs": 1,
            "type": "pubkeyhash",
            "addresses": [
              "1CUTyyxgbKvtCdoYmceQJCZLXCde5akiX2"
            ]
          }
        }
      ],
      "hex": "010000000194dc91ebf775f6aa7f9a66261b485ccd4f961d738b7e56c8cbdbd64b96fb96820a0000008a47304402200f39c3128648123c3e97b1609499bb9cb75f28c7e51110fdfe09b5e9c07fd19d02204ce16e193980969bb90feb80fae3b5d0ad0453416aeb97a01edc4e128895565f014104c4b7a7f7bb2c899f4aeab75b41567c040ae79506d43ee72f650c95b6319e47402f0ba88d1c5a294d075885442679dc24882ea37c31e0dbc82cfd51ed185d7e94ffffffff06002f0d000000000017a914241b7ad339c2f3c43bd5f34db630d69fa914848d876cc53100000000001976a914344921df9da453f9b9de4590302c5702e5dd865688acc8020800000000001976a9141558f83af264835ff900488a6d239be4a31be1ed88ac415800000000000017a914eff0ce59b1fd8a5d942b1bad7e8d85c8029b762487708203000000000017a9144e375344ad7839cec1dbc783609310b22634ac4c878bd79219000000001976a9147ddb236e7877d5040e2a59e4be544c65934e573a88ac00000000"
    },
   ...
   {
      "txid": "112ed40dfb9136511a30ffceaf15101d2a805ebcacdb7a7915d846d151aa661a",
      "hash": "112ed40dfb9136511a30ffceaf15101d2a805ebcacdb7a7915d846d151aa661a",
      "version": 1,
      "size": 189,
      "vsize": 189,
      "weight": 756,
      "locktime": 0,
      "vin": [
        {
          "txid": "09f02cd6ea426f1b346b80bd88f6fb680ee9accca875f2580d5635c9946464eb",
          "vout": 0,
          "scriptSig": {
            "asm": "304402202b6fa8ab5202515fddfbe915ca220639bc76be1d8c142194f2d0cdedf5e830a602207e9fc8477f02d65bfdc62b9a9385e46a4e8cdff4813537e87caba91990e59b1f[ALL] 035ebbcbd7778a980b66a47a6196691c39d9ef69a20491d9415daec3c1de5195f9",
            "hex": "47304402202b6fa8ab5202515fddfbe915ca220639bc76be1d8c142194f2d0cdedf5e830a602207e9fc8477f02d65bfdc62b9a9385e46a4e8cdff4813537e87caba91990e59b1f0121035ebbcbd7778a980b66a47a6196691c39d9ef69a20491d9415daec3c1de5195f9"
          },
          "sequence": 4294967295
        }
      ],
      "vout": [
        {
          "value": 0.00589600,
          "n": 0,
          "scriptPubKey": {
            "asm": "OP_HASH160 e7e1d4d5d7704c30fe317bf8016181175370206d OP_EQUAL",
            "hex": "a914e7e1d4d5d7704c30fe317bf8016181175370206d87",
            "reqSigs": 1,
            "type": "scripthash",
            "addresses": [
              "3Nq6Ytx5Lbvf7TwUz9zCjnTDekgaNWp4Tk"
            ]
          }
        }
      ],
      "hex": "0100000001eb646494c935560d58f275a8ccace90e68fbf688bd806b341b6f42ead62cf009000000006a47304402202b6fa8ab5202515fddfbe915ca220639bc76be1d8c142194f2d0cdedf5e830a602207e9fc8477f02d65bfdc62b9a9385e46a4e8cdff4813537e87caba91990e59b1f0121035ebbcbd7778a980b66a47a6196691c39d9ef69a20491d9415daec3c1de5195f9ffffffff0120ff08000000000017a914e7e1d4d5d7704c30fe317bf8016181175370206d8700000000"
    }
  ],
  "time": 1612798475,
  "mediantime": 1612795492,
  "nonce": 3178414745,
  "bits": "170d21b9",
  "difficulty": 21434395961348.92,
  "chainwork": "0000000000000000000000000000000000000000192ae9c64cff6db7c9dcb30b",
  "nTx": 3043,
  "previousblockhash": "0000000000000000000c343308b3093403c6f28107139f49d306e9dd85aed438",
  "nextblockhash": "000000000000000000083fba49c903b65ecb0636cc229e8f5c6c4df9d8d7e1d0"
}

```

# raw
## get_raw_transaction
This function can't work if you did not set 'tindex=1' when you run bitcoind <br/>
**Inputs**:
```
"tx_id":"f68394a5fa08907fbdd049401a4da25b10bd57f9301822747a23830fe328de6e"
```
**Example**
```
rt = bitcoin.raw.get_raw_transaction("f68394a5fa08907fbdd049401a4da25b10bd57f9301822747a23830fe328de6e")
print(rt)
```
**Outputs**:
```
"020000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff1f0386520a0484c35e6062696e616e63652f626a4629220e4781290000000000ffffffff020e9db926000000001600143156afc4249915008020f932783319f3e610b97d0000000000000000266a24aa21a9ed50ab3dbcc26ab26a587dddf4b98d93036e0cfd52c141eae7983775aa534f51820120000000000000000000000000000000000000000000000000000000000000000000000000"
```

## decode_raw_transaction
**Inputs**:
```
"rt":"020000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff1f0386520a0484c35e6062696e616e63652f626a4629220e4781290000000000ffffffff020e9db926000000001600143156afc4249915008020f932783319f3e610b97d0000000000000000266a24aa21a9ed50ab3dbcc26ab26a587dddf4b98d93036e0cfd52c141eae7983775aa534f51820120000000000000000000000000000000000000000000000000000000000000000000000000"
```
**Example**
```
tran = bitcoin.raw.decode_raw_transaction("020000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff1f0386520a0484c35e6062696e616e63652f626a4629220e4781290000000000ffffffff020e9db926000000001600143156afc4249915008020f932783319f3e610b97d0000000000000000266a24aa21a9ed50ab3dbcc26ab26a587dddf4b98d93036e0cfd52c141eae7983775aa534f51820120000000000000000000000000000000000000000000000000000000000000000000000000")
print(tran)
```
**Outputs**:
```
{
  'txid': 'f68394a5fa08907fbdd049401a4da25b10bd57f9301822747a23830fe328de6e',
  'hash': '2972ad7373d1dfcb074be84b96f3da0632993feb52b00a645fc7d137ce8b9414',
  'version': 2,
  'size': 196,
  'vsize': 169,
  'weight': 676,
  'locktime': 0,
  'vin': [
    {
      'coinbase': '0386520a0484c35e6062696e616e63652f626a4629220e4781290000000000',
      'txinwitness': [
        '0000000000000000000000000000000000000000000000000000000000000000'
      ],
      'sequence': 4294967295
    }
  ],
  'vout': [
    {
      'value': 6.49698574,
      'n': 0,
      'scriptPubKey': {
        'asm': '0 3156afc4249915008020f932783319f3e610b97d',
        'hex': '00143156afc4249915008020f932783319f3e610b97d',
        'reqSigs': 1,
        'type': 'witness_v0_keyhash',
        'addresses': [
          'bc1qx9t2l3pyny2spqpqlye8svce70nppwtaxwdrp4'
        ]
      }
    },
    {
      'value': 0.0,
      'n': 1,
      'scriptPubKey': {
        'asm': 'OP_RETURN aa21a9ed50ab3dbcc26ab26a587dddf4b98d93036e0cfd52c141eae7983775aa534f5182',
        'hex': '6a24aa21a9ed50ab3dbcc26ab26a587dddf4b98d93036e0cfd52c141eae7983775aa534f5182',
        'type': 'nulldata'
      }
    }
  ]
}
```

# wallet
The wallet will be automatically loaded after created, do not load it again
## create_wallet
**Inputs**:
```
{
    "name":"nice"
}
```
**Example**
```
wa = bitcoin.wallet.create_wallet("nice")
print(wa)
```
**Outputs**:
```
{
  'name': 'nice',
  'warning': 'Empty string given as passphrase, wallet will not be encrypted.'
}
```

## load_wallet
The wallet needs to be reloaded after the bitcoind node restarts <br/>
**Inputs**:
```
{
    "wallet":"nice"
}
```
**Example**
```
wa = bitcoin.wallet.load_wallet("nice")
print(wa)
```
**Outputs**:
```
{
    'name': 'nice', 
    'warning': ''
}
```

## list_wallets
**Inputs**:
```None```
**Example**
```
wallets = bitcoin.wallet.list_wallets()
print(wa)
```
**Outputs**:
```['nice', 'firstwallet']```

## encrypt_wallet
**Inputs**:
```
{
    "wallet":"nice",
    "pass_phrase":"qwe123"    
}
```
**Example**
```
res = bitcoin.wallet.encrypt_wallet("nice","qwe123")
print(res)
```
**Outputs**:
```
wallet encrypted; The keypool has been flushed and a new HD seed was generated (if you are using HD). You need to make a new backup.
```

## wallet_pass_phrase
Unlock the wallet after transaction or sign in 'timeout' seconds <br/>
**Inputs**:
```
{
    "wallet":"nice",
    "pass_phrase":"qwe123"
    "timeout": default 10    
}
```
**Example**
```
bitcoin.wallet.wallet_pass_phrase("nice","qwe123")
```
**Outputs**:
```None```


## wallet_lock
Lock the wallet <br/>
**Inputs**:
```
{
  "wallet":"nice"
}
```
**Example**
```
bitcoin.wallet.wallet_lock("nice")
```
**Outputs**:


## get_new_address
**Inputs**:
```
{
    "wallet":"nice",
    "label":"wow"
}
```
**Example**
```
address = bitcoin.wallet.get_new_address("nice","wow")
print(address)
```
**Outputs**:
```
"1PXjDKw3PeDLqfFYok5bdQMnP2F1AxqmPT"
```

## get_balance
**Inputs**:
```
{
    "wallet":"nice"
}
```
**Example**
```
balance = bitcoin.wallet.get_balance("nice")
print(balance)
```
**Outputs**:
```
0.0
```

## list_received_by_address
**Inputs**:
```
{
    "wallet":"nice"
    "include_empty":True
}
```
**Example**
```
res = bitcoin.wallet.list_received_by_address("nice",include_empty=True)
print(res)
```
**Outputs**:
```
[
  {
    'address': '1k679FsMRJfUQeTh4txPF35v39NaRNse3',
    'amount': 0.0,
    'confirmations': 0,
    'label': 'go',
    'txids': []
  },
  {
    'address': '14csDNFKwkzAJK3Jkk5QWj37NiV6eZ4P17',
    'amount': 0.0,
    'confirmations': 0,
    'label': 'like',
    'txids': []
  }
]
```

## list_received_by_label
**Inputs**:
```
{
    "wallet":"nice"
    "include_empty":True
}
```
**Example**
```
res = bitcoin.wallet.list_received_by_label("firstwallet",include_empty=True)
print(res)
```
**Outputs**:
```
[
  {
    'amount': 0.0,
    'confirmations': 0,
    'label': ''
  },
  {
    'amount': 0.0,
    'confirmations': 0,
    'label': 'go'
  },
  {
    'amount': 0.0,
    'confirmations': 0,
    'label': 'like'
  },
  {
    'amount': 0.0,
    'confirmations': 0,
    'label': 'nice'
  }
]
```
# utils
## validate_address
Validate input address, return True if address is legal <br/>
**Inputs**
```
  {'address':'34wcANsazFutEiTegvsYUCZz5NDmsLg9Jh'}
```
**Example**
```angular2html
  res = bitcoin.utils.validate_address("34wcANsazFutEiTegvsYUCZz5NDmsLg9Jh")
  print(res)
```
**Outputs**
```angular2html
    True
```

# Tips
- The default parameters of these functions are not specified in the document, you need to check the source code by yourself.
- The current document is incomplete, I will gradually improve the document later.