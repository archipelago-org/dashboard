from fastapi import APIRouter
from archipelago.models.blockchain_transaction import BlockchainTxns
from archipelago.services.xrpl_service import XrplService
import os

router = APIRouter()


@router.get("/recent-transactions", response_model=BlockchainTxns,
            name="recent_transactions")
async def get_recent_transactions() -> BlockchainTxns:
    xrpl_service = XrplService(os.environ['SEED'], os.environ['SEQUENCE'])
    txns: BlockchainTxns = await xrpl_service.get_recent_transactions()
    return txns
