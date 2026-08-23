from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


def test_item_appears_in_cart(authenticated_page):
    inventory = InventoryPage(authenticated_page)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.cart_link.click()

    cart = CartPage(authenticated_page)
    assert cart.get_item_count() == 1


def test_remove_item_from_cart(authenticated_page):
    inventory = InventoryPage(authenticated_page)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.cart_link.click()

    cart = CartPage(authenticated_page)
    cart.remove_item("sauce-labs-backpack")
    assert cart.get_item_count() == 0


def test_checkout_button_navigates(authenticated_page):
    inventory = InventoryPage(authenticated_page)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.cart_link.click()

    cart = CartPage(authenticated_page)
    cart.go_to_checkout()
    expect(authenticated_page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )
