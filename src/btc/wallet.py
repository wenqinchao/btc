from btc.rpc_abi import RPC

class Wallet:
    """
    Some wallet function can't work before wallet loading, please ensure your wallet is loaded,
    you can check whether your wallet is loaded via list_wallets function. If your wallet is encrypted,
    please unlock your wallet via wallet_pass_phrase first
    """

    def __init__(self, bitcoin):
        self._bitcoin = bitcoin
        self._provider = bitcoin.provider

    def bump_fee(self, tx_id: str) -> dict:
        """
        Bumps the fee of an opt-in-RBF transaction T, replacing it with a new transaction B.
        :param tx_id:
        :return:
        """
        return self._provider.make_request(RPC.wallet_bumpFee, [tx_id])

    def create_wallet(self, name: str, disable_private_keys: bool = False, blank: bool = False, passphrase: str = "",
                      avoid_reuse: bool = False, descriptors: bool = False, load_on_startup: bool = None):
        """
        Create a wallet
        :param name:
        :param disable_private_keys:
        :param blank:
        :param passphrase:
        :param avoid_reuse:
        :param descriptors:
        :param load_on_startup:
        :return:
        """
        return self._provider.make_request(RPC.wallet_createWallet,
                                           [name, disable_private_keys, blank, passphrase, avoid_reuse, descriptors,
                                            load_on_startup])

    def load_wallet(self, wallet: str):
        """
        Load a wallet
        :param wallet:
        :return:
        """
        return self._provider.make_request(RPC.wallet_loadWallet, [wallet], None, 180)

    def dump_wallet(self, wallet: str, filename: str) -> str:
        """
        Dumps all wallet keys in a human-readable format to a server-side file. This does not allow overwriting existing files.
        :param filename:
        :param wallet
        :return: Absolute path of dumpfile
        """
        resp = self._provider.make_request(RPC.wallet_dumpWallet, [filename], wallet)
        return resp.get("filename")

    def import_wallet(self, wallet: str, filename: str):
        """
        Imports keys from a wallet dump file (see dump_wallet). Requires a new wallet backup to include imported keys.
        :param filename: Absolute path
        :param wallet:
        :return:
        """
        self._provider.make_request(RPC.wallet_importWallet, [filename], wallet, 180)

    def list_wallets(self) -> list:
        """
        List all wallets
        :return: wallet name list
        """
        return self._provider.make_request(RPC.wallet_listWallets)

    def list_wallet_dir(self):
        """
        Returns a list of wallets in the wallet directory
        :param wallet:
        :return:
        """
        return self._provider.make_request(RPC.wallet_listWalletDir)

    def backup_wallet(self, wallet: str, destination: str):
        """
        Safely copies current wallet file to destination, which can be a directory or a path with filename
        :param destination:
        :param wallet
        :return:
        """
        return self._provider.make_request(RPC.wallet_backupWallet, [destination], wallet)

    def unload_wallet(self, wallet: str):
        """
        Unloads the wallet referenced by the request endpoint otherwise unloads the wallet specified in the argument.
        Specifying the wallet name on a wallet endpoint is invalid.
        :param wallet: The name of the wallet to unload.
        :return:
        """
        return self._provider.make_request(RPC.wallet_unloadWallet, [], wallet)

    def encrypt_wallet(self, wallet: str, pass_phrase: str):
        """
        Encrypts the wallet with ‘passphrase’. This is for first time encryption.
        After this, any calls that interact with private keys such as sending or
        signing will require the passphrase to be set prior the making these calls.
        Use the walletpassphrase call for this, and then walletlock call.
        If the wallet is already encrypted, use the wallet_passphrase_change call.
        :param pass_phrase:
        :param wallet:
        :return:
        """
        return self._provider.make_request(RPC.wallet_encryptWallet, [pass_phrase], wallet)

    def wallet_pass_phrase(self, wallet: str, pass_phrase: str, timeout: int = 10):
        """
        Stores the wallet decryption key in memory for ‘timeout’ seconds.
        This is needed prior to performing transactions related to private keys such as sending bitcoins
        :param pass_phrase:
        :param wallet
        :param timeout:
        :return:
        """
        return self._provider.make_request(RPC.wallet_passPhrase, [pass_phrase, timeout], wallet)

    def abandon_transaction(self, tx_id: str):
        """
        Mark in-wallet transaction <txid> as abandoned This will mark this transaction and all its in-wallet
        descendants as abandoned which will allow for their inputs to be respent. It can be used to replace “stuck”
        or evicted transactions.
        It only works on transactions which are not included in a block and are not currently in the mempool.
        It has no effect on transactions which are already abandoned
        :param tx_id:
        :return:
        """
        return self._provider.make_request(RPC.wallet_abandonTransaction, [tx_id])

    def abort_rescan(self):
        """
        Stops current wallet rescan triggered by an RPC call, e.g. by an importprivkey call.
        :return:
        """
        return self._provider.make_request(RPC.wallet_abortScan, [])

    def add_multi_sig_address(self, n_required: int, keys: list):
        """
        Add a nrequired-to-sign multisignature address to the wallet. Requires a new wallet backup.
        :param n_required: The number of required signatures out of the n keys or addresses
        :param keys: A json array of bitcoin addresses or hex-encoded public keys
        :return:
        """
        return self._provider.make_request(RPC.wallet_addMultiSigAddress, [n_required, keys])

    def dump_private_key(self, wallet: str, address: str):
        """
        Reveals the private key corresponding to ‘address’.Then the importprivkey can be used with this output
        :param address:
        :param wallet
        :return:
        """
        return self._provider.make_request(RPC.wallet_dumpPrivateKey, [address], wallet)

    def get_address_by_label(self, wallet: str, label: str):
        """
        Returns the list of addresses assigned the specified label
        :param label:
        :param wallet:
        :return:
        """
        return self._provider.make_request(RPC.wallet_getAddressByLabel, [label], wallet)

    def get_address_info(self, wallet: str, address: str):
        """
        Return information about the given bitcoin address. Some information requires the address to be in the wallet
        :param address:
        :param wallet: Wallet name
        :return:
        """
        return self._provider.make_request(RPC.wallet_getAddressInfo, [address], wallet)

    def get_balance(self, wallet: str, dummy: str = "*", min_conf: int = 0, include_watch_only: bool = False):
        """
        Returns the total available balance. The available balance is what the wallet considers currently spendable,
         and is thus affected by options which limit spendability such as -spendzeroconfchange.
        :param wallet: Wallet name
        :param dummy: Remains for backward compatibility. Must be excluded or set to “*”.
        :param min_conf: Only include transactions confirmed at least this many times
        :param include_watch_only: Also include balance in watch-only addresses (see ‘importaddress’)
        :return:
        """
        return self._provider.make_request(RPC.wallet_getBalance, [dummy, min_conf, include_watch_only], wallet)

    def get_new_address(self, wallet: str, label: str = "", address_type: str = "legacy"):
        """
        Returns a new Bitcoin address for receiving payments.
        :param wallet: Wallet name
        :param label: The label name for the address to be linked to. It can also be set to the empty string “” to represent the default label.
        :param address_type:The address type to use. Options are “legacy”, “p2sh-segwit”, and “bech32”
        :return:
        """
        return self._provider.make_request(RPC.wallet_getNewAddress, [label, address_type], wallet)

    def get_raw_change_address(self, wallet: str, address_type: str = "legacy"):
        """
        Returns a new Bitcoin address, for receiving change. This is for use with raw transactions, NOT normal use
        :param wallet: Wallet name
        :param address_type: The address type to use. Options are “legacy”, “p2sh-segwit”, and “bech32”
        :return:
        """
        return self._provider.make_request(RPC.wallet_getRawChangeAddress, [address_type], wallet)

    def get_received_by_address(self, wallet: str, address: str, min_conf: int = 1):
        """
        Returns the total amount received by the given address in transactions with at least minconf confirmations.
        :param wallet: Wallet name
        :param address:
        :param min_conf: Only include transactions confirmed at least this many times
        :return:
        """
        return self._provider.make_request(RPC.wallet_getReceivedByAddress, [address, min_conf], wallet)

    def get_received_by_label(self, wallet: str, label: str, min_conf: int = 1):
        """
        Returns the total amount received by addresses with <label> in transactions with at least [minconf] confirmations.
        :param wallet:
        :param label: The selected label, may be the default label using “”.
        :param min_conf: Only include transactions confirmed at least this many times
        :return:
        """
        return self._provider.make_request(RPC.wallet_getReceivedByLabel, [label, min_conf], wallet)

    def get_transaction(self, wallet: str, tx_id: str, include_watch_only: str = False):
        """
        Get detailed information about in-wallet transaction <txid>
        :param wallet:
        :param tx_id: The transaction id
        :param include_watch_only: Whether to include watch-only addresses in balance calculation and details[]
        :return:
        """
        return self._provider.make_request(RPC.wallet_getTransaction, [tx_id, include_watch_only], wallet)

    def get_wallet_info(self, wallet: str):
        """
        Returns an object containing various wallet state info
        :param wallet:
        :return:
        """
        return self._provider.make_request(RPC.wallet_getWalletInfo, [], wallet)

    def import_address(self, wallet: str, address: str, label: str = "", rescan: bool = False, p2sh: bool = False):
        """
        Adds an address or script (in hex) that can be watched as if it were in your wallet but cannot
        be used to spend. Requires a new wallet backup.
        :param wallet:
        :param address: The Bitcoin address (or hex-encoded script)
        :param label: An optional label
        :param rescan: Rescan the wallet for transactions
        :param p2sh: Add the P2SH version of the script as well
        :return:
        """
        return self._provider.make_request(RPC.wallet_importAddress, [address, label, rescan, p2sh], wallet)

    def import_multi(self, wallet: str, requests: list, options: dict):
        """
        Import addresses/scripts (with private or public keys, redeem script (P2SH)), optionally rescanning the blockchain
        from the earliest creation time of the imported scripts. Requires a new wallet backup.
        :param wallet:
        :param requests:
        :param options:
        :return:
        """
        return self._provider.make_request(RPC.wallet_importMulti, [requests, options], wallet)

    def import_private_key(self, wallet: str, private_key: str, label: str = "", rescan: bool = False):
        """
        Adds a private key (as returned by dumpprivkey) to your wallet. Requires a new wallet backup.
        :param wallet:
        :param private_key:
        :param label:
        :param rescan:
        :return:
        """
        return self._provider.make_request(RPC.wallet_importPrivateKey, [private_key, label, rescan], wallet)

    def import_pruned_funds(self, raw_transaction: str, tx_out_proof: str):
        """
        Imports funds without rescan. Corresponding address or script must previously be included in wallet.
        :param raw_transaction: A raw transaction in hex funding an already-existing address in wallet
        :param tx_out_proof: The hex output from get_tx_out_proof that contains the transaction
        :return:
        """
        return self._provider.make_request(RPC.wallet_importPrunedFunds, [raw_transaction, tx_out_proof])

    def import_public_key(self, wallet: str, public_key: str, label: str = "", rescan: bool = False):
        """
        Adds a public key (in hex) that can be watched as if it were in your wallet but cannot be used to spend. Requires a new wallet backup.
        :param wallet:
        :param public_key: The hex-encoded public key
        :param label: An optional label
        :param rescan: Rescan the wallet for transactions
        :return:
        """
        return self._provider.make_request(RPC.wallet_importPublicKey, [public_key, label, rescan], wallet)

    def key_pool_refill(self, new_size: int = 100):
        """
        Fills the key pool
        :param new_size: The new key pool size
        :return:
        """
        return self._provider.make_request(RPC.wallet_keyPoolRefill, [new_size])

    def list_address_groups(self, wallet: str):
        """
        Lists groups of addresses which have had their common ownership made public by common use
        as inputs or as the resulting change in past transactions
        :param wallet:
        :return:
        """
        return self._provider.make_request(RPC.wallet_listAddressGroupings, [], wallet)

    def list_labels(self, wallet: str):
        """
        Returns the list of all labels, or labels that are assigned to addresses with a specific purpose
        :param wallet:
        :return:
        """
        return self._provider.make_request(RPC.wallet_listLabels, [], wallet)

    def list_received_by_address(self, wallet: str, min_conf: int = 1, include_empty: bool = False,
                                 include_watch_only: bool = False, address_filter: str = None):
        """
        List balances by receiving address
        :param wallet:
        :param min_conf: The minimum number of confirmations before payments are included.
        :param include_empty: Whether to include addresses that haven’t received any payments.
        :param include_watch_only: Whether to include watch-only addresses (see ‘importaddress’).
        :param address_filter: If present, only return information on this address
        :return:
        """
        params = [min_conf, include_empty, include_watch_only]
        if address_filter:
            params.append(address_filter)
        return self._provider.make_request(RPC.wallet_listReceivedByAddress,
                                           params, wallet)

    def list_received_by_label(self, wallet: str, min_conf: int = 1, include_empty: bool = False,
                               include_watch_only: bool = False):
        """
        List received transactions by label
        :param wallet:
        :param min_conf: The minimum number of confirmations before payments are included.
        :param include_empty: Whether to include labels that haven’t received any payments
        :param include_watch_only: Whether to include watch-only addresses (see ‘importaddress’).
        :return:
        """

        return self._provider.make_request(RPC.wallet_listReceivedByLabel,
                                           [min_conf, include_empty, include_watch_only], wallet)

    def list_since_block(self, wallet: str, block_hash: str = None, target_confirmations: int = 1,
                         include_watch_only: bool = False, include_removed: bool = False):
        """
        Get all transactions in blocks since block [blockhash], or all transactions if omitted.
        :param wallet:
        :param block_hash: If set, the block hash to list transactions since, otherwise list all transactions.
        :param target_confirmations: Return the nth block hash from the main chain. e.g. 1 would mean the best block hash
        :param include_watch_only: Include transactions to watch-only addresses (see ‘importaddress’)
        :param include_removed: Show transactions that were removed due to a reorg in the “removed” array
        :return:
        """
        return self._provider.make_request(RPC.wallet_listSinceBlock,
                                           [block_hash, target_confirmations, include_watch_only, include_removed],
                                           wallet)

    def list_transactions(self, wallet: str, label: str = "*", count: int = 10, skip: int = 0,
                          include_watch_only: bool = False):
        """
        If a label name is provided, this will return only incoming transactions paying to addresses with the specified label.
        Returns up to ‘count’ most recent transactions skipping the first ‘from’ transactions
        :param wallet:
        :param label: If set, should be a valid label name to return only incoming transactions with the specified label, or “*” to disable filtering and return all transactions
        :param count: The number of transactions to return
        :param skip: The number of transactions to skip
        :param include_watch_only: Include transactions to watch-only addresses (see ‘importaddress’)
        :return:
        """
        return self._provider.make_request(RPC.wallet_listTransactions, [label, count, skip, include_watch_only],
                                           wallet)

    def list_unspent(self, wallet: str, min_conf: int = 1, max_conf: int = 9999999, addresses: list = [],
                     include_unsafe: bool = True, query_options: dict = None):
        """
        Returns array of unspent transaction outputs with between minconf and maxconf (inclusive) confirmations.
        Optionally filter to only include txouts paid to specified addresses
        :param wallet:
        :param min_conf: The minimum confirmations to filter
        :param max_conf: The maximum confirmations to filter
        :param addresses: A json array of bitcoin addresses to filter
        :param include_unsafe: Include outputs that are not safe to spend See description of “safe” attribute below.
        :param query_options: JSON with query options
        :return:
        """
        return self._provider.make_request(RPC.wallet_listUnspent,
                                           [min_conf, max_conf, addresses, include_unsafe, query_options], wallet)

    def list_lock_unspent(self, wallet: str, unlock: bool, transactions: list = []):
        """
        Updates list of temporarily unspendable outputs.
        :param wallet:
        :param unlock: Whether to unlock (true) or lock (false) the specified transactions
        :param transactions: A json array of objects. Each object the txid (string) vout (numeric).
        :return:
        """
        return self._provider.make_request(RPC.wallet_lockUnspent, [unlock, transactions], wallet)

    def remove_pruned_funds(self, wallet: str, tx_id: str):
        """
        Deletes the specified transaction from the wallet. Meant for use with pruned wallets and as a companion to importprunedfunds.
        This will affect wallet balances.
        :param wallet:
        :param tx_id: The hex-encoded id of the transaction you are deleting
        :return:
        """
        return self._provider.make_request(RPC.wallet_removePrunedFunds, [tx_id], wallet)

    def rescan_blockchain(self, wallet: str, start_height: int = 0, stop_height: int = None):
        """
        Rescan the local blockchain for wallet related transactions.
        :param wallet:
        :param start_height: block height where the rescan should start
        :param stop_height: the last block height that should be scanned. If none is provided it will rescan up to the tip at return time of this call
        :return:
        """
        return self._provider.make_request(RPC.wallet_rescanBlockChain, [start_height, stop_height], wallet)

    def send_many(self, wallet: str, dummpy: str, amounts: dict, min_conf: int = 1, comment: str = None,
                  subtract_fee_from: list = None, replace_able: bool = None, conf_target: int = None,
                  estimate_mode: str = "UNSET"):
        """
        Send multiple times. Amounts are double-precision floating point numbers.
        :param wallet:
        :param dummpy: Must be set to “” for backwards compatibility
        :param amounts: A json object with addresses and amounts
        :param min_conf: Only use the balance confirmed at least this many times.
        :param comment: A comment
        :param subtract_fee_from: The fee will be equally deducted from the amount of each selected address. Those recipients will receive less bitcoins than you enter in their corresponding amount field. If no addresses are specified here, the sender pays the fee
        :param replace_able: optional, default=fallback to wallet’s default. Allow this transaction to be replaced by a transaction with higher fees via BIP 125
        :param conf_target: numeric, optional, default=fallback to wallet’s default. Confirmation target (in blocks)
        :param estimate_mode: The fee estimate mode, must be one of: UNSET” “ECONOMICAL” “CONSERVATIVE”
        :return:
        """

        return self._provider.make_request(RPC.wallet_sendMany,
                                           [dummpy, amounts, min_conf, comment, subtract_fee_from, replace_able,
                                            conf_target, estimate_mode], wallet)

    def send_to_address(self, wallet: str, address: str, amount: float, comment: str = None, comment_to: str = None,
                        subtract_fee_from_amount: bool = False, replace_able: bool = True, conf_target: bool = None,
                        estimate_mode: str = "UNSET"):
        """
        Send an amount to a given address.
        :param wallet:
        :param address: The bitcoin address to send to.
        :param amount: The amount in BTC to send. eg 0.1
        :param comment: A comment used to store what the transaction is for.
        :param comment_to:  A comment to store the name of the person or organization
        :param subtract_fee_from_amount: The fee will be deducted from the amount being sent.
        :param replace_able: Allow this transaction to be replaced by a transaction with higher fees via BIP 125
        :param conf_target:
        :param estimate_mode:
        :return:
        """

        return self._provider.make_request(RPC.wallet_sendToAddress,
                                           [address, amount, comment, comment_to, subtract_fee_from_amount,
                                            replace_able, conf_target, estimate_mode], wallet)

    def set_label(self, wallet: str, address: str, label: str):
        """
        Sets the label associated with the given address.
        :param wallet:
        :param address:
        :param label:
        :return:
        """
        self._provider.make_request(RPC.wallet_setLabel, [address, label], wallet)

    def set_tx_fee(self, wallet: str, amount: float):
        """
        Set the transaction fee per kB for this wallet. Overrides the global -paytxfee command line parameter.
        :param wallet:
        :param amount: The transaction fee in BTC/kB
        :return:
        """
        return self._provider.make_request(RPC.wallet_setTxFee, [amount], wallet)

    def sign_message(self, wallet: str, address: str, message: str):
        """
        Sign a message with the private key of an address
        :param wallet:
        :param address: The bitcoin address to use for the private key
        :param message: The message to create a signature of.
        :return:
        """
        return self._provider.make_request(RPC.wallet_signMessage, [address, message], wallet)

    def sign_raw_transaction_with_wallet(self, wallet: str, hex_string: str, pre_txs: list):
        """
        Sign inputs for raw transaction (serialized, hex-encoded).
        :param wallet:
        :param hex_string: The transaction hex string
        :param pre_txs: A json array of previous dependent transaction outputs
        :return:
        """
        return self._provider.make_request(RPC.wallet_signRawTransactionWithWallet, [hex_string, pre_txs], wallet)

    def wallet_create_funded_psbt(self, wallet: str, inputs: list, outputs: list, lock_time: int = 0,
                                  options: dict = None,
                                  bip32derivs: bool = False):
        """
        Creates and funds a transaction in the Partially Signed Transaction format.
        Inputs will be added if supplied inputs are not enough Implements the Creator and Updater roles.
        :param wallet
        :param inputs: A json array of json objects
        :param outputs: a json array with outputs (key-value pairs), where none of the keys are duplicated.
        :param lock_time:
        :param options: If true, includes the BIP 32 derivation paths for public keys if we know them
        :return:
        """
        return self._provider.make_request(RPC.wallet_walletCreateFundedPsbt,
                                           [inputs, outputs, lock_time, options, bip32derivs], wallet)

    def wallet_lock(self, wallet: str):
        """
        Removes the wallet encryption key from memory, locking the wallet.
        :param wallet:
        :return:
        """
        return self._provider.make_request(RPC.wallet_walletUnlock, [], wallet)

    def wallet_pass_phrase_change(self, wallet: str, old_phrase: str, new_phrase: str):
        """
        Changes the wallet passphrase
        :param wallet:
        :param old_phrase:
        :param new_phrase:
        :return:
        """
        return self._provider.make_request(RPC.wallet_passPhraseChange, [old_phrase, new_phrase], wallet)

    def wallet_process_psbt(self, wallet: str, psbt: str, sign: bool = True, sig_hash_type: str = "ALL",
                            bip32_derives: bool = False):
        """
        Update a PSBT with input information from our wallet and then sign inputs that we can sign for.
        :param wallet:
        :param psbt: The transaction base64 string
        :param sign: Also sign the transaction when updating
        :param sig_hash_type: The signature hash type to sign with if not specified by the PSBT. Must be one of “ALL” “NONE” “SINGLE” “ALL|ANYONECANPAY” “NONE|ANYONECANPAY” “SINGLE|ANYONECANPAY”
        :param bip32_derives: If true, includes the BIP 32 derivation paths for public keys if we know them
        :return:
        """
        return self._provider.make_request(RPC.wallet_processPsbt, [psbt, sign, sig_hash_type, bip32_derives], wallet)
