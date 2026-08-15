# Step 45: A small end-to-end test suite (10+ tests) on a public sandbox site — consolidating Phase 3
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post_status_code():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


def test_get_single_post_has_expected_fields():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "title" in data
    assert "userId" in data


@pytest.mark.parametrize("post_id", [1, 5, 10, 100])
def test_get_post_by_id_returns_matching_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.json()["id"] == post_id


def test_get_nonexistent_post_returns_404():
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404


@pytest.mark.custom
def get_post_title(get_post_title_api):
    response = get_post_title_api.fetch("title")
    return response["title"]


def test_get_post_title(mocker):
    mocked_dataset = mocker.Mock()
    mocked_dataset.fetch.return_value = {
        "title": "accusamus beatae ad facilis cum similique qui sunt"
    }

    result = get_post_title(mocked_dataset)
    assert result == "accusamus beatae ad facilis cum similique qui sunt"


def test_nonexisting_user_id():
    result = requests.get(f"{BASE_URL}/posts/0")
    assert result.status_code == 404


new_post_json = {
    "title": "test",
    "body": "bar",
    "userId": 1,
}


def test_create_post():
    result = requests.post(f"{BASE_URL}/posts", json=new_post_json)
    assert result.status_code == 201
    data = result.json()
    assert data["title"] == "test"


@pytest.mark.skip(reason="not merged functionality yet")
def test_generate_income():
    invoice = requests.get(f"{BASE_URL}/income")
    assert invoice.status_code == 200
