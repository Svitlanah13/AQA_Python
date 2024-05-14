import pytest

@pytest.mark.add
def test_add_phone_to_catalog(store_with_phone):
    store, phone = store_with_phone
    catalog = store.show_catalog()
    assert len(catalog) == 1
    assert catalog[0].model == phone.model
    assert catalog[0].price == phone.price

@pytest.mark.remove
def test_remove_phone_from_catalog(store_with_phone):
    store, phone = store_with_phone
    removed_phone = store.remove_phone_from_catalog(phone.model)
    assert removed_phone.model == phone.model
    assert removed_phone.price == phone.price
    assert len(store.show_catalog()) == 0

@pytest.mark.show
def test_show_catalog(store_with_phone):
    store, phone = store_with_phone
    catalog = store.show_catalog()
    assert len(catalog) == 1
    assert catalog[0].model == phone.model
    assert catalog[0].price == phone.price

@pytest.mark.show
def test_show_catalog_empty(store):
    catalog = store.show_catalog()
    assert len(catalog) == 0

@pytest.mark.parametrize("model", [
    "NonExistentModel",
    "TestModel1",
])
@pytest.mark.remove
def test_remove_nonexistent_phone(store, model):
    with pytest.raises(IndexError):
        store.remove_phone_from_catalog(model)

