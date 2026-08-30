# import os

import pytest
import requests

# @pytest.fixture
# def temp_results_file():
#     filename = "temp_file.csv"
#     with open(filename, "w") as f:
#         f.write("test_name,status\n")
#         f.write("test_login,Passed\n")
#         f.write("test_logout,Failed\n")
#     yield filename
#     os.remove(filename)


# this version is for parallelism
@pytest.fixture(scope="module")
def temp_results_file(tmp_path_factory):
    filename = tmp_path_factory.mktemp("data") / "temp_file.csv"
    with open(filename, "w") as f:
        f.write("test_name,status\n")
        f.write("test_login,Passed\n")
        f.write("test_logout,Failed\n")
    yield filename
    # no manual cleanup needed - pytest cleans up tmp_path directories automatically


@pytest.fixture
def api_session():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()


@pytest.fixture(scope="session")
def auth_state(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    context.storage_state(path="tests/auth_state.json")
    context.close()
    return "tests/auth_state.json"


@pytest.fixture(scope="session", autouse=True)
def configure_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def authenticated_page(browser, auth_state):
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    yield page
    context.close()


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {**browser_type_launch_args, "headless": True}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1280, "height": 720}}
