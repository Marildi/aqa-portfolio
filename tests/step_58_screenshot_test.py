from playwright.sync_api import Page, expect


def test_deliberate_failure_for_screenshot(page: Page):
    page.goto("https://www.saucedemo.com")
    expect(page.get_by_test_id("this-does-not-exist")).to_be_visible()
