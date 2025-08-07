from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_create_delivery_option():
    response = client.post("/delivery-options/", json={"order_id": 1, "method": "delivery"})
    assert response.status_code == 200
    assert response.json()["method"] == "delivery"
    assert response.json()["order_id"] == 1