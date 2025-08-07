from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_menu_items():
    response = client.get("/menu-items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
