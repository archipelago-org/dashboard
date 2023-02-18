from archipelago.main import get_app

app = get_app()


def test_default_route(test_client) -> None:
    response = test_client.get('/')
    assert response.status_code == 404
