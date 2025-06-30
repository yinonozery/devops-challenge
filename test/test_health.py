import pytest

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert 'status' in data
    assert 'container' in data
    assert 'project' in data
    assert data['status'] == 'healthy'