from typing import Any, Union
import os
import requests
import itertools
from btc.encoding import FriendlyCode
from btc.types_btc import RPCEndpoint


class JSONBaseProvider:
    def __init__(self) -> None:
        self.request_counter = itertools.count()

    def decode_rpc_response(self, raw_response):
        resp = FriendlyCode().json_decode(raw_response.text)
        error = resp.get("error")
        if error is None:
            res = resp.get("result")
            return res
        else:
            raise Exception(error)

    def encode_rpc_request(self, method: RPCEndpoint, params: Any):
        rpc_dict = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        }
        return rpc_dict


class HttpProvider(JSONBaseProvider):
    """
        An HTTP Provider for API request
        :param endpoint_uri: HTTP API URL base. Default value is ``"http://127.0.0.1:8332"``. Can also be configured via the ``BITCOIN_LOTUS_HTTP_PROVIDER_URI`` environment variable.
        :return:
    """

    def __init__(self, rpcuser: str, rpcpassword: str, endpoint_uri: Union[str, dict] = None,
                 ):
        super(HttpProvider, self).__init__()
        if endpoint_uri is None:
            self.endpoint_uri = os.environ.get("BITCOIN_HTTP_PROVIDER_URI", "http://127.0.0.1:8332")
        elif isinstance(endpoint_uri, (str,)):
            self.endpoint_uri = endpoint_uri
        else:
            raise TypeError("unknown endpoint uri {}".format(endpoint_uri))

        self.sess = requests.session()
        self.sess.headers = {
            "Content-Type": "application/json"
        }
        self.auth = (rpcuser, rpcpassword)

        """Request timeout in second."""

    def make_request(self, method: RPCEndpoint, params: Any = None, rpcwallet: str = None, timeout: int = 10) -> Any:
        json_dict = self.encode_rpc_request(method, params)
        if rpcwallet:
            uri = self.endpoint_uri + "/wallet/" + rpcwallet
        else:
            uri = self.endpoint_uri
        resp = self.sess.post(uri, json=json_dict, timeout=timeout,
                              auth=self.auth)
        res = self.decode_rpc_response(resp)
        return res
