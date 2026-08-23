# Step 54: Authentication handling: storage state reuse (log in once, reuse session across tests) + Step 55: Page Object Model (POM)
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_save_auth_state(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    page.context.storage_state(path="tests/auth_state.json")


def test_reuse_auth_state(browser):
    context = browser.new_context(storage_state="tests/auth_state.json")
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")

    expect(page.get_by_test_id("inventory-item")).to_have_count(6)
    context.close()


def test_add_to_cart(authenticated_page):
    inventory = InventoryPage(authenticated_page)
    inventory.add_to_cart("sauce-labs-backpack")
    assert inventory.is_item_in_cart("sauce-labs-backpack")


def test_sorting(authenticated_page):
    inventory = InventoryPage(authenticated_page)
    inventory.sort_by("Price (low to high)")

    prices = inventory.get_prices()
    for i in range(1, len(prices)):
        assert prices[i] >= prices[i - 1], f"Sorting failed at index {i}"
