# 47. Locators: CSS, XPath, text, role-based locators — prefer role-based/test-id where possible
# 48. Auto-waiting concept — understand why Playwright rarely needs manual sleeps
# 49. Actions: click, fill, select, hover, drag-and-drop, keyboard/mouse events
# 50. Assertions with expect() — web-first assertions vs generic assert
# from pathlib import Path
# from playwright.sync_api import expect, sync_playwright

# def run():
#     with sync_playwright() as p:
#         p.selectors.set_test_id_attribute("data-test")
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://www.saucedemo.com")
#         expect(page.get_by_role("button", name="Login"))

#         page.get_by_placeholder("Username").fill("standard_user")
#         page.get_by_placeholder("Password").fill("secret_sauce")
#         page.get_by_role("button", name="Login").click()
#         expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
#         expect(page.get_by_test_id("inventory-item")).to_have_count(6)

#         page.get_by_test_id("add-to-cart-sauce-labs-backpack").click()
#         expect(page.get_by_test_id("remove-sauce-labs-backpack")).to_be_visible()
#         page.get_by_test_id("add-to-cart-sauce-labs-bike-light").click()
#         expect(page.get_by_test_id("shopping-cart-badge")).to_have_text("2")

#         page.locator("[data-test='product-sort-container']").select_option(
#             label="Price (low to high)"
#         )
#         # small loop to check each consequent element more expensive than the previous
#         expect(page.get_by_test_id("inventory-item")).to_have_count(6)
#         price_elements = page.get_by_test_id("inventory-item-price").all()
#         previous_element_price = None
#         for price_element in price_elements:
#             price = price_element.text_content()
#             current_element_price = float(price.replace("$", "").strip())

#             if (
#                 previous_element_price is not None
#             ):  # False only on the very first iteration
#                 if previous_element_price > current_element_price:
#                     print("sorting failed")
#                 else:
#                     print("sorting ok")

#             previous_element_price = current_element_price

#         page.get_by_test_id("shopping-cart-link").click()
#         expect(page).to_have_url("https://www.saucedemo.com/cart.html")
#         # expect until all elements are loaded
#         expect(page.get_by_test_id("inventory-item")).to_have_count(2)

#         page.screenshot(path="cart_state.png")
#         page.close()


# run()


# Step 51: Handling iframes, popups, new tabs, file uploads/downloads
# def iframe_run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://the-internet.herokuapp.com/nested_frames")

#         top_frame = page.frame_locator("frame[name='frame-top']")
#         left_text = (
#             top_frame.frame_locator("frame[name='frame-left']")
#             .locator("body")
#             .text_content()
#         )
#         middle_text = (
#             top_frame.frame_locator("frame[name='frame-middle']")
#             .locator("body")
#             .text_content()
#         )
#         right_text = (
#             top_frame.frame_locator("frame[name='frame-right']")
#             .locator("body")
#             .text_content()
#         )

#         print("LEFT:", left_text)
#         print("MIDDLE:", middle_text)
#         print("RIGHT:", right_text)

#         expect(
#             top_frame.frame_locator("frame[name='frame-middle']").locator("body")
#         ).to_have_text("MIDDLE")

#         browser.close()


# def new_page_run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://practice.expandtesting.com/windows")

#         # Catch the new tab using expect_popup()
#         with page.expect_popup() as new_page_info:
#             page.get_by_role("link", name="Click Here").click()

#         # Access the page outside or inside the context block
#         new_page = new_page_info.value
#         new_page.wait_for_load_state()
#         print(new_page.title())

#         page.close()


# def file_upload_run():
#     with sync_playwright() as p:
#         p.selectors.set_test_id_attribute("data-testid")
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://the-internet.herokuapp.com/upload")

#         page.locator("#file-upload").set_input_files(
#             "/home/maryna/Downloads/1787288840924_sampleFile.jpeg"
#         )
#         page.locator("#file-submit").click()
#         expect(page.get_by_text("File Uploaded!")).to_be_visible()
#         print("Upload confirmed")

#         page.close()


# def file_download_run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto("https://the-internet.herokuapp.com/download")

#         with page.expect_download() as download_info:
#             page.get_by_role("link", name="image.png").click()

#         download = download_info.value
#         download.save_as("image.png")
#         print(download.suggested_filename)

#         browser.close()


# iframe_run()
# new_page_run()
# file_upload_run()
# file_download_run()


# Step 52: Network interception — mocking API responses, intercepting requests

# def network_interception_run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()

#         def mock_weather(route):
#             route.fulfill(
#                 status=200,
#                 content_type="application/json",
#                 body='{"temperature": 22, "condition": "sunny"}',
#             )

#         page.route("**/api/weather", mock_weather)
#         page.goto(f"file://{Path.cwd()}/test_page.html")

#         expect(page.locator("#result")).to_have_text(
#             "Temperature: 22, Condition: sunny"
#         )
#         print(page.locator("#result").text_content())

#         browser.close()


# network_interception_run()


# def network_interception_error_run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()

#         def simulate_server_error(route):
#             route.fulfill(
#                 status=500, content_type="text/plain", body="Internal Server Error"
#             )

#         page.route("**/api/weather", simulate_server_error)
#         page.goto(f"file://{Path.cwd()}/test_page.html")

#         expect(page.locator("#result")).to_have_text("Error loading weather")
#         print(page.locator("#result").text_content())

#         browser.close()


# network_interception_error_run()
