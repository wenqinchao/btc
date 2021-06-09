from btc.rpc_abi import RPC


class Utils:

    def __init__(self, bitcoin):
        self._bitcoin = bitcoin
        self._provider = bitcoin.provider

    def validate_address(self, address: str) -> bool:
        res = self._provider.make_request(RPC.util_validateAddress, [address])
        return res.get("isvalid")
