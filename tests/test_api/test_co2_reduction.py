from archipelago.main import get_app
import json

app = get_app()


def test_co2_routes(test_client) -> None:
    response = test_client.get('/api/recycling/co2-reduction')
    assert response.status_code == 200


def test_spot_price_content(test_client) -> None:
    response = test_client.get('/api/recycling/co2-reduction')
    print(response.content)
    data = json.loads(response.content)
    assert "sequestration" in data
    assert "abatement" in data
    assert "accus_issued" in data
