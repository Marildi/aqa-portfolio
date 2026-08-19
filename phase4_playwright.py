from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com")
    print(page.title())
    input("Press Enter to close...")  # pauses so the window stays open
    browser.close()
