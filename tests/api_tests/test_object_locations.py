from archipelago.main import get_app
import json

app = get_app()


def test_location_routes(test_client) -> None:
    response = test_client.get('/api/geospatial/object-locations')
    assert response.status_code == 200


def test_geo_location_content(test_client) -> None:
    response = test_client.get('/api/geospatial/object-locations')
    print(response.content)
    data = json.loads(response.content)
    assert "latitude" in data["locations"][0]
    assert "longitude" in data["locations"][0]
    assert "weight" in data["locations"][0]
