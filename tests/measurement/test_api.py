import pytest
from rest_framework.test import APIClient

# def test_example():
#     assert False, "Just test example"

url = '/api/test/'


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_get_response(client):
    response = client.get(url)
    data = response.json()
    assert data == 'Test_3'
    assert response.status_code == 200
