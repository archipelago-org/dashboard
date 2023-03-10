import pytest

from archipelago.services.xrpl_service import XrplService

@pytest.mark.asyncio
async def test_transactions(test_client) -> None:
    await XrplService().get_recent_transactions()
