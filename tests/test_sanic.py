from app import app


def test_total():
    url = "http://localhost:8000/total"
    _, response = app.test_client.get(url)

    assert response.status == 200


def test_total_type():
    """without a payload, endpoints should fail."""
    url = "http://localhost:8000/total"
    _, response = app.test_client.get(url)
    r = response.json
    assert isinstance(r[0], int)


def test_save():
    url = "http://localhost:8000/save"
    payload = {"method": "test", "rate": 0}
    _, response = app.test_client.post(url, json=payload)
    assert response.status == 201

