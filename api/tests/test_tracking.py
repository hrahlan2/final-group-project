import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..main import app
from ..dependencies.database import get_db
from ..models import orders
from ..models.orders import Order

client = TestClient(app)

def test_tracking_status_lookup(client, tracking_number=None):
    response = client.get(f"/track/{tracking_number}")
    assert response.status_code == 200
    assert response.json()["status"] == "Order Placed"


@pytest.fixture
def setup_order_with_tracking():
    tracking_number = "TEST123TRACK"


    order = Order(
        customer_id=1,
        order_date="2025-08-07",
        total_amount=10.0,
        tracking_number=tracking_number
    )

def test_get_tracking_status_success(setup_order_with_tracking):
    tracking_number = setup_order_with_tracking
    response = client.get(f"/track/{tracking_number}")
    assert response.status_code == 200
    data = response.json()
    assert data["tracking_number"] == tracking_number
    assert data["status"] == "Order Placed"
    assert "last_updated" in data

def test_get_tracking_status_not_found():
    response = client.get("/track/DOESNOTEXIST")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tracking number not found."