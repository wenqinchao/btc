from btc.rpc_abi import RPC


class Raw:
    def __init__(self, bitcoin):
        self._bitcoin = bitcoin
        self._provider = bitcoin.provider

    def get_raw_transaction(self, tx_id: str) -> str:
        """
        Return the raw transaction data.
        :param tx_id:
        :return:
        """
        return self._provider.make_request(RPC.raw_getRawTransaction, [tx_id])

    def decode_raw_transaction(self, tran_info_hex: str) -> dict:
        """
        Return a JSON object representing the serialized, hex-encoded transaction.
        :param tran_info_hex
        :return
        """
        return self._provider.make_request(RPC.raw_decodeRawTransaction, [tran_info_hex])

    def create_raw_transaction(self, inputs: list, outputs: list, lock_time: int = 0, replaceable: bool = False):
        """
        Create a transaction spending the given inputs and creating new outputs.
        Outputs can be addresses or data.
        :param inputs:
        :param outputs:
        :param lock_time:
        :param replaceable:
        :return:
        """
        return self._provider.make_request(RPC.raw_createRawTransaction, [inputs, outputs, lock_time, replaceable])

    def fund_raw_transaction(self, hex_string: str, *args):
        """
        Add inputs to a transaction until it has enough in value to meet its out value.
        :param hex_string: The hex string of the raw transaction
        :param args:
        :return:
        """
        return self._provider.make_request(RPC.raw_fundRawTransaction, [hex_string, *args])

    def combine_raw_transaction(self, transactions: [str]) -> str:
        """
        Combine multiple partially signed transactions into one transaction.
        :param transactions:
        :return:
        """
        return self._provider.make_request(RPC.raw_combineRawTransaction, transactions)

    def send_raw_transaction(self, hex_string: str, allow_high_fees: bool = False):
        """
        Submits raw transaction (serialized, hex-encoded) to local node and network.
        :param hex_string: The hex string of the raw transaction
        :param allow_high_fees
        :return:
        """
        return self._provider.make_request(RPC.raw_sendRawTransaction, [hex_string, allow_high_fees])

    def sign_raw_transaction(self, hex_string: str, private_keys: list, prev_txs: list, sign_hash_type: str = "ALL"):
        """
        Sign inputs for raw transaction (serialized, hex-encoded).
        :param hex_string: The transaction hex string
        :param private_keys: A json array of base58-encoded private keys for signing
        :param prev_txs: A json array of previous dependent transaction outputs
        :param sign_hash_type: The signature hash type. Must be one of: “ALL” “NONE” “SINGLE” “ALL|ANYONECANPAY” “NONE|ANYONECANPAY” “SINGLE|ANYONECANPAY”
        :return:
        """
        return self._provider.make_request(RPC.raw_signRawTransaction,
                                           [hex_string, private_keys, prev_txs, sign_hash_type])

    def analyze_psbt(self, psbt: str) -> dict:
        """
        Analyzes and provides information about the current status of a PSBT and its inputs
        :param psbt:
        :return:
        """
        return self._provider.make_request(RPC.raw_analyzePsbt, psbt)

    def combine_psbt(self, psbts: list):
        """
        Combine multiple partially signed Bitcoin transactions into one transaction.
        :param psbts:
        :return:
        """
        return self._provider.make_request(RPC.raw_combinePsbt, psbts)

    def convert_to_psbt(self, tran_info_hex: str, permit_sig_data: bool = False, is_witness: bool = False):
        """
        Converts a network serialized transaction to a PSBT. This should be used only with createrawtransaction and fundrawtransaction createpsbt and walletcreatefundedpsbt should be used for new applications
        :param tran_info_hex:The hex string of a raw transaction
        :param permit_sig_data:
        :param is_witness:
        :return:
        """
        return self._provider.make_request(RPC.raw_convertToPsbt, [tran_info_hex, permit_sig_data, is_witness])

    def create_psbt(self, inputs: list, outputs: list, lock_time: int = 0, replaceable: bool = False):
        """
        Creates a transaction in the Partially Signed Transaction format.
        :param inputs:
        :param outputs:
        :param lock_time:
        :param replaceable:
        :return:
        """
        return self._provider.make_request(RPC.raw_createPsbt, [inputs, outputs, lock_time, replaceable])

    def decode_psbt(self, psbt):
        """
        Return a JSON object representing the serialized, base64-encoded partially signed Bitcoin transaction.
        :param psbt:
        :return:
        """
        return self._provider.make_request(RPC.raw_decodePsbt, [psbt])

    def finalize_psbt(self, psbt):
        """
        Finalize the inputs of a PSBT. If the transaction is fully signed, it will produce a network serialized
        transaction which can be broadcast with sendrawtransaction. Otherwise a PSBT will be created which has
        the final_scriptSig and final_scriptWitness fields filled for inputs that are complete.
        :param psbt:
        :return:
        """
        return self._provider.make_request(RPC.raw_finalizePsbt, [psbt])

    def join_psbts(self, psbts: list):
        """
        Joins multiple distinct PSBTs with different inputs and outputs into one PSBT with inputs and outputs
        from all of the PSBTs No input in any of the PSBTs can be in more than one of the PSBTs.
        :param psbts:
        :return:
        """
        return self._provider.make_request(RPC.raw_joinPsbts, psbts)

    def utxo_update_psbt(self, psbt):
        """
        Updates a PSBT with witness UTXOs retrieved from the UTXO set or the mempool.
        :param psbt:
        :return:
        """
        return self._provider.make_request(RPC.raw_utxoUpdatePsbt, [psbt])
