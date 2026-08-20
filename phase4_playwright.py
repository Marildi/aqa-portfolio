from playwright.sync_api import sync_playwright

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

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
        page.get_by_test_id("add-to-cart-sauce-labs-bike-light").click()
        page.locator("[data-test='product-sort-container']").select_option(
            "lohi"
        )  # low to high
        page.locator("[data-test='product-sort-container']").select_option(
            label="Price (low to high)"
        )
        page.get_by_test_id("shopping-cart-link").click()
        page.screenshot(path="cart_state.png")
        page.close()


run()
