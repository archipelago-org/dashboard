from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.models import AccountTx, Response
from archipelago.models.transaction import TxnResponse, Txn
from xrpl.wallet import Wallet
from datetime import datetime, timedelta

# Prototyping data:
LIMIT = 5
SEQUENCE = 33195616
TESTNET_SEED = "sEd7JS4SqQhivydnN1YUmcL4dGj2vxn"
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
EXPLORER_URL = "https://blockexplorer.one/xrp/testnet/tx/"


async def get_recent_transactions() -> TxnResponse:
    retrieved_txns = await fetch_txns()
    return response(retrieved_txns)


def response(retrieved_txns: Response) -> TxnResponse:
    txns: list = []
    for retrieved_txn in retrieved_txns.result["transactions"]:
        txn = Txn(
            date=date(retrieved_txn["tx"]["date"]),
            txn_type=retrieved_txn["tx"]["TransactionType"],
            memo_type=decode(retrieved_txn["tx"]["Memos"][0]["Memo"]["MemoType"]),
            memo_data=decode(retrieved_txn["tx"]["Memos"][0]["Memo"]["MemoData"]),
            block_explorer=EXPLORER_URL + retrieved_txn["tx"]["hash"]
        )
        txns.append(txn)

    return TxnResponse(txns=txns)


def decode(hex_string: str) -> str:
    return bytearray.fromhex(hex_string).decode()


def date(delta: int) -> str:
    base_date = datetime(2000, 1, 1)
    d = base_date + timedelta(seconds=delta)
    return d.strftime("%Y-%m-%d %H:%M:%S")


async def fetch_txns() -> Response:
    wallet = Wallet(seed=TESTNET_SEED, sequence=SEQUENCE)
    client = AsyncJsonRpcClient(JSON_RPC_URL)

    acct_txn = AccountTx(
        account=wallet.classic_address,
        limit=LIMIT,
    )

    return await client.request(acct_txn)
