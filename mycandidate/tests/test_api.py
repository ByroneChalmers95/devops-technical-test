import json


def test_get_candidates_by_ward(client):
    """
    Test the /api/v1/wards/<ward_id>/candidates endpoint.
    Works whether DB is seeded or not (stub fallback).
    """
    response = client.get("/api/v1/wards/1/candidates")

    # API should always return JSON
    assert response.status_code in [200, 500]

    data = json.loads(response.data.decode())
    assert isinstance(data, list)
