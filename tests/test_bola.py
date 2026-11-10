import pytest

from utils.orders_api import get_order_secure, get_order_vulnerable


# tests for secure function
@pytest.mark.parametrize(
    "user, order_id, expected_status",
    [
        ("bob", "002", 200),  # owner gets in
        ("alice", "001", 200),  # the other owner gets in
        ("bob", "001", 404),  # stranger blocked
        ("alice", "999", 404),  # missing order
    ],
    ids=["owner_bob", "owner_alice", "stranger_blocked", "missing_order"],
)
def test_order_access(user, order_id, expected_status):
    response = get_order_secure(user, order_id)
    assert response["status_code"] == expected_status


# test against vulnerable function
@pytest.mark.xfail(
    reason="vulnerable version leaks other users' orders (BOLA)", strict=True
)
def test_vulnerable_version_leaks_other_users_order():
    result = get_order_vulnerable("bob", "001")
    assert result["status_code"] == 404
