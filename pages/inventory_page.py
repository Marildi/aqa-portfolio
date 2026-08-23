# pages/inventory_page.py
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.get_by_test_id("shopping-cart-link")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")

    def add_to_cart(self, product_test_id: str):
        self.page.get_by_test_id(f"add-to-cart-{product_test_id}").click()

    def is_item_in_cart(self, product_test_id: str) -> bool:
        return self.page.get_by_test_id(f"remove-{product_test_id}").is_visible()

    def sort_by(self, label: str):
        self.sort_dropdown.select_option(label=label)

    def get_prices(self) -> list[float]:
        price_elements = self.page.get_by_test_id("inventory-item-price").all()
        return [
            float(p.text_content().replace("$", "").strip()) for p in price_elements
        ]
