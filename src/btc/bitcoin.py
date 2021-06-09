from btc.providers import HttpProvider
from btc.chain import Chain
from btc.wallet import Wallet
from btc.raw_transaction import Raw
from btc.utils import Utils

"""
reference:  https://developer.bitcoin.org/reference/rpc/
"""

class BitCoin:
    HttpProvider = HttpProvider

    def __init__(self, provider: HttpProvider):
        self.provider = provider
        self._wallet = Wallet(self)
        self._chain = Chain(self)
        self._raw = Raw(self)
        self._utils = Utils(self)

    @property
    def wallet(self):
        return self._wallet

    @property
    def chain(self):
        return self._chain

    @property
    def raw(self):
        return self._raw

    @property
    def utils(self):
        return self._utils


