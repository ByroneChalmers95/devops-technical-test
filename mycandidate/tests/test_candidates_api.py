import json
from main.app import app

def test_get_candidates_by_ward():
    client = app.test_client()
    response = client.get("/api/v1/wards/1/candidates")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert data[0]["name"] == "Candidate A"
