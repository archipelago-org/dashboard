from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models import AccountTx, Response
from archipelago.models.blockchain_transaction import BlockchainTxns, BlockchainTxn
from xrpl.wallet import Wallet
from datetime import datetime, timedelta
from archipelago.core.config import XRPL_JSON_RPC_URL, XRPL_EXPLORER_URL
import json

# Prototyping data:
FETCH_LIMIT = 5


class XrplService:
    def __init__(self, seed: str, sequence: str):
        self.seed = seed,
        self.sequence = sequence
        self.wallet = Wallet(seed, sequence)
        self.client = AsyncJsonRpcClient(XRPL_JSON_RPC_URL)

    async def get_recent_transactions(self) -> BlockchainTxns:
        retrieved_txns = await self._fetch_txns()
        return self._response(retrieved_txns)

    async def _fetch_txns(self) -> Response:
        acct_txn = AccountTx(
            account=self.wallet.classic_address,
            limit=FETCH_LIMIT,
        )

        return await self.client.request(acct_txn)

    def _response(self, retrieved_txns: Response) -> BlockchainTxns:
        txns: list = []
        for retrieved_txn in retrieved_txns.result["transactions"]:
            if len(retrieved_txn["tx"]["Memos"]) == 0:
                continue
            memo_data = json.loads(
                self._decode(retrieved_txn["tx"]["Memos"][0]["Memo"]["MemoData"]))
            txn = BlockchainTxn(
                date=self._date(retrieved_txn["tx"]["date"]),
                txn_type=retrieved_txn["tx"]["TransactionType"],
                product_code=memo_data["product_code"],
                product_name=memo_data["name"],
                quantity=memo_data["qty"],
                batch=memo_data["batch"],
                block_explorer=XRPL_EXPLORER_URL + retrieved_txn["tx"]["hash"]
            )
            txns.append(txn)

        return BlockchainTxns(txns=txns)

    def _decode(self, hex_string: str) -> str:
        return bytearray.fromhex(hex_string).decode()

    def _date(self, delta: int) -> str:
        base_date = datetime(2000, 1, 1)
        d = base_date + timedelta(seconds=delta)
        return d.strftime("%Y-%m-%d %H:%M:%S")
