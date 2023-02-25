from fastapi import APIRouter
from archipelago.models.transaction import TxnResponse
import archipelago.services.transaction as xrpl_service

router = APIRouter()


@router.get("/recent-transactions", response_model=TxnResponse,
            name="recent_transactions")
async def get_recent_transactions() -> TxnResponse:
    txn: TxnResponse = await xrpl_service.get_recent_transactions()
    return txn
