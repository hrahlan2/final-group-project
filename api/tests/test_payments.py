from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_create_payment():
    response = client.post("/payments/", json={
        "order": 1,
        "card_details": "1234-5678-9876-5432",
        "payment_type": "card",
        "transaction_status": "success"
    })
    assert response.status_code == 200
    assert response.json()["payment_type"] == "card"
