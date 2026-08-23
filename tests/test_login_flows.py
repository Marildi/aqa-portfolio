import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "standard_user",
            "not_secret",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "non_standard_user",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
    ],
)
def test_login_failures(page: Page, username, password, expected_error):
    login = LoginPage(page)
    login.goto()
    login.login(username, password)
    expect(login.error_message).to_be_visible()
    assert expected_error in login.get_error_text()


def test_login_success(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_out_user_cannot_login(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("locked_out_user", "secret_sauce")
    expect(login.error_message).to_be_visible()
    assert "locked out" in login.get_error_text()
