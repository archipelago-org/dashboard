import pytest

from archipelago.services.xrpl_service import get_recent_transactions


@pytest.mark.asyncio
async def test_transactions(test_client) -> None:
    await get_recent_transactions()
