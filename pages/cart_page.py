from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.get_by_test_id("inventory-item")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def remove_item(self, product_test_id: str):
        self.page.get_by_test_id(f"remove-{product_test_id}").click()

    def go_to_checkout(self):
        self.checkout_button.click()
