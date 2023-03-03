from pydantic import BaseModel
from typing import List


class BlockchainTxn(BaseModel):
    date: str
    txn_type: str
    product_code: str
    product_name: str
    quantity: int
    batch: int
    block_explorer: str


class BlockchainTxns(BaseModel):
    txns: List[BlockchainTxn]
