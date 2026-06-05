from fastapi.testclient import TestClient

from parkinguv.api import app


client = TestClient(app)


def test_calculate_endpoint_returns_fee():
    response = client.get("/calculate", params={"minutes": 91, "vip": True})

    assert response.status_code == 200
    assert response.json()["total"] == 800


def test_calculate_endpoint_rejects_negative_minutes():
    response = client.get("/calculate", params={"minutes": -1})

    assert response.status_code == 400
