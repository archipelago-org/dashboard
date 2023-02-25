from archipelago.main import get_app

app = get_app()


def test_location_routes(test_client) -> None:
    response = test_client.get('/api/blockchain/recent-transactions')
    assert response.status_code == 200
