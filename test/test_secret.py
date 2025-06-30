import pytest
from unittest.mock import patch, MagicMock

@patch("boto3.client")
def test_secret(mock_boto_client, client):
    mock_dynamodb = MagicMock()
    mock_dynamodb.get_item.return_value = {
        "Item": {
            "codeName": {"S": "theDoctor"},
            "secretCode": {"S": "12345"}
        }
    }

    mock_boto_client.return_value = mock_dynamodb

    response = client.get('/secret')
    
    assert response.status_code == 200
    data = response.get_json()
    assert "secret_code" in data
    assert data["secret_code"] == {
        "codeName": {"S": "theDoctor"},
        "secretCode": {"S": "12345"}
    }
