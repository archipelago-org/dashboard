from fastapi import APIRouter
from archipelago.models.blockchain_transaction import BlockchainTxns
import archipelago.services.xrpl_service as xrpl_service

router = APIRouter()


@router.get("/recent-transactions", response_model=BlockchainTxns,
            name="recent_transactions")
async def get_recent_transactions() -> BlockchainTxns:
    txns: BlockchainTxns = await xrpl_service.get_recent_transactions()
    return txns
