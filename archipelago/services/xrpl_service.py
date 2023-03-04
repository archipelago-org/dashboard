from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models import AccountTx, Response
from archipelago.models.blockchain_transaction import BlockchainTxns, BlockchainTxn
from xrpl.wallet import Wallet
from datetime import datetime, timedelta
import json
import os

# Prototyping data:
LIMIT = 5
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
EXPLORER_URL = "https://blockexplorer.one/xrp/testnet/tx/"


async def get_recent_transactions() -> BlockchainTxns:
    retrieved_txns = await fetch_txns()
    return response(retrieved_txns)


def response(retrieved_txns: Response) -> BlockchainTxns:
    txns: list = []
    for retrieved_txn in retrieved_txns.result["transactions"]:
        if len(retrieved_txn["tx"]["Memos"]) == 0:
            continue
        memo_data = json.loads(
            decode(retrieved_txn["tx"]["Memos"][0]["Memo"]["MemoData"]))
        txn = BlockchainTxn(
            date=date(retrieved_txn["tx"]["date"]),
            txn_type=retrieved_txn["tx"]["TransactionType"],
            product_code=memo_data["product_code"],
            product_name=memo_data["name"],
            quantity=memo_data["qty"],
            batch=memo_data["batch"],
            block_explorer=EXPLORER_URL + retrieved_txn["tx"]["hash"]
        )
        txns.append(txn)

    return BlockchainTxns(txns=txns)


def decode(hex_string: str) -> str:
    return bytearray.fromhex(hex_string).decode()


def date(delta: int) -> str:
    base_date = datetime(2000, 1, 1)
    d = base_date + timedelta(seconds=delta)
    return d.strftime("%Y-%m-%d %H:%M:%S")


async def fetch_txns() -> Response:
    wallet = Wallet(seed=os.environ['SEED'], sequence=os.environ['SEQUENCE'])
    client = AsyncJsonRpcClient(JSON_RPC_URL)

    acct_txn = AccountTx(
        account=wallet.classic_address,
        limit=LIMIT,
    )

    return await client.request(acct_txn)
