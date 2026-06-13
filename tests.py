from fastapi.testclient import TestClient
from server import server

client = TestClient(server)

def test_health():
    response = client.get("/")
    assert response.status_code == 200