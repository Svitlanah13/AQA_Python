import pytest
from src.store.store_facade import StoreFacade, Phone

@pytest.fixture
def store():
    return StoreFacade()

@pytest.fixture
def phone():
    return Phone("TestModel", 1000)

@pytest.mark.add
def test_add_phone_to_catalog(store, phone):
    store.add_phone_to_catalog(phone.model, phone.price)
    catalog = store.show_catalog()
    assert len(catalog) == 1
    assert catalog[0].model == phone.model
    assert catalog[0].price == phone.price

@pytest.mark.remove
def test_remove_phone_from_catalog(store, phone):
    store.add_phone_to_catalog(phone.model, phone.price)
    removed_phone = store.remove_phone_from_catalog(phone.model)
    assert removed_phone.model == phone.model
    assert removed_phone.price == phone.price
    assert len(store.show_catalog()) == 0

@pytest.mark.show
def test_show_catalog(store, phone):
    store.add_phone_to_catalog(phone.model, phone.price)
    catalog = store.show_catalog()
    assert len(catalog) == 1
    assert catalog[0].model == phone.model
    assert catalog[0].price == phone.price

@pytest.mark.show
def test_show_catalog_empty(store):
    catalog = store.show_catalog()
    assert len(catalog) == 0

@pytest.mark.remove
def test_remove_nonexistent_phone(store):
    try:
        removed_phone = store.remove_phone_from_catalog("NonExistentModel")
        assert removed_phone is None
    except IndexError:
        assert True