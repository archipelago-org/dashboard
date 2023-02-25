from pydantic import BaseModel
from typing import List


class BlockchainTxn(BaseModel):
    date: str
    txn_type: str
    description: str
    block_explorer: str


class BlockchainTxns(BaseModel):
    txns: List[BlockchainTxn]
