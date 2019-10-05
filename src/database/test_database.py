from src.app import app


def test_health():
    _, response = app.test_client.get('/v1/database/health')
    assert response.status == 200
    assert response.json['data'] == 'database_v1'


