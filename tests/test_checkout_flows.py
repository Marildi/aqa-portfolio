import pytest
from playwright.sync_api import Page, expect

from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def _add_item_and_go_to_checkout(page: Page):
    inventory = InventoryPage(page)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.cart_link.click()
    page.get_by_role("button", name="Checkout").click()


def test_completes_order_successfully(authenticated_page):
    _add_item_and_go_to_checkout(authenticated_page)
    checkout = CheckoutPage(authenticated_page)
    checkout.fill_info("Maryna", "QA", "12345")
    checkout.continue_to_overview()
    checkout.finish_order()
    expect(checkout.confirmation_header).to_have_text("Thank you for your order!")


@pytest.mark.parametrize(
    "first, last, postal, expected_error",
    [
        ("", "QA", "12345", "First Name is required"),
        ("Maryna", "", "12345", "Last Name is required"),
        ("Maryna", "QA", "", "Postal Code is required"),
    ],
)
def test_checkout_validation_errors(
    authenticated_page, first, last, postal, expected_error
):
    _add_item_and_go_to_checkout(authenticated_page)
    checkout = CheckoutPage(authenticated_page)
    checkout.fill_info(first, last, postal)
    checkout.continue_to_overview()
    expect(checkout.error_message).to_be_visible()
    assert expected_error in checkout.get_error_text()
