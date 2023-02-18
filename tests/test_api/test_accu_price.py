from archipelago.main import get_app
import json

app = get_app()


def test_spot_price_route(test_client) -> None:
    response = test_client.get('/api/accu-price/accu-spot-price')
    assert response.status_code == 200


def test_spot_price_content(test_client) -> None:
    response = test_client.get('/api/accu-price/accu-spot-price')
    print(response.content)
    data = json.loads(response.content)
    assert "spot" in data
