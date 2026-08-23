# Step 54: Authentication handling: storage state reuse (log in once, reuse session across tests)

from playwright.sync_api import expect

# from playwright.sync_api import Page

# def test_save_auth_state(page: Page):
#     page.goto("https://www.saucedemo.com")
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")
#     page.get_by_role("button", name="Login").click()
#     expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

#     page.context.storage_state(path="tests/auth_state.json")

# def test_reuse_auth_state(browser):
#     context = browser.new_context(storage_state="tests/auth_state.json")
#     page = context.new_page()
#     page.goto("https://www.saucedemo.com/inventory.html")

#     expect(page.get_by_test_id("inventory-item")).to_have_count(6)
#     context.close()


def test_add_to_cart(authenticated_page):
    authenticated_page.goto("https://www.saucedemo.com/inventory.html")
    authenticated_page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
    expect(
        authenticated_page.get_by_test_id("remove-sauce-labs-backpack")
    ).to_be_visible()


def test_sorting(authenticated_page):
    authenticated_page.goto("https://www.saucedemo.com/inventory.html")
    authenticated_page.locator("[data-test='product-sort-container']").select_option(
        label="Price (low to high)"
    )
    # small loop to check each consequent element more expensive than the previous
    expect(authenticated_page.get_by_test_id("inventory-item")).to_have_count(6)
    price_elements = authenticated_page.get_by_test_id("inventory-item-price").all()
    previous_element_price = None
    for price_element in price_elements:
        price = price_element.text_content()
        current_element_price = float(price.replace("$", "").strip())

        if previous_element_price is not None:  # False only on the very first iteration
            if previous_element_price > current_element_price:
                print("sorting failed")
            else:
                print("sorting ok")

        previous_element_price = current_element_price
