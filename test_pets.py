import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture
def pet_data():
    pet = {
        "id": 123456789,
        "name": "TestPet",
        "photoUrls": ["http://example.com/photo"],
        "status": "available"
    }
    return pet

@pytest.fixture
def create_pet(pet_data):
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200
    yield pet_data

    requests.delete(f"{BASE_URL}/pet/{pet_data['id']}")

def test_create_pet(create_pet):
    pet = create_pet
    response = requests.get(f"{BASE_URL}/pet/{pet['id']}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id'] == pet['id']
    assert response_data['name'] == pet['name']
    assert response_data['status'] == pet['status']

def test_read_pet(create_pet):
    pet = create_pet
    response = requests.get(f"{BASE_URL}/pet/{pet['id']}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id'] == pet['id']
    assert response_data['name'] == pet['name']
    assert response_data['status'] == pet['status']

def test_update_pet(create_pet):
    pet = create_pet
    updated_pet = pet.copy()
    updated_pet['name'] = "UpdatedTestPet"
    updated_pet['status'] = "sold"
    response = requests.put(f"{BASE_URL}/pet", json=updated_pet)
    assert response.status_code == 200

    response = requests.get(f"{BASE_URL}/pet/{updated_pet['id']}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id'] == updated_pet['id']
    assert response_data['name'] == updated_pet['name']
    assert response_data['status'] == updated_pet['status']

def test_delete_pet(create_pet):
    pet = create_pet
    response = requests.delete(f"{BASE_URL}/pet/{pet['id']}")
    assert response.status_code == 200

    response = requests.get(f"{BASE_URL}/pet/{pet['id']}")
    assert response.status_code == 404

if __name__ == "__main__":
    pytest.main()
