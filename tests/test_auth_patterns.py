from datetime import datetime, timedelta, timezone

import jwt
import pytest

API_KEY = "valid-secret-key-123"


def call_protected_endpoint(headers: dict) -> dict:
    """Simulates calling a protected endpoint - in reality this would be requests.get(...)"""
    provided_key = headers.get("X-API-Key")
    if provided_key != API_KEY:
        return {"status_code": 401, "body": {"error": "Invalid or missing API key"}}
    return {"status_code": 200, "body": {"data": "secret info"}}


def test_valid_api_key_succeeds():
    response = call_protected_endpoint({"X-API-Key": API_KEY})
    assert response["status_code"] == 200


def test_missing_api_key_fails():
    response = call_protected_endpoint({})
    assert response["status_code"] == 401


def test_wrong_api_key_fails():
    response = call_protected_endpoint({"X-API-Key": "wrong-key"})
    assert response["status_code"] == 401


# JWT
SECRET_KEY = "a_much_longer_test_secret_key_for_hs256_1234567890"  # 32+ bytes


def generate_token(expires_in_seconds: int = 3600) -> str:
    payload = {
        "user": "maryna",
        "exp": datetime.now(timezone.utc) + timedelta(seconds=expires_in_seconds),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def verify_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])


def test_valid_token_decodes_successfully():
    token = generate_token(expires_in_seconds=3600)
    payload = verify_token(token)
    assert payload["user"] == "maryna"


def test_expired_token_raises_error():
    token = generate_token(expires_in_seconds=-10)  # already expired
    with pytest.raises(jwt.ExpiredSignatureError):
        verify_token(token)


def test_tampered_token_raises_error():
    token = generate_token()
    tampered_token = token[:-5] + "xxxxx"  # corrupt the signature
    with pytest.raises(jwt.InvalidTokenError):
        verify_token(token=tampered_token)


def test_bearer_token_header_format():
    token = generate_token()
    headers = {"Authorization": f"Bearer {token}"}
    assert headers["Authorization"].startswith("Bearer ")
    extracted_token = headers["Authorization"].split(" ")[1]
    assert extracted_token == token
