from archipelago.main import get_app
import json

app = get_app()


def test_info_route(test_client) -> None:
    response = test_client.get('/api/accu/info')
    assert response.status_code == 200


def test_spot_price(test_client) -> None:
    response = test_client.get('/api/accu/info')
    print(response.content)
    data = json.loads(response.content)
    assert "spot" in data
