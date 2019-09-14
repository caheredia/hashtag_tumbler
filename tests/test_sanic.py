from app import app

total_url = "http://localhost:8000/total"


def test_total():
    _, response = app.test_client.get(total_url)

    assert response.status == 200


def test_total_type():
    _, response = app.test_client.get(total_url)
    r = response.json
    assert isinstance(r[0], int)


save_url = "http://localhost:8000/save"


def test_save_status():
    payload = {"write_method": "test", "rate": 0}
    _, response = app.test_client.post(save_url, json=payload)
    assert response.status == 201


def test_save():
    payload = {"write_method": "test", "rate": 0}
    _, response = app.test_client.post(save_url, json=payload)
    assert response.json[0] == "saved"
