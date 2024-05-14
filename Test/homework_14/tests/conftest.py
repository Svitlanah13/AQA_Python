import pytest
from src.store.store_facade import StoreFacade, Phone

@pytest.fixture
def store():
    return StoreFacade()

@pytest.fixture(params=[
    {"model": "TestModel1", "price": 1000},
    {"model": "TestModel2", "price": 2000},
])
def phone(request):
    return Phone(request.param["model"], request.param["price"])

@pytest.fixture
def store_with_phone(store, phone):
    store.add_phone_to_catalog(phone.model, phone.price)
    return store, phone