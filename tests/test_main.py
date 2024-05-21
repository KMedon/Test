import requests
import pytest

BASE_URL = 'https://api.example.com'

def test_get_users():
    response = requests.get(f'{BASE_URL}/users')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    data = {'name': 'John Doe', 'email': 'john@example.com'}
    response = requests.post(f'{BASE_URL}/users', json=data)
    assert response.status_code == 201
    assert response.json()['name'] == 'John Doe'

def test_update_user():
    data = {'name': 'John Doe', 'email': 'john.doe@example.com'}
    response = requests.put(f'{BASE_URL}/users/1', json=data)
    assert response.status_code == 200
    assert response.json()['email'] == 'john.doe@example.com'

def test_delete_user():
    response = requests.delete(f'{BASE_URL}/users/1')
    assert response.status_code == 204
