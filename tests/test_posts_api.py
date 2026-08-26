# Step 45: A small end-to-end test suite (10+ tests) on a public sandbox site — consolidating Phase 3
import pytest
from jsonschema import validate

from utils.constants import BASE_URL


def test_get_single_post_status_code(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


def test_get_single_post_has_expected_fields(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "title" in data
    assert "userId" in data


@pytest.mark.parametrize("post_id", [1, 5, 10, 100])
def test_get_post_by_id_returns_matching_id(post_id, api_session):
    response = api_session.get(f"{BASE_URL}/posts/{post_id}")
    assert response.json()["id"] == post_id


def test_get_nonexistent_post_returns_404(api_session):
    response = api_session.get(f"{BASE_URL}/posts/99999")
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


def test_nonexisting_user_id(api_session):
    result = api_session.get(f"{BASE_URL}/posts/0")
    assert result.status_code == 404


new_post_json = {
    "title": "test",
    "body": "bar",
    "userId": 1,
}


def test_create_post(api_session):
    result = api_session.post(f"{BASE_URL}/posts", json=new_post_json)
    assert result.status_code == 201
    data = result.json()
    assert data["title"] == "test"


@pytest.mark.skip(reason="not merged functionality yet")
def test_generate_income(api_session):
    invoice = api_session.get(f"{BASE_URL}/income")
    assert invoice.status_code == 200


def test_update_post(api_session):
    updated_data = {"id": 1, "title": "updated", "body": "updated body", "userId": 1}
    response = api_session.put(f"{BASE_URL}/posts/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["title"] == "updated"


def test_delete_post(api_session):
    response = api_session.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


# Step 62: requests library in depth — headers, auth, query params, JSON bodies
url = f"{BASE_URL}/posts"


def test_filter_posts(api_session):
    response = api_session.get(url, params={"userId": 1})
    posts = response.json()
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)


def test_json_vs_data_request_body(api_session):
    json_response = api_session.post(
        url, json={"title": "test", "body": "content", "userId": 1}
    )
    data_response = api_session.post(
        url, data={"title": "test", "body": "content", "userId": 1}
    )

    print("JSON request body:", json_response.request.body)
    print("JSON content-type:", json_response.request.headers["Content-Type"])
    print("Data request body:", data_response.request.body)
    print("Data content-type:", data_response.request.headers["Content-Type"])


def test_response_time_is_reasonable(api_session):
    response = api_session.get(url)
    assert (
        response.elapsed.total_seconds() < 2
    ), f"Response took {response.elapsed.total_seconds()}s"


# Step 63: JSON Schema validation (jsonschema library)
post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["id", "title", "body"],
}


def test_post_matches_schema(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    validate(instance=response.json(), schema=post_schema)


# Step 66: Contract testing — what it solves vs. regular API testing
def test_posts_endpoint_honors_contract(api_session):
    """
    Consumer-driven contract check: this schema represents what OUR system
    expects from GET /posts/{id}. If the provider (JSONPlaceholder) changes
    this shape, this test should fail — acting as an early warning before
    real integration breaks.
    """
    response = api_session.get(f"{BASE_URL}/posts/1")
    validate(instance=response.json(), schema=post_schema)
