from src.app import app


def test_health():
    _, response = app.test_client.get('/health')
    assert response.status == 200
    assert response.json['database open'] is True
