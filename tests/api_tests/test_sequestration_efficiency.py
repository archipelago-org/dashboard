from archipelago.main import get_app
import json

app = get_app()


def test_efficiency_routes(test_client) -> None:
    response = test_client.get('/api/recycling/efficiency')
    assert response.status_code == 200


def test_efficiency_content(test_client) -> None:
    response = test_client.get('/api/recycling/efficiency')
    print(response.content)
    data = json.loads(response.content)
    assert "sequestration_efficiency" in data
