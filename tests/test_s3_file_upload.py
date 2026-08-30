from playwright.sync_api import expect


def test_deliberate_failure_for_s3_upload_check(page):
    page.goto("https://www.saucedemo.com")
    expect(page.get_by_test_id("this-does-not-exist")).to_be_visible()
