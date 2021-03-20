from btc.rpc_abi import RPC
from typing import Any


class Chain:
    def __init__(self, bitcoin):
        self._bitcoin = bitcoin
        self._provider = bitcoin.provider

    def get_block_count(self):
        """
        Get count of blocks
        :return:
        """
        return self._provider.make_request(RPC.chain_getBlockCount)

    def get_latest_block_hash(self):
        """
        Get latest block hash
        :return:
        """
        return self._provider.make_request(RPC.chain_getBestBlockHash)

    def get_block_hash(self, height: int):
        """
        Get block hash via  height
        :return:
        """
        return self._provider.make_request(RPC.chain_getBlockHash, [height])

    def get_block(self, block_hash: str, verbosity: int):
        """
        Get block data via  block hash
        :param block_hash:
        :param verbosity: 1 or 2, if 1, returns an Object with information about block ‘hash’; if 2, returns an Object with information about block ‘hash’ and information about each transaction.
        :return:
        """
        return self._provider.make_request(RPC.chain_getBLock, [block_hash, verbosity])

    def get_block_states(self, hash_or_height: [int, str], state: Any = "all"):
        """
        Get block statistic info via hash or height
        :param hash_or_height:
        :param state: Statistical indicators
        :return:
        """
        return self._provider.make_request(RPC.chain_getBlockStates, [hash_or_height, state])

    def get_block_chain_info(self):
        """
        Returns an object containing various state info regarding blockchain processing
        :return:
        """
        return self._provider.make_request(RPC.chain_getBlockChainInfo, [])

    def get_chain_tips(self):
        """
        Return information about all known tips in the block tree, including the main chain as well as orphaned branches
        :return:
        """
        return self._provider.make_request(RPC.chain_getChainTips, [])

    def get_chain_tx_stats(self, n_blocks: int = None, block_hash: str = None):
        """
        Compute statistics about the total number and rate of transactions in the chain
        :param n_blocks:
        :param block_hash:
        :return:
        """
        return self._provider.make_request(RPC.chain_getBlockStates, [n_blocks, block_hash])

    def get_difficulty(self):
        """
        Returns the proof-of-work difficulty as a multiple of the minimum difficulty
        :return:
        """
        return self._provider.make_request(RPC.chain_getDifficulty, [])

    def get_mem_pool_ancestors(self, tx_id: str, verbose: bool = False):
        """
        If txid is in the mempool, returns all in-mempool ancestors.
        :param tx_id: The transaction id (must be in mempool)
        :param verbose: True for a json object, false for array of transaction ids
        :return:
        """
        return self._provider.make_request(RPC.chain_getMemPoolAncestors, [tx_id, verbose])

    def get_mem_pool_descendants(self, tx_id: str):
        """
        If txid is in the mempool, returns all in-mempool descendants
        :param tx_id:
        :return:
        """
        return self._provider.make_request(RPC.chain_getMemPoolDescendants, [tx_id])

    def get_mem_pool_entry(self, tx_id: str):
        """
        Returns mempool data for given transaction
        :param tx_id:
        :return:
        """
        return self._provider.make_request(RPC.chain_getMemPoolEntry, [tx_id])

    def get_mem_pool_info(self):
        """
        Returns details on the active state of the TX memory pool.
        :return:
        """
        return self._provider.make_request(RPC.chain_getMemPoolInfo)

    def get_raw_mem_pool(self, verbose: bool = False):
        """
        Returns all transaction ids in memory pool as a json array of string transaction ids.
        Hint: use getmempoolentry to fetch a specific transaction from the mempool.
        :param verbose:
        :return:
        """
        return self._provider.make_request(RPC.chain_getRawMemPool, [verbose])

    def get_tx_out(self, tx_id: str, n: int, include_mempool: bool = False):
        """
        Returns details about an unspent transaction output
        :param tx_id:
        :param n: vout number
        :param include_mempool: Whether to include the mempool. Note that an unspent output that is spent in the mempool won’t appear.
        :return:
        """
        return self._provider.make_request(RPC.chain_getTxOut, [tx_id, n, include_mempool])

    def get_tx_out_proof(self, tx_ids: list, block_hash: str = None):
        """
        Returns a hex-encoded proof that “txid” was included in a block.
        :param tx_ids:
        :param block_hash:
        :return:
        """
        return self._provider.make_request(RPC.chain_getTxOutProof, [tx_ids, block_hash])

    def get_tx_out_set_info(self):
        """
        Returns statistics about the unspent transaction output set.
        :return:
        """
        return self._provider.make_request(RPC.chain_getTxOutSetInfo, [], None, 180)

    def precious_block(self, block_hash: str):
        """
        Treats a block as if it were received before others with the same work.
        :return:
        """
        return self._provider.make_request(RPC.chain_preciousBlock, [block_hash])

    def prune_block_chain(self, height: int):
        """
        Prune block chain
        :param height:The block height to prune up to. May be set to a discrete height, or a unix timestamp to prune blocks whose block time is at least 2 hours older than the provided timestamp
        :return:
        """
        return self._provider.make_request(RPC.chain_pruneBlockChain, [height])

    def verify_chain(self, check_level: int = 3, n_blocks: int = 6):
        """
        Verifies blockchain database
        :param check_level: How thorough the block verification is. default=3, range=0-4
        :param n_blocks: The number of blocks to check. default=6, 0=all
        :return:
        """
        return self._provider.make_request(RPC.chain_verifyChain, [check_level, n_blocks])

    def verify_tx_out_proof(self, proof: str):
        """
        Verifies that a proof points to a transaction in a block, returning the transaction it commits to and throwing an RPC error if the block is not in our best chain
        :param proof: The hex-encoded proof generated by get_tx_out_proof
        :return:
        """
        return self._provider.make_request(RPC.chain_verifyTxOutProof,[proof])