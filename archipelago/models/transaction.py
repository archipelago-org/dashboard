from pydantic import BaseModel
from typing import List


class Txn(BaseModel):
    date: str
    txn_type: str
    memo_type: str
    memo_data: str
    block_explorer: str


class TxnResponse(BaseModel):
    txns: List[Txn]
