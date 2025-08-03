import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def sample_order():
    return {
        "guest_name": "Alice",
        "guest_phone": "1234567890",
        "guest_address": "123 Apple St",
        "status": "pending",
        "items": [
            {"menu_item_id": 1, "quantity": 2},
            {"menu_item_id": 2, "quantity": 1}
        ]
    }

def test_create_guest_order(sample_order):
    response = client.post("/guest-orders/", json=sample_order)
    assert response.status_code == 201
    data = response.json()
    assert data["guest_name"] == "Alice"
    assert data["status"] == "pending"
    assert "tracking_number" in data
