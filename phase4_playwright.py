from playwright.sync_api import expect, sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://example.com")
#     print(page.title())
#     input("Press Enter to close...")  # pauses so the window stays open
#     browser.close()


def run():
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-test")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com")
        expect(page.get_by_role("button", name="Login"))

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.get_by_test_id("inventory-item")).to_have_count(6)

        page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
        expect(page.get_by_test_id("remove-sauce-labs-backpack")).to_be_visible()
        page.get_by_test_id("add-to-cart-sauce-labs-bike-light").click()
        expect(page.get_by_test_id("shopping-cart-badge")).to_have_text("2")

        page.locator("[data-test='product-sort-container']").select_option(
            label="Price (low to high)"
        )
        # small loop to check each consequent element more expensive than the previous
        expect(page.get_by_test_id("inventory-item")).to_have_count(6)
        price_elements = page.get_by_test_id("inventory-item-price").all()
        previous_element_price = None
        for price_element in price_elements:
            price = price_element.text_content()
            current_element_price = float(price.replace("$", "").strip())

            if (
                previous_element_price is not None
            ):  # False only on the very first iteration
                if previous_element_price > current_element_price:
                    print("sorting failed")
                else:
                    print("sorting ok")

            previous_element_price = current_element_price

        page.get_by_test_id("shopping-cart-link").click()
        expect(page).to_have_url("https://www.saucedemo.com/cart.html")
        # expect until all elements are loaded
        expect(page.get_by_test_id("inventory-item")).to_have_count(2)

        page.screenshot(path="cart_state.png")
        page.close()


run()
