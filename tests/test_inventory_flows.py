import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


@pytest.mark.parametrize(
    "sort_label, ascending",
    [
        ("Price (low to high)", True),
        ("Price (high to low)", False),
    ],
)
def test_sort_by_price(authenticated_page, sort_label, ascending):
    inventory = InventoryPage(authenticated_page)
    inventory.sort_by(sort_label)
    prices = inventory.get_prices()

    if ascending:
        assert prices == sorted(prices)
    else:
        assert prices == sorted(prices, reverse=True)


@pytest.mark.parametrize(
    "sort_label, ascending",
    [
        ("Name (A to Z)", True),
        ("Name (Z to A)", False),
    ],
)
def test_sort_by_name(authenticated_page, sort_label, ascending):
    inventory = InventoryPage(authenticated_page)
    inventory.sort_by(sort_label)
    names = [
        el.text_content()
        for el in authenticated_page.get_by_test_id("inventory-item-name").all()
    ]

    if ascending:
        assert names == sorted(names)
    else:
        assert names == sorted(names, reverse=True)


def test_add_multiple_items_updates_badge(authenticated_page):
    inventory = InventoryPage(authenticated_page)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    badge = authenticated_page.get_by_test_id("shopping-cart-badge")
    expect(badge).to_have_text("2")


def test_product_count_is_six(authenticated_page):
    inventory = InventoryPage(authenticated_page)
    assert inventory.get_product_count() == 6


def test_remove_item_from_inventory_page(authenticated_page):
    inventory = InventoryPage(authenticated_page)
    inventory.add_to_cart("sauce-labs-backpack")
    assert inventory.is_item_in_cart("sauce-labs-backpack")

    authenticated_page.get_by_test_id("remove-sauce-labs-backpack").click()
    assert not inventory.is_item_in_cart("sauce-labs-backpack")
